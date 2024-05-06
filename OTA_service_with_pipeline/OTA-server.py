from flask import Flask, request, jsonify

app = Flask(__name__)
curr_push_timestamp= 0
update=False

@app.route('/webhook-endpoint', methods=['POST'])
def handle_webhook():
    global curr_push_timestamp 
    global update
    payload = request.json

   # print("Received payload:", payload)  # Debug: Print received payload

    new_push_timestamp = payload['push_data']['pushed_at']
    print("New image pushed at timestamp:", new_push_timestamp)  # Debug: Print pushed_at timestamp

    if new_push_timestamp is not None:
        new_push_timestamp = int(new_push_timestamp)  # Convert to integer
        
        if curr_push_timestamp == new_push_timestamp:
            print('no update')
            repository_name = payload['kaream10']['app']
            tag = payload['push_data']['tag']
            print(f"New image pushed to repository: {repository_name}, tag: {tag}")
            # Implement your logic here to handle the new image push event
            # Example: execute_bash_commands(tag)

        if curr_push_timestamp < new_push_timestamp:
            print('there is update')
            update=True
            

    return jsonify({'status': 'success'})

@app.route('/data', methods=['GET'])
def get_data():
    global update
    #print('update at first =',{update})
    if update == True:
        data = {
        'boolean_value': True
                    }
        
    elif update== False:
        data = {'message': 'NO update from the server!'}
    else:
        data = {'message': 'NO change from the server!'}
    update= False



    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
