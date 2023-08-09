from datetime import datetime
from ntplib import NTPClient
async def return_server_time():
    client = NTPClient()
    response = client.request('inocar.ntp.ec')
    server_time = datetime.fromtimestamp(response.tx_time)
    return server_time