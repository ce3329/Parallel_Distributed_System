from fastapi import FastAPI
from .tasks import process_message

app = FastAPI()

@app.post("/send-messages/")
async def send_messages(count: int = 1000):
    for i in range(count):
        process_message.delay(i)
    return {"status": "Messages sent"}
