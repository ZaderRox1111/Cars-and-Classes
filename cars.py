import turtle

def main():
    car1 = Car('ewad', 10, 'green')
    

    done = False
    while done == False:
        inp = input()
        car1.move(5, inp)
        if car1.move(5, inp) == False:
            done = True
        
    turtle.exitonclick()

class Car:
    
    def __init__(self, inputs, turn_amount, color):
        self.inputs = inputs
        self.turn_amount = turn_amount
        self.color = color
        self.turt = turtle.Turtle()
        self.direction = 0
        self.turt.color(self.color)

    def move(self, speed, inp):
#        done = False
#        while done == False:
#            inp = input()

        for move in inp:

            if move == self.inputs[0]:
                return False

            if move == self.inputs[1]:
                self.turt.fd(speed)

            if move == self.inputs[2]:
                self.direction += self.turn_amount
                if self.direction >= 360:
                    self.direction = 0
                self.turt.seth(self.direction)

            if move == self.inputs[3]:
                self.direction -= self.turn_amount
                if self.direction <= 0:
                    self.direction = 360
                self.turt.seth(self.direction)


main()
