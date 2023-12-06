# example of state machine

import time, requests

class TrafficLight:
    def __init__(self):
        self.state="red"

    def changeState(self, event):
        if self.state == "red" and event == "change":
            self.state = "green"
            print("Traffic light changed to green")
            print(requests.get("http://192.168.1.101:5000/green/").text)
        elif self.state == "green" and event == "change":
            self.state = "yellow"
            print("Traffic light changed to yellow")
            print(requests.get("http://192.168.1.101:5000/yellow/").text)
        elif self.state == "yellow" and event == "change":
            self.state = "red"
            print("Traffic light changed to red")
            print(requests.get("http://192.168.1.101:5000/red/").text)
        else:
            print("invalid event   " + event + "   for state   " + self.state)
                  
    def __str__(self):
        return self.state.__str__()
    
if __name__ == '__main__':
    tl = TrafficLight()
    print(tl)
    
    tl.changeState("change")
    print(tl)
    time.sleep(1)
    tl.changeState("change")
    print(tl)
    time.sleep(1)
    tl.changeState("change")
    print(tl)    