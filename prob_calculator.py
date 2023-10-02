import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key,value in kwargs.items():
      for i in range(value):
        self.contents.append(key)


  def draw(self, number):
    balls_drawn = []
    if number > len(self.contents):
      return self.contents
    for i in range(number):
      random_ball = random.randint(0,(len(self.contents)-1))
      balls_drawn.append(self.contents[random_ball])
      self.contents.remove(self.contents[random_ball])
    return balls_drawn  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for i in range(num_experiments):
    copied_hat = copy.deepcopy(hat)
    copied_expected_balls = copy.deepcopy(expected_balls)
    colors = copied_hat.draw(num_balls_drawn)
    for i in colors:
      if i in copied_expected_balls:
        copied_expected_balls[i] -= 1
    if all(x <= 0 for x in copied_expected_balls.values()):
            m +=1
  return m / num_experiments
