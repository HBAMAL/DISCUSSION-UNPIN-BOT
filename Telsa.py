import os 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel


HB = Client(
    "MSG_DELETING Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """HI {}, 
I CAN UNPIN MESSAGES IN YOUR GROUP WHEN YOU POST ON THE CONNECTED CHANNEL
MADE BY @TELSABOTS
"""
HELP_TEXT = """
 ADD ME TO UR DISCUSSION GROUP AS ADMIN 
THEN SEE THE MAGIC 🥳
MADE BY @TELSABOTS
"""
ABOUT_TEXT = """
 🤖<b>BOT:DISCUSS UNPIN🤖</b>
 
📢<b>CHANNEL :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS❤️</a>

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

 
🤩<b>SOURCE :</b> 🤩 <a href='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'>CLICK HERE❤️</a>

"""

SOURCE_TEXT = """</b>PRESS SOURCE BUTTON FOR SOURCE 
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🤩SOURCE🤩', url='https://youtu.be/sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
    
@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
@HB.on_message(filters.command(["Source", "s"]))
async def Source_message(bot, update):
    text = SOURCE_TEXT
    reply_markup = SOURCE_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )     
    
@HB.on_message(filters.linked_channel & filters.group)
async def delete(c, m):
    bot = await c.get_me()
    bot_permissions = await m.chat.get_member(bot.id)
    if not bot_permissions.can_delete_messages:
        return await m.reply_text("BRO MAKE ME AS ADMIN WITH AT LEAST MSG 🗑 PERMISSION ")
    await m.delete()


HB.run()
