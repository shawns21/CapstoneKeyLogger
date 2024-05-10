import aiohttp
import asyncio

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

async def main():
    url = "https://famous-parrots-remain.loca.lt"
    while True:
        userInput = input("Enter num: ")
        payload = {"number": int(userInput)}
        await sendNum(userInput, url, payload)

if __name__ == "__main__":
    asyncio.run(main())
