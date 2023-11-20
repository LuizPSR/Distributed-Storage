# Distributed-Storage
A distributed storage system using gRPC implemented in python.

The system stores key-value pairs of type (int, string). Two distinct types of servers are used to achieve this goal: Servers that store the pairs and clients capable of inserting, consulting, activating (more of that on part II) and terminating the servers.

### Part I
Implement a pair-server that receive as parameter the port used and a optional parameter that connect it to a central server that will be implemented in part II. The server must export the following procedures using the gRPC protocol:
- Insertion: receive as parameter an integer key and the associated string value, and returns 0 if inserted successfully and -1 if this key is already in use.
- Consult: receive an integer key as parameter and return the associated value or None if key has not be inserted yet.
- Activation: receive as a parameter a string that identifies a service (address and port). No implementation at this phase.
- Termination: terminates the server, without parameters.

The client that communicates with the server must receive its address and port as parameters and read from stdin the operation to be performe, both from termina and files. The format of the commands are:
- Insertion: I,key,string of description
- Consult: C,key
- Activation: A,string that identifies service
- Termination: T
