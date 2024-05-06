import requests
import time
import subprocess
import docker
# Make an HTTP GET request to the server
server_url= 'http://3.209.49.156:5000/data'

OTA_client= 'first_start'
#commands = "ls;echo '---------------------START UPDATE-----------------------';cd ~/TCU-compose/;docker-compose down;docker-compose up -d"
commands1 = "chmod +x check_OTA_container ;./check_OTA_container 1 "
commands2 = "chmod +x check_OTA_container ;./check_OTA_container"
ContainerRunning= False

# Function to fetch data from the server
def fetch_data_from_server():
    try:
        # Make an HTTP GET request to the server
        response = requests.get(server_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            boolean_value = data.get('boolean_value')  # Extract boolean value from response
            print("Server Response:", data)

            if boolean_value== True:
                print("---------------------FOUND UPDATE---------------------")
                # Start the process with shell=True to interpret the commands using the shell
                process = subprocess.Popen(commands1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Wait for the process to finish and get the output
                stdout, stderr = process.communicate()

                # Check the return code
                if process.returncode == 0:
                    print(stdout)
                    print("Commands executed succesifully")
                    
                else:
                    print("Commands failed with return code:", process.returncode)
                    print("Error output:")
                    print(stderr)
            boolean_value= False

        else:
            print("Failed to fetch data from the server.")
    except Exception as e:
        print("Error occurred while fetching data:", str(e))


def check_container():
    global OTA_client

   # if OTA_client == 'first_start':
    process = subprocess.Popen(commands2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                    # Wait for the process to finish and get the output
    stdout, stderr = process.communicate()

                    # Check the return code
    if process.returncode == 0:
            print(stdout)
            print("Commands executed succesifully: I found APP container")
            OTA_client= 'OK'
                        
    else:
            print("Commands failed with return code:", process.returncode)
            print(stderr)
        
                          



# Periodically fetch data from the server
while True:
    check_container()
    fetch_data_from_server()  # Call the function to fetch data
    
    time.sleep(10)  # Wait for 10 seconds before making the next request