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
print(request)
'''
car_id: 95
driver_id: "McQueen"
passenger_ids: "p1"
passenger_ids: "p2"
passenger_ids: "p3"
type: POOL
location {
  lat: 32.564322
  lng: 34.123245
}
time {
  seconds: 1644763182
}
'''

# ToDatetime
time2 = request.time.ToDatetime()
print(type(time2), time2)
# <class 'datetime.datetime'> 2022-02-13 14:39:42

# Now
from google.protobuf.timestamp_pb2 import Timestamp
now = Timestamp()
now.GetCurrentTime()
print(now)
'''
seconds: 1711863744
nanos: 17003000
'''