import asyncio
from datetime import datetime
import json
from aiohttp import web

from aiohttp_sse import sse_response


async def hello(request: web.Request) -> web.StreamResponse:
    async with sse_response(request) as resp:
        while resp.is_connected():
            time_dict = {"time": f"Server Time : {datetime.now()}"}
            data = json.dumps(time_dict, indent=2)
            print(data)
            await resp.send(data)
            await asyncio.sleep(1)
    return resp


async def index(_request: web.Request) -> web.StreamResponse:
    html = """
        <html>
            <body>
                <script>
                    var eventSource = new EventSource("/hello");
                    eventSource.addEventListener("message", event => {
                        document.getElementById("response").innerText = event.data;
                    });
                </script>
                <h1>Response from server:</h1>
                <div id="response"></div>
            </body>
        </html>
    """
    return web.Response(text=html, content_type="text/html")


app = web.Application()
app.router.add_route("GET", "/hello", hello)
app.router.add_route("GET", "/", index)
web.run_app(app, host="0.0.0.0", port=8000)
