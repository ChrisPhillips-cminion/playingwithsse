import http from 'http';




// Function to send events to the client
function sendEvent(res, event, data) {
  res.write(`event: ${event}\n`);
  res.write(`data: ${JSON.stringify(data)}\n\n`);
}

// Create HTTP server
const server = http.createServer((req, res) => {
  // Header to indicate that SSE events are being sent


  const headers = {
    'Access-Control-Allow-Origin': '*', /* @dev First, read about security */
    'Access-Control-Allow-Methods': 'OPTIONS, POST, GET',
    'Access-Control-Max-Age': 2592000, // 30 days
    /** add other headers as per requirement */
  };

  if (req.method === 'OPTIONS') {
    res.writeHead(204, headers);
    res.end();
    return;
  }


  if (['GET', 'POST'].indexOf(req.method) > -1) {
    res.writeHead(200, headers);

  // Send an event every 5 seconds
    const interval = setInterval(() => {
      sendEvent(res, 'message', { message: 'Hello from the server' });
    }, 5000);

  // Handle client connection close
    req.on('close', () => {
      clearInterval(interval);
      console.log('Client disconnected');
    });
  }
});

const port = 3030;
server.listen(port, () => {
  console.log(`SSE server started on http://localhost:${port}`);
});
