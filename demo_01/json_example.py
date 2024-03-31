from datetime import datetime

import rides_pb2 as pb

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3'],
    type=pb.POOL,
    location=pb.Location(
        lat=32.564322,
        lng=34.123245
    )
)
time = datetime(2022, 2, 13, 14, 39, 42)
request.time.FromDatetime(time)

# json
from google.protobuf.json_format import MessageToJson

data = MessageToJson(request)
print(data)

'''
{
  "carId": "95",
  "driverId": "McQueen",
  "passengerIds": [
    "p1",
    "p2",
    "p3"
  ],
  "type": "POOL",
  "location": {
    "lat": 32.564322,
    "lng": 34.123245
  },
  "time": "2022-02-13T14:39:42Z"
}
'''

# size
print('encode size')
print('- json   :', len(data)) # 214
print('- protobuf:', len(request.SerializeToString())) # 53