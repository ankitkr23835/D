#import keep_alive

from telethon import TelegramClient, events
from googletrans import Translator
from langdetect import detect

# Replace these with your own values
API_ID = 29109690
API_HASH = '74c9033cbfd088fadf148295595d8eb4'
BOT_TOKEN = '6467854416:AAE_t361n2MPdejif5jDRCfVcsKkUr2ARIk'

# Initialize the Telegram client
client = TelegramClient('telethon_bot_session', API_ID, API_HASH)

# Initialize the Translator
translator = Translator()

# Function to handle incoming messages
@client.on(events.NewMessage)
async def translate_message(event):
    if event.is_group:
        chat = await event.get_chat()
        chat_id = event.chat_id
        if event.out:
            # Avoid processing the bot's own messages to prevent loops
            return
        try:
            # Detect the language of the message
            original_message = event.message.message
            detected_language = detect(original_message)

            # Check if the detected language is not None and not English, then translate
            if detected_language and detected_language != 'en':
                translated_message = translator.translate(original_message, dest='en')
                translated_text = translated_message.text
                if original_message != translated_text:
                    await event.reply(f"Translated Message: {translated_text}")
        except Exception as e:
            print(f"Error translating message: {e}")

# Start th
#keep_alive.keep_alive()
client.start()
client.run_until_disconnected()
