# Usage

This microservice communicates with the client using **ZeroMQ**. To enable communication, import the required dependencies for your programming language. Next, connect your program to socket 5555, following the ZeroMQ documentation.

## CREATE Request

To send a CREATE request, use the ZeroMQ **socket.send_string( )** method. The sent string must be formatted as **“CREATE”** followed by a JSON object containing the first_name, last_name, shifts, days_working, trained_rotations, and comments fields, which should be filled according to the database schema.

### Example Request:
    socket.send_string( 
    	“CREATE”{
    	    "first_name": "Jane",
    	    "last_name": "Doe",
    	    "shifts": "shift 2, shift 4, shift 5",
    	    "days_working": "someDays",
    	    "trained_rotations": "somePositions",
    	    "comments": "someComments"
			})


## FETCH Request

To send a FETCH request, use the ZeroMQ **socket.send_string( )** method. The sent string must be formatted as **“CREATE”** followed by nothing else.

### Example Request:

    socket.send_string(“FETCH”)

## Responses

To receive a response, use the ZeroMQ **socket.recv( )** method to listen for the outcome of the request. 

### Example:

    message = socket.recv()


## CREATE Response

The response for a successful CREATE request will be the message **“Successfully added shift to DB”**. If any errors are encountered, the message will read **“ERROR: SQL ERROR.”** For more detailed information, refer to the console.

### Example Response:
    “Successfully added shift to DB”

## FETCH Response

The response for a successful FETCH request will be a JSON string with two keys: “data” and “scroll”. The **“data”** key contains an array of arrays, where each inner array represents a row from the database and each element is a column in the same order as specified in the schema. The **“scroll”** key is a string reading True or False , that indicates whether there are 8 or more items retrieved from the query. If any errors occurred, the response will be the error message **“ERROR: SQL ERROR”**. For more detailed information, refer to the console.


### Example Response:
    {
	"data": [
	[1, "person1", "lastName 1", "shift 1, shift 2", "myDays 1", "myPositions 1", 	"myComments 1", "2025-02-28 01:22:39”], 
	[2, "Jane", "Doe", "shift 2, shift 4, shift 5", "someDays", "somePositions", 	"someComments", "2025-02-28 01:22:39”] 
	], 
	"scroll": “False"
	}



## UML diagram
![UML Diagram](https://github.com/selfsta/Microservice-David/blob/main/UML_diagram.png?raw=true)
