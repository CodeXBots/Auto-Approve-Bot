from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant

async def force_sub(bot, message, sub_id):
    chat = await bot.get_chat(int(sub_id))
    try:
        await bot.get_chat_member(sub_id, message.from_user.id)
    except UserNotParticipant:
        return await message.reply_text(f"👋 Hello {message.from_user.mention},\n\nPlease join my 'Updates Channel'. 😇", 
        reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton(f'Join {chat.title}', url=chat.invite_link)
        ]]))                      
    except Exception as e:
        pass
