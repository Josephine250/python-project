class car:
    def move(self):
        print("the car is driving")
class boat:
    def move(self):
        print("the boat is sailing") 
for vechile in (car(),boat()):
    vechile.move()

