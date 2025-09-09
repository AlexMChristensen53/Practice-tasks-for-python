import time

class LED:
    def __init__(self, name ="LED"):
        self.name = name
    def turnon(self):
        print(f"{self.name} BLINK")
    def turnoff(self):
        print(f"{self.name} SLUK")
    def wait(self, seconds):
        time.sleep(seconds)

Rød = LED("Rød")
Rød.turnon()
Rød.wait(5)
Rød.turnoff()
Rød.wait(2)
Grøn = LED("Grøn")
Grøn.turnon()
Rød.wait(5)
Grøn.turnoff()