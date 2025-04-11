 
import ssl
import socket
import requests

import time

# context = ssl.create_default_context()
# context.check_hostname = False
# context.verify_mode = ssl.CERT_NONE

# Using SSLContext with socket
# sock = socket.create_connection((host, port))
# wrapped_sock = context.wrap_socket(sock, server_hostname=host)

def sse_client():
    # url = "http://sse-sse.apps.bubble.hur.hdclab.intranet.ibm.com/events"
    url = "http://localhost:8080/hello"
    # url = "https://small-ocp2-gw-gateway-apic2.apps.bubble.hur.hdclab.intranet.ibm.com/dev/sandbox/seetest"
    while True:
        response = requests.get(url, headers={"x-ibm-client-id":"b94c7746b9b23a61037c3ebde3c3f173"}, stream=True, verify=False)
        for line in response.iter_lines():
            if line:
                event = line.decode()
                print(f"Received event: {event}")
                time.sleep(1)

if __name__ == "__main__":
    sse_client()
