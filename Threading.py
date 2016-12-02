import threading

class BuckyMessenger(threading.Thread):

    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

            x= BuckyMessenger(name="Sent out messages")
            y= BuckyMessenger(name="Recive message")
            x.start()
            y.start()