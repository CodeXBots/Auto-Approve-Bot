from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import os, sys, time, asyncio, logging, datetime, pytz
from CodeXBots.database import rkn_botz
from configs import rkn1


@Client.on_message(filters.command(["stats", "status"]) & filters.user(rkn1.ADMIN))
async def get_stats(bot, message):
    total_users = await rkn_botz.total_users_count()
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - bot.uptime))    
    start_t = time.time()
    rkn = await message.reply('**ᴘʀᴏᴄᴇssɪɴɢ.....**')    
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rkn.edit(text=f"**--Bᴏᴛ Sᴛᴀᴛᴜꜱ--** \n\n**⌚️ Bᴏᴛ Uᴩᴛɪᴍᴇ:** {uptime} \n**🐌 Cᴜʀʀᴇɴᴛ Pɪɴɢ:** `{time_taken_s:.3f} ᴍꜱ` \n**👭 Tᴏᴛᴀʟ Uꜱᴇʀꜱ:** `{total_users}`")

# Restart to cancell all process 
@Client.on_message(filters.private & filters.command("restart") & filters.user(rkn1.ADMIN))
async def restart_bot(b, m):
    rkn = await b.send_message(text="**🔄 ᴘʀᴏᴄᴇssᴇs sᴛᴏᴘᴘᴇᴅ. ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛɪɴɢ.....**", chat_id=m.chat.id)
    failed = 0
    success = 0
    deactivated = 0
    blocked = 0
    start_time = time.time()
    total_users = await rkn_botz.total_users_count()
    all_users = await rkn_botz.get_all_users()
    async for user in all_users:
        try:
            restart_msg = f"ʜᴇʏ, {(await b.get_users(user['_id'])).mention}\n\n**🔄 ᴘʀᴏᴄᴇssᴇs sᴛᴏᴘᴘᴇᴅ. ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛɪɴɢ.....\n\n✅️ ʙᴏᴛ ɪs ʀᴇsᴛᴀʀᴛᴇᴅ. ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ.**"
            await b.send_message(user['_id'], restart_msg)
            success += 1
        except InputUserDeactivated:
            deactivated +=1
            await rkn_botz.delete_user(user['_id'])
        except UserIsBlocked:
            blocked +=1
            await rkn_botz.delete_user(user['_id'])
        except Exception as e:
            failed += 1
            await rkn_botz.delete_user(user['_id'])
            print(e)
            pass
        try:
            await rkn.edit(f"<u>ʀᴇsᴛᴀʀᴛ ɪɴ ᴩʀᴏɢʀᴇꜱꜱ:</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {total_users}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
        except FloodWait as e:
            await asyncio.sleep(e.value)
    completed_restart = datetime.timedelta(seconds=int(time.time() - start_time))
    await rkn.edit(f"ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʀᴇsᴛᴀʀᴛ: {completed_restart}\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {total_users}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
    
@Client.on_message(filters.command("broadcast") & filters.user(rkn1.ADMIN) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    broadcast_msg = m.reply_to_message
    if not broadcast_msg:
        await m.reply_text("Please reply to a message to broadcast.")
        return

    await bot.send_message(rkn1.LOG_CHANNEL, f"{m.from_user.mention} or {m.from_user.id} started the broadcast.")
    all_users = await rkn_botz.get_all_users()
    total_users = await rkn_botz.total_users_count()

    sts_msg = await m.reply_text("Broadcast started...")
    success, failed, done = 0, 0, 0
    start_time = time.time()

    for user in all_users:
        sts = await send_msg(user['_id'], broadcast_msg)
        if sts == 200:
            success += 1
        else:
            failed += 1
            if sts == 400:
                await rkn_botz.delete_user(user['_id'])

        done += 1
        if not done % 50:  # Update every 50 users
            await sts_msg.edit(
                f"Broadcast In Progress:\n"
                f"Total Users: {total_users}\n"
                f"Completed: {done}/{total_users}\n"
                f"Success: {success}\nFailed: {failed}"
            )

    completed_in = str(datetime.timedelta(seconds=int(time.time() - start_time)))
    await sts_msg.edit(
        f"Broadcast Completed:\n"
        f"Completed In: `{completed_in}`\n"
        f"Total Users: {total_users}\n"
        f"Completed: {done}/{total_users}\n"
        f"Success: {success}\nFailed: {failed}"
    )

           
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : Bʟᴏᴄᴋᴇᴅ Tʜᴇ Bᴏᴛ")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : Uꜱᴇʀ Iᴅ Iɴᴠᴀʟɪᴅ")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500
