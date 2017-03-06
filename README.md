

The Smart Classroom Complex is a live system that needs to be monitored closely and effectively to ensure user comfort and so that any issue can be brought into notice the instant it occurs. 
This goes towards the goal of having no downtime.

Various aspects need to be monitored:

First Level: 
1) All Raspberry Pi's are up 
2) Production Server running the server scripts and proxy forwarder is up 
3) All Cameras are up

Second Level:
1) All RPI's are running the room actuator and temp collect scripts 
2) Production Server is running Proxy Forwarder 1 and 2. 
3) Server script that performs image processing is up.

Third Level: 
1) Logging Mongo Insert Error in the RPI scripts. 
2) Logging the messages RPI sends to the Server Side 
3) Logging the messages Server Side sends to the RPI 
4) Logging OpenCV errors (invalid frames) 
5) Logging results of motion and face detection algorithm at low granularity so that complaints can be looked into in great detail.

In this project, the first and second level will be implemented.