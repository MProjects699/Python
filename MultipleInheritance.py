class Mario:

    def move(self):
        print("I am moving")

class shroom:

    def sshroom(self):
        print("now i am big")
        
        class BigMario(Mario, shroom):
            pass

        bm = BigMario()
        bm.move()
        bm.sshroom()