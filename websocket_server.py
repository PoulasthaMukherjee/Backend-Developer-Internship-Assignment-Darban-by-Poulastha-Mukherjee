import asyncio
import websockets
import json

async def handle_message(websocket):
    async for message in websocket:
        # Process the message: echo, reverse, count
        echo = message
        reverse = message[::-1]
        last_char = message[-1]
        count = message.count(last_char) - 1

        # Construct the JSON response
        response_data = {
            "Message": echo,
            "Reverse": reverse,
            "Last Character": last_char,
            f"Occurrences of {last_char} (excluding the last character)": count  
        }
        json_response = json.dumps(response_data)

        # Send the JSON response with a delay between characters
        for char in json_response:
            await websocket.send(char)
            await asyncio.sleep(0.1)  # 0.1-second delay

async def main():
    async with websockets.serve(handle_message, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())