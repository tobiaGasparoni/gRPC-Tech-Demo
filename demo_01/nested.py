import rides_pb2 as pb

loc = pb.Location(
    lat=32.564322,
    lng=34.123245
)
print(loc)
'''
lat: 32.564322
lng: 34.123245
'''

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
'''
print('lat:', request.location.lat) # 32.564322