import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("Aleykum Salam😁 ",

@client.on(events.NewMessage(pattern="^/help$"))
async def start(event):
  await event.reply("saxaiyqi daaaa ",



@app.on_message(filters.command("salam"))
async def _py(client: Client, message: Message):
   await message.reply_text('Aleykum Salam')



 



 
@client.on(events.NewMessage(pattern="^nə$"))
async def start(event):
  await event.reply("zəhər😁 ",

print(">> Bot işləyir narahat olma 🚀 məlumat almaq üçün @ThrHassan yazın <<")
client.run_until_disconnected()
