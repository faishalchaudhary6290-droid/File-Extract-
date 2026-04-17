import os
from flask import Flask
from threading import Thread
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# --- RENDER KEEP ALIVE ---
server = Flask('')
@server.route('/')
def home(): return "Bot is Alive! 🚀"
def run(): server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# --- CONFIGURATION ---
API_ID = 32244889 
API_HASH = "cb2f194931d477417c78f43c80c3deb2"
BOT_TOKEN = "8780531616:AAFbhhisSxbhOlGm5lx6NZ46FKxAEbh9png"

# --- YAHAN NAYI IDs DALNA ---
FILES = {
    "ray": "YAHAN_NAYI_ID_DALO",
    "rare": "YAHAN_NAYI_ID_DALO",
    "stark": "YAHAN_NAYI_ID_DALO",
    "delta": "YAHAN_NAYI_ID_DALO"
}

app = Client("BypassBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 1. ID NIKALNE WALA FEATURE (Bot ko file bhejo ye ID dega)
@app.on_message(filters.private & filters.document)
async def get_id(client, message):
    file_id = message.document.file_id
    await message.reply_text(f"✅ **Nayi File ID:**\n\n`{file_id}`\n\nIs ID ko copy karo aur code mein update karo.")

# 2. START COMMAND
@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"👋 Hello **{message.from_user.first_name}**!\nNeeche buttons se file download karein:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📁 StudyRay", callback_data="file_ray"), InlineKeyboardButton("📁 StudyRare", callback_data="file_rare")],
            [InlineKeyboardButton("📁 StudyStark", callback_data="file_stark"), InlineKeyboardButton("📁 DeltaStudy", callback_data="file_delta")]
        ])
    )

# 3. BUTTONS KA KAAM
@app.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data.startswith("file_"):
        key = data.split("_")[1]
        file_id = FILES.get(key)
        try:
            await query.message.reply_document(file_id)
            await query.answer("File bheji ja rahi hai...")
        except:
            await query.answer("❌ Error: ID purani hai! Bot ko file bhej kar nayi ID lo.", show_alert=True)

if __name__ == "__main__":
    keep_alive()
    app.run()
