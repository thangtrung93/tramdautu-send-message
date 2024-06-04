import tkinter as tk
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


# Function: Get member list of Channel
with client:
    l_user = []
    for user in client.iter_participants(channel):
        if not user.deleted:
            l_user.append({"user_id":user.id, "user_username":user.username})
            # print(f"id: {user.id}, username: @{user.username}")
    df = pd.DataFrame(l_user)
    print(pd.DataFrame(l_user))

# Save file: Choose location to save df
df.to_excel(file_path + file_name, index=False)

