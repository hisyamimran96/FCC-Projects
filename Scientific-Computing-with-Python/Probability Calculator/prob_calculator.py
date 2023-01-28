import copy
import random

class Hat:
  def __init__(self,**balls):
    self.contents = []
    self.balls = {**balls}
    for color,amount in balls.items():
      self.contents += [color] * amount

  def draw(self,amount:int):
    if amount <= len(self.contents):
      drawn_balls = random.sample(self.contents,k = amount) 
      #lesson: use random.sample() to draw one item without putting the item back, use random.choices() to draw item and putting the item back into the sample.
      for ball in drawn_balls:
        self.contents.remove(ball)
      return drawn_balls
    else:
      return self.contents

  def __str__(self):
    return "{}".format(self.contents)
  
def experiment(hat, expected_balls:dict, num_balls_drawn:int, num_experiments:int):
  success = 0
  for experiment in range(num_experiments):
    experiment_hat = copy.deepcopy(hat)
    experiment_drawn_balls = experiment_hat.draw(num_balls_drawn)
    experiment_drawn_balls = {ball: experiment_drawn_balls.count(ball) for ball in experiment_drawn_balls}

    #testing conditions to verify if what drawn is more or equal than expected. 
    condition = []
    for ball, count in expected_balls.items():
      if count <= experiment_drawn_balls.get(ball,0):
        condition.append(True)
      else:
        condition.append(False)
    if all(condition):
      success += 1
  
  return success / num_experiments
  