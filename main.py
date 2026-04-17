import os
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

# --- RENDER KEEP ALIVE ---
app_web = Flask('')
@app_web.route('/')
def home(): return "ID Extractor is Alive!"
def run(): app_web.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# --- CONFIG ---
API_ID = 32244889 
API_HASH = "cb2f194931d477417c78f43c80c3deb2"
BOT_TOKEN = "8780531616:AAFbhhisSxbhOlGm5lx6NZ46FKxAEbh9png"

bot = Client("IdExtractor", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private & (filters.document | filters.video | filters.audio | filters.photo))
async def send_file_id(client, message):
    # Check if it's a document, photo, etc.
    file_type = message.media
    file_obj = getattr(message, file_type.value)
    
    # Extract File ID
    file_id = getattr(file_obj, "file_id", "ID nahi mil saki")
    
    await message.reply_text(
        f"✅ **File Type:** {file_type.value.capitalize()}\n\n"
        f"📋 **File ID:**\n`{file_id}`\n\n"
        f"👆 *Isko copy karke apne main bot ke code mein daal lo.*"
    )

if __name__ == "__main__":
    keep_alive()
    print("ID Extractor Bot Starting... 🚀")
    bot.run()
  
