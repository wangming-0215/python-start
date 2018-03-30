from random import choice
import matplotlib.pyplot as plt


class RandomWalk():

    def __init__(self, num_point=5000):
        self.num_point = num_point
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_point:
            directions = [1, -1]
            distances = list(range(8))

            x_direction = choice(directions)
            x_distance = choice(distances)
            x_step = x_direction * x_distance

            y_direction = choice(directions)
            y_distance = choice(distances)
            y_step = y_direction * y_distance

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = RandomWalk()
rw.fill_walk()

plt.plot(rw.x_values, rw.y_values, linewidth=1)

plt.show()
