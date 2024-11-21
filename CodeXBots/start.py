from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant, PeerIdInvalid, UserIsBlocked
from CodeXBots.database import rkn_botz
from CodeXBots.fsub import force_sub
from configs import rkn1
import random, asyncio, os

@Client.on_chat_join_request()
async def approve_request(bot, m):
    try:
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
        await bot.send_message(m.from_user.id, "**{},\n\n𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖳𝗈 𝖩𝗈𝗂𝗇 {} 𝖺𝗌 𝖻𝖾𝖾𝗇 𝖠𝖼𝖼𝖾𝗉𝗍𝖾𝖽.**".format(m.from_user.mention, m.chat.title))
        await rkn_botz.add_user(bot, m)
    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid as err:
        print(f"user isn't start bot (means group) Error- {err}")
    except Exception as err:
        print(f"Error\n{str(err)}")


@Client.on_message(filters.command("start"))
async def command(bot, m: Message):
    await rkn_botz.add_user(bot, m)
    await force_sub(bot, m, rkn1.FORCE_SUB)
    await m.reply_text(f"{m.from_user.mention},\n\n𝖨 𝖼𝖺𝗇 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝗂𝖼𝖺𝗅𝗅𝗒 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 𝗎𝗌𝖾𝗋𝗌 𝗂𝗇 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌.\n\n𝖩𝗎𝗌𝗍 𝖺𝖽𝖽 𝗆𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝖺𝗇𝖽 𝗀𝗋𝗈𝗎𝗉𝗌 𝗐𝗂𝗍𝗁 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇 𝗍𝗈 𝖺𝖽𝖽 𝗇𝖾𝗐 𝗆𝖾𝗆𝖻𝖾𝗋𝗌.\n\nᴅᴇᴠᴇʟᴏᴘᴇʀ : @CodeXBro",
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆", url=f"https://telegram.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat"),
                        ],[
                            InlineKeyboardButton("• ᴜᴩᴅᴀᴛᴇꜱ •", url="https://telegram.me/RahulRevirwsYT"),
                            InlineKeyboardButton("• ꜱᴜᴩᴩᴏʀᴛ •", url="https://telegram.me/CodeXSupport")
                        ],[
                            InlineKeyboardButton("⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆", url=f"https://telegram.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                        ]]))

@Client.on_message(filters.command("help"))
async def codexbots(bot, message):
    btn = [[
        InlineKeyboardButton(text='👨‍💻 ᴏᴡɴᴇʀ', url='https://telegram.me/CodeXBro'),
        InlineKeyboardButton(text='💥 ʀᴇᴘᴏ', url='https://github.com/CodeXBots/Auto-Approve-Bot')
    ]]
    await message.reply_photo(photo='https://envs.sh/jbi.jpg', caption="<blockquote>❤️‍🔥 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</blockquote>\n\n<b><i>💞  ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴏᴜʀ ʙᴏᴛ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ₹𝟷𝟶, ₹𝟸𝟶, ₹𝟻𝟶, ₹𝟷𝟶𝟶, ᴇᴛᴄ.</i></b>\n\n❣️ 𝐷𝑜𝑛𝑎𝑡𝑖𝑜𝑛𝑠 𝑎𝑟𝑒 𝑟𝑒𝑎𝑙𝑙𝑦 𝑎𝑝𝑝𝑟𝑒𝑐𝑖𝑎𝑡𝑒𝑑 𝑖𝑡 ℎ𝑒𝑙𝑝𝑠 𝑖𝑛 𝑏𝑜𝑡 𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡\n\n💖 𝐔𝐏𝐈 𝐈𝐃 : <code>RahulReviews@UPI</code>", reply_markup=InlineKeyboardMarkup(btn))
