import random
import time

# This is a simulation of the client-server interaction


class Client:
    def __init__(self, state, client_id):
        self.state = state
        self.client_id = client_id

    def send_message(self, server):
        print("Client", self.client_id, "sending message with current state:", self.state)
        start = time.time()
        server.send_reply()
        end = time.time()
        response_time = end - start  # timing the server reply function

        if self.state == 0:
            step = 1  # goes to state 1 only
        elif self.state == 5:
            step = -1  # goes to state 4 only
        elif response_time <= server.response_time:
            # before time out -> has the option to move forward or backward
            inp = input("Do you want to move forward (F) or backward (B)? ")
            if inp.lower() == "f":
                step = 1
            elif inp.lower() == "b":
                step = -1
            else:
                print("The option you entered is invalid")
                exit()
        else:
            # after time out, must move backward
            step = -1

        new_state = self.state + step

        print("Server replied, current state is:", new_state, "\n")
        self.state = new_state


class Server:
    def __init__(self, num_clients, response_time):
        self.num_clients = num_clients
        self.response_time = response_time

    @staticmethod
    def send_reply():
        time.sleep(random.randint(0, 5))  # simulates the delay in server response from 0 to 5 seconds - random
        return "Accept message"


def state_machine_use(num_clients, response_time):
    server = Server(num_clients, response_time)
    clients = [Client(state, client_id) for _ in range(num_clients)
               for state in range(6) for client_id in range(num_clients)]  # list of client objects
    # clients created with states from 0->5 to generate all possible combinations

    for client in clients:
        client.send_message(server)


def main(num_clients, response_time):
    for i in range(num_clients + 1):
        print("Test Case with number of clients:", i, " and response time:", response_time)
        state_machine_use(i, response_time)
        print("\n")


main(2, 3)  # server needs to respond within response_time 3
