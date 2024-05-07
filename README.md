# OTA_service_with_pipeline

# SCENARIO:

a.	OTA-client.py app checks every 10 seconds for a new push to kaream/app repo for a new version of app image.

![image](https://github.com/kaream1adel/OTA_service_with_pipeline/assets/96724633/35daa58b-aecc-437c-841f-d047ce245fce)

 
b.	APP GitHub repo updated by developers which trigger Jenkins APP pipeline build job by GitHub webhook and the pipeline pushed the new image to docker hub.

c.	Docker hub webhook triggered when a new image pushed to kaream10/app repo and send request to OTA-server container running on an ec2 instance to acknowledge the server that there is update.

![image](https://github.com/kaream1adel/OTA_service_with_pipeline/assets/96724633/dd66ac57-148c-4017-8720-95c531779729)

 
d.	OTA-server updates its state.

![image](https://github.com/kaream1adel/OTA_service_with_pipeline/assets/96724633/033ba7fb-101f-4ab0-8098-30cab3d1b01a)

 
e.	OTA-client next request will find that there is a new image version that can be used and can update the app container running on the client. 

![image](https://github.com/kaream1adel/OTA_service_with_pipeline/assets/96724633/6ef1c4bb-e912-4768-9fb2-6ea1a57a8c9c)

 
f.	OTA-client run bash script to pull the new image and run the new container. 

![image](https://github.com/kaream1adel/OTA_service_with_pipeline/assets/96724633/14ccc4c4-2a97-4cbb-9b2b-31a94d45ad36)

 
