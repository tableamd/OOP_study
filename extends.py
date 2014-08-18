from turtle import *


#Turtleクラスを継承したextendsTurtleクラス
class extendsTurtle(Turtle):
    def __init__(self, scale):
        super(extendsTurtle, self).__init__()
        self.shapesize(scale[0],scale[1],scale[2])

    def moveFast(self, move):
        from time import sleep
        sleep(1)
        self.forward(move*10)

    def moveSlow(self,move):
        from time import sleep
        for val in range(1,move):
            self.forward(1)
            sleep(0.05)

    def sayHello(self):
        from time import sleep
        sleep(1)
        self.write("hello!",font=("Arial", 30, "normal"))


#extendsTurtleクラスを継承したtalkerクラス
class talker(extendsTurtle):
    def __init__(self, scale):
        super(talker, self).__init__(scale)

    def talking(self,sentence):
        self.write(sentence,font=("Arial", 40, "normal"))

#lambda hoge:hoge.fuga


#exTurtle = extendsTurtle((2,2,4))
#exTurtle.moveFast(10)
def demo1(exTurtle):
    exTurtle.moveSlow(100)
    exTurtle.left(90)
    exTurtle.forward(50)
    exTurtle.sayHello()

#exTurtle2 = extendsTurtle((4,4,4))
def demo2(exTurtle):
    exTurtle.right(90)
    exTurtle.moveFast(20)
    exTurtle.sayHello()
