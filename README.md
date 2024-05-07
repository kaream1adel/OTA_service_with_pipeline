# OTA_service_with_pipeline

#SCENARIO:

a.	OTA-client.py app checks every 10 seconds for a new push to kaream/app repo for a new version of app image.
 
b.	APP GitHub repo updated by developers which trigger Jenkins APP pipeline build job by GitHub webhook and the pipeline pushed the new image to docker hub.

c.	Docker hub webhook triggered when a new image pushed to kaream10/app repo and send request to OTA-server container running on an ec2 instance to acknowledge the server that there is update.
 
d.	OTA-server updates its state.
 
e.	OTA-client next request will find that there is a new image version that can be used and can update the app container running on the client. 
 
f.	OTA-client run bash script to pull the new image and run the new container. 
 
