import zmq
import json

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for x in range(1, 9):
    i = str(x)
    testShift = {
    "first_name": f"person {i}",
    "last_name": f"lastName {i}",
    "shifts": f"shift 0, shift {i}",
    "days_working": f"myDays {i}",
    "trained_rotations": f"myPositions {i}",
    "comments": f"myComments {i}"
                    }
    
    testShift = json.dumps(testShift)
    createReq = f"CREATE{testShift}"
    # Send the request to create shift
    socket.send_string(createReq) 
    #  Get reply
    message = socket.recv()
    print(f"Received reply: [ {message.decode()} ]")
    

lastShift = {
    "first_name": "Jane",
    "last_name": "Doe",
    "shifts": "shift 2, shift 4, shift 5",
    "days_working": "someDays",
    "trained_rotations": "somePositions",
    "comments": "someComments"
                    }
    
lastShift = json.dumps(lastShift)
createReq = f"CREATE{lastShift}"
# Send the request to create shift
socket.send_string(createReq) 
#  Get reply
message = socket.recv()
print(f"Received reply: [ {message.decode()} ]")
    
# Send the request to fetch
socket.send_string("FETCH") 
#  Get reply
message = socket.recv()
print(f"Received reply: [ {message.decode()} ]")