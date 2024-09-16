class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        Horse.x_distance += dx

class Eagle:
    sound = 'I train, eat, sleep, and repeat'
    y_distance = 0

    def fly(self, dy):
        Eagle.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().x_distance
        super().x_distance
        super().sound

    def move(self, dx, dy):
        super().run(dy)
        super().fly(dx)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
