import time
import random
import threading
import json
from queue import Queue

from freezer import Freezer

FREEZERS = 5
TECHNICIANS = 3

# Thread which simulates the functioning of a freezer
def freezer_functioning(freezer):
    while 1:
        # Get desired temperature and current humidity in order to generate new values based on them
        desired_temperature = freezer.features["temperatureControl"]["desiredProperties"]["temperature"]
        current_humidity = freezer.features["temperatureControl"]["properties"]["humidity"]

        # 40 % chance for freezer to break
        if random.randint(0, 100) < 40:
            freezer.break_freezer()
            # Add the freezer and its event to the queue of the manager
            manager_queue.put(freezer)
            # Notify manager event
            manager_event.set()
            manager_event.clear()
            # Wait for freezer to be fixed
            freezer.event.wait()
        # 60 % chance to send data
        else:
            # Generate new temperature based on desired temperature
            temperature = random.randint(desired_temperature - 3, desired_temperature + 3)
            # Generate humidity based on current himudity
            humidity = random.randint(current_humidity - 5 if current_humidity - 5 > 0 else 0, current_humidity + 5 if current_humidity + 5 < 100 else 100)
            # lower_limit = current_humidity - 5 if current_humidity - 5 > 0 else 0
            # upper_limit = current_humidity + 5 if current_humidity + 5 < 100 else 100
            # humidity = random.randint(lower_limit, upper_limit)
            freezer.update_temperature_control(temperature, humidity)

        # Random sleep between two freezer operations
        time.sleep(random.randint(3, 5))


# Thread for a technician to fix a freezer
def technician_fix_freezer(technician_id, freezer):
    # Fix freezer and notify freezer thread to continue sending data
    freezer.fix_freezer(technician_id)
    freezer.event.set()
    freezer.event.clear()
    available_technicians.put(technician_id)


# Thread for the manager of the technicians
def manager():
    while True:
        # Wait for notification for a broken freezer
        manager_event.wait()
        # While there are freezers for fixing
        while not manager_queue.empty():
            # If there are free technicians, get a freezer from the queue and start a thread fixing it
            if not available_technicians.empty():
                # Daemon threads are joined implicitly before the program ends, not killed
                threading.Thread(target=technician_fix_freezer, args=(available_technicians.get(), manager_queue.get(),), daemon=True).start()

def dashboard():
    while True:
        print("Freezer ID | Temperature | Humidity | State")
        for freezer in freezers:
            with open("./digital-twins/" + freezer.file_name, "r") as output:
                freezer_data = json.load(output)
                id = freezer_data["attributes"]["number"]
                temperature = freezer_data["features"]["temperatureControl"]["properties"]["temperature"]
                humidity = freezer_data["features"]["temperatureControl"]["properties"]["humidity"]
                if freezer_data["features"]["state"]["properties"]["working"]==True:
                    state = "On"
                else:
                    state = "Off"

            print(f"{id} | {temperature} C° | {humidity}% | {state}")

        print("\n")
        time.sleep(1)

if __name__ == "__main__":
    # Generate manager
    manager_thread = threading.Thread(target=manager, daemon=True)
    manager_queue = Queue()
    manager_event = threading.Event()

    # Start manager thread
    manager_thread.start()

    # Generate technicians
    available_technicians = Queue()
    for i in range(TECHNICIANS):
        available_technicians.put(i + 1)

    # Generate freezer numbers
    freezer_numbers = [i + 1 for i in range(FREEZERS)]
    # Generate freezer thing IDs
    freezer_thing_ids = ["freezer-" + str(num) for num in freezer_numbers]
    # Generate freezers
    freezers = [Freezer(freezer_thing_ids[i], freezer_numbers[i]) for i in range(FREEZERS)]

    # Generate freezer threads
    freezer_threads = []
    for freezer in freezers:
        ft = threading.Thread(target=freezer_functioning, args=(freezer,), daemon=True)
        freezer_threads.append(ft)

    # Start freezer threads
    for ft in freezer_threads:
        ft.start()
        time.sleep(.5)

    threading.Thread(target=dashboard, daemon=True).start()

    # Join freezer threads
    for ft in freezer_threads:
        ft.join()


