import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            for _ in range(quantity):
                self.contents.append(color)

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        balls_drawn = random.sample(self.contents, num_balls)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**expected_balls)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        success = True
        for color, quantity in expected_balls.items():
            if drawn_balls.count(color) < quantity:
                success = False
                break
        if success:
            num_success += 1
    return num_success / num_experiments

# Test cases

# Test case for creating Hat object with correct contents
hat = Hat(red=3, blue=2)
assert len(hat.contents) == 5
assert hat.contents.count('red') == 3
assert hat.contents.count('blue') == 2

# Test case for draw method reducing number of items in contents
hat = Hat(red=3, blue=2)
initial_length = len(hat.contents)
hat.draw(3)
assert len(hat.contents) == initial_length - 3

# Test case for draw method when number of balls to extract is bigger than the number of balls in the hat
hat = Hat(red=1)
drawn_balls = hat.draw(2)
assert len(drawn_balls) == 1  # Draw all available balls

# Test case for experiment method returning a different probability
hat = Hat(red=3, blue=2)
probability1 = experiment(hat, expected_balls={"red": 2, "blue": 1}, num_balls_drawn=3, num_experiments=1000)
probability2 = experiment(hat, expected_balls={"red": 1, "blue": 1}, num_balls_drawn=2, num_experiments=1000)
assert probability1 != probability2
