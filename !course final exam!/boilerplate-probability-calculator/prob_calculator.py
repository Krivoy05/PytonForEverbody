import copy
import random


# Consider using the modules imported above.


class Hat:
    contents = list()

    def __init__(self, **balls):
        self.contents = list()
        self.balls = balls
        for colour, how_many in balls.items():
            for i in range(how_many):
                self.contents.append(colour)

    def draw(self, number_of_balls):
        if number_of_balls >= len(self.contents):
            return self.contents
        else:
            result = list()
            for i in range(number_of_balls):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                result.append(ball)
            return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_local = copy.deepcopy(hat)
    hat_local_balLs_list = hat_local.contents.copy()
    how_many_times_got_expected_balls = 0
    expected_balls_list = list()
    for colour, how_many in expected_balls.items():
        for i in range(how_many):
            expected_balls_list.append(colour)
    for i in range(num_experiments):
        pull_out_balls = hat_local.draw(num_balls_drawn)

        #recznie chek with remoe
        check  = False
        check_list = list()
        for i in range(len(expected_balls_list)):
            for el in pull_out_balls:
                if expected_balls_list[i] == el:
                    check_list.append(True)
                    pull_out_balls.remove(el)
                    break
        if len(check_list) == len(expected_balls_list):
            check = True
        if check:
            how_many_times_got_expected_balls += 1
            check = False
        hat_local.contents = hat_local_balLs_list.copy()
    return how_many_times_got_expected_balls / num_experiments
