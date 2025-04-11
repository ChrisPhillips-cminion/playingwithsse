 
import requests
import time

def sse_client():
    url = "http://localhost:8000/events"

    while True:
        response = requests.get(url, stream=True)
        for line in response.iter_lines():
            if line:
                event = line.decode().strip().split(": ")[1]
                print(f"Received event: {event}")
                time.sleep(1)

if __name__ == "__main__":
    sse_client()
