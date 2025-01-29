# WebSocket Data Server

A WebSocket server using `aiohttp` to stream random data (Pressure, Temperature, Flow).

## Requirements:
- Python 3.7+
- `aiohttp`

## Setup:
1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python server.py
   ```

## Endpoints:
- `/ws/pressure`
- `/ws/temperature`
- `/ws/flow`