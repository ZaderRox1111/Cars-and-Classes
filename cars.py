import turtle

def main():
    harry = turtle.Turtle()

    harry_dir = 0
    done = False
    while done == False:
        inp = input("wad: ")
        
        for move in inp:
            if move == 'e':
                done = True

            if move == 'w':
                harry.fd(5)

            if move == 'a':
                harry_dir += 5
                if harry_dir == 360:
                    harry_dir = 0
                harry.seth(harry_dir)

            if move == 'd':
                harry_dir -= 5
                if harry_dir == 0:
                    harry_dir = 360
                harry.seth(harry_dir)

class Car:
    
    def __init__(self, inputs, turn_amount):
        self.inputs = inputs
        self.turn_amount = turn_amount

    def move(self, speed):
        turt = turtle.Turtle()
        
        direction = 0
        done = False
        while done == False:
            inp = input()

            for move in inp:

                if move == self.inputs[0]:
                    done == True

                if move == self.inputs[1]:
                    turt.fd(speed)

                if move == self.inputs[2]:
                    direction += self.turn_amount
                    if direction >= 360:
                        direction = 0
                    turt.seth(direction)

                if move == self.inputs[3]:
                    direction -= self.turn_amount
                    if direction <= 0:
                        direction = 360
                    turt.seth(direction)


car1 = Car("ewad", 10)
car1.move(5)
turtle.exitonclick()
