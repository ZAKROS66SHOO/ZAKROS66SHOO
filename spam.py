from pyrogram import Client
import asyncio
app = Client("sJJJJJ",api_id=15551290,api_hash="52541a59f55c6f54678a4ec33e708e0f")
app.start()
target = input("Enter Target : @")
msg = input('Enter Msg For Spam')
async def main():
    while True:
        await app.send_message(target,msg)
asyncio.get_event_loop().run_until_complete(main())