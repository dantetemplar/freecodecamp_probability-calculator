import copy
import random
from collections import Counter


# Consider using the modules imported above.

class Hat:
    def __init__(self, mutable: bool = True, **kwargs):
        self._hat_ = Counter(kwargs)
        self._contents_ = None
        self.mutable = mutable

    @property
    def contents(self):
        if self.mutable:
            return list(self._hat_.elements())
        else:
            if self._contents_ is None:
                self._contents_ = list(self._hat_.elements())
            return self._contents_

    def draw(self, amount: int):
        amount = min(amount, sum(self._hat_.values()))
        choiced = random.sample(self.contents, k=amount)
        if self.mutable:
            self._hat_ -= Counter(choiced)
        return choiced


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    def expectation(actual_balls):
        counter = Counter(actual_balls)
        for color, expected_amount in expected_balls.items():
            if counter[color] < expected_amount:
                return False
        return True

    positives = 0
    for i in range(num_experiments):
        exp_hat = copy.deepcopy(hat)
        positives += expectation(exp_hat.draw(num_balls_drawn))

    return positives / num_experiments


if __name__ == '__main__':
    hat = Hat(blue=3, red=2, green=6)
    probability = experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4,
                             num_experiments=4000)
    actual = probability
    print(actual)
