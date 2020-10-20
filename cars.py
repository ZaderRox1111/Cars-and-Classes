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


main()
turtle.exitonclick()
