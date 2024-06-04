from telethon import TelegramClient, events
from telethon.sessions import StringSession
import time
from a_const_element import *
import pandas as pd

api_id = api_id
api_hash = api_hash
channel = channel
file_path = file_path
file_name = file_name
l_target_user = l_target_user
content_message = content_message

# Login
client =  TelegramClient("session_send_mess", api_id, api_hash)

async def send_mess():
    for target_user in l_target_user:
    # try:
        await client.send_message(target_user, content_message, parse_mode="html")
        time.sleep(3)
    # except:
        # pass
with client:
    client.loop.run_until_complete(send_mess())

       
# async for target_user in l_target_user:
#     client.loop.run_until_complete(send_mess(target_user))
#     time.sleep(3)

