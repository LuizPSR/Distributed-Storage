# Distributed-Storage
A distributed storage system using gRPC implemented in python.

The system stores key-value pairs of type (int, string). Two distinct types of servers are used to achieve this goal: Servers that store the pairs and clients capable of inserting, consulting, activating (more of that on part II) and terminating the servers.
___
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
___
### Part II
Implement a central-server, that is a hub for clients to find the pair server containing the right key. The server must export the following procedures using the gRPC protocol:
- Register: receive as parameter an address and a list of integers, then register the keys as belonging to that address (assumed to be a pair-server).
- Map: receive an integer key as parameter and return the address of the last pair-server to register that key.
- Termination: terminates the server, without parameters.

Now the original pair-server must implement the activation service, by registering its key with the central address (passed as the string identifying the service). This return the number of keys that were registered by the operation. This behavior is only allowed if the pair-server received more than a single argument.

The client that communicates with the central-server must receive its address and port as parameters and read from stdin the operation to be performe, both from termina and files. The format of the commands are:
- Map and Consult: C,key
- Termination: T
___
### Behavior Observations
**Register Overwrites**: when a new service register a key already mapped by the central-server, it becomes the new address of that key. **IT DO NOT CHECK IF THE KEYS MAP TO THE SAME VALUE**, essencially overwriting the value of that key for the clients of the central server.