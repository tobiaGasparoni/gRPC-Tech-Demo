import rides_pb2 as pb

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3']
)

print(request)

'''
car_id: 95
driver_id: "McQueen"
passenger_ids: "p1"
passenger_ids: "p2"
passenger_ids: "p3"
'''

# Marshal
data = request.SerializeToString()
print('type:', type(data)) # <class 'bytes'>
print('size:', len(data)) # 23

# Unmarshal
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)

'''
car_id: 95
driver_id: "McQueen"
passenger_ids: "p1"
passenger_ids: "p2"
passenger_ids: "p3"
'''