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
            asyncio.run(send())
        elif event.name == "space":
            cur.append(" ")
        elif event.name == "backspace":
            pass
        else:
            cur.append(event.name)

async def send():
    url = "https://clever-snakes-worry.loca.lt"
    userInput = "".join(cur)
    payload = {"number": userInput}
    await sendNum(userInput, url, payload)

async def main():
    keyboard.on_press(on_key_event)
    await asyncio.sleep(float('inf'))

if __name__ == "__main__":
    asyncio.run(main())
