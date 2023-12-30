# Wokwi project: https://wokwi.com/projects/385390330902292481

import json
import paho.mqtt.client as mqtt

CLIENT_ID = "tic-tac-toe-python-players"
TOPIC_MOVES = "tic-tac-toe/players-moves"
GAME_STATE_TOPIC = "tic-tac-toe/game-state"

connected_flag = False
subscribed_flag = False

def on_connect(client, userdata, flags, rc):
    global connected_flag
    if not connected_flag:
        print("Connected with result code {} \n".format(rc))
        connected_flag = True
    client.subscribe(GAME_STATE_TOPIC)

def on_subscribe(client, userdata, mid, granted_qos):
    global subscribed_flag
    if not subscribed_flag:
        print("Successfully subscribed")
        subscribed_flag = True
def on_message(client, userdata, msg):
    if msg.topic == GAME_STATE_TOPIC:
        try:
            print("\n" + msg.payload.decode("utf-8"))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
try:
    client.connect("broker.mqttdashboard.com", port=1883, keepalive=60)
    client.subscribe(GAME_STATE_TOPIC)

    player_name = int(input("Player: "))

    client.loop_start()

    while True:
        row = input("Enter row: ")
        col = input("Enter column: ")
        try:
            row = int(row)
            col = int(col)
            move_message = {"player": player_name, "move": [col, row]}
            client.publish(TOPIC_MOVES, json.dumps(move_message))
        except ValueError:
            print("Invalid input. Please enter valid integers for row and column.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    client.loop_stop()