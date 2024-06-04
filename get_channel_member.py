import streamlit as st
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
from qrcode import QRCode


api_id= "22426383"
api_hash = "dbe56731ecfba79f74871b0b486556b1"
bot_token = "7135735816:AAFiOPeeK2mY9ygFibA5wr9NB_agG8g2AUg"

channel = "chungkhoanDNSE"


# client = TelegramClient(StringSession(), api_id, api_hash)

# client.start(bot_token=bot_token)
# client.send_message(PeerUser(1968641665), 'Hi bác,')

# with TelegramClient('bot', api_id, api_hash) as client:
#     # print(len(client.iter_participants(channel)))
#     l_user = []
#     for user in client.iter_participants(channel):
#         if not user.deleted:
#             l_user.append(user.username)
#             # print(f"id: {user.id}, username: @{user.username}")
#     print(len(l_user))
# async def send_message_to_user():
#     await client.start(bot_token=bot_token)
#     # Send a message to the user by their ID
#     await client.send_message(PeerUser(1968641665), 'Hello!')

# with client:
#     client.loop.run_until_complete(send_message_to_user())

# with TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token) as client:
#     user = client.get_entity(1968641665)
#     client.send_message(user, 'Hello!')

# client_send_message = TelegramClient('send_message', api_id, api_hash)
# phone_number="+84947385048"
# async def send_code(client, phone_number):
#     await client.connect()
#     await client.send_code_request(phone_number)
# phone_number="+84947385048"
# client = TelegramClient(phone_number, api_id, api_hash)


# async def send_message():
#     text = "Siu: @TramDauTuBot"
#     await client.send_message("@thangkhong", text, parse_mode="html")

# with client:
#     # client.loop.run_until_complete(login_telegram())
#     client.loop.run_until_complete(send_message())

with TelegramClient('anon', api_id, api_hash) as client:
    client.start()

    # Now you can use the client for any operations
    # For example, sending a message to yourself
    client.send_message('me', 'Hello, myself!')