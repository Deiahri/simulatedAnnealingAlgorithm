import math
import random


def func(x_1: float, x_2: float):
    part_1 = pow(pow(x_1, 2) + x_2 - 11, 2)
    part_2 = pow(x_1 + pow(x_2, 2) - 7, 2)
    return part_1 + part_2


max_time = 20
max_temp = 1000

def schedule(t: int):
    if t > max_time:
        return 0.0
    else:
        return max_temp*((max_time-t)/max_time)


def get_range(current, current_val_range, shift_amount):
    if current - shift_amount < current_val_range[0]:
        current_change_range_neg = current - current_val_range[0]
    else:
        current_change_range_neg = shift_amount

    if current + shift_amount > current_val_range[1]:
        current_change_range_pos = current_val_range[1] - current
    else:
        current_change_range_pos = shift_amount
    return -current_change_range_neg, current_change_range_pos


def get_random_in_range(val, val_range):
    total_current_range = -val_range[0] + val_range[1]
    amount = (random.random()*total_current_range)+val_range[0]
    return val + amount


def annealing_prob(diff, temperature):
    prob = 2 - (pow(math.e, -diff/temperature))
    if random.random() < prob:
        return False
    return True


def main():
    neighbor_range = 0.25
    val_range = (0, 5)

    current_x = (random.random()*val_range[1])-val_range[0]
    current_x_2 = (random.random()*val_range[1])-val_range[0]
    for t in range(max_time):
        temperature = schedule(t)
        if temperature == 0:
            return current_x, current_x_2
        else:
            current_x_range = get_range(current_x, val_range, neighbor_range)
            current_x_2_range = get_range(current_x_2, val_range, neighbor_range)

            next_x = get_random_in_range(current_x, current_x_range)
            next_x_2 = get_random_in_range(current_x_2, current_x_2_range)

            current_val = func(current_x, current_x_2)
            next_val = func(next_x, next_x_2)
            if next_val < current_val:
                current_x = next_x
                current_x_2 = next_x_2
                print(f"f({current_x:.2f}, {current_x_2:.2f}) = {current_val:.2f} < f({next_x:.2f}, {next_x_2:.2f}) = "
                      f"{next_val:.2f}. Assign x1, x2 -> n1, n2")
            else:
                if annealing_prob(next_val - current_val, temperature):
                    current_x = next_x
                    current_x_2 = next_x_2
                    print(
                        f"f({current_x:.2f}, {current_x_2:.2f}) = {current_val:.2f} < f({next_x:.2f}, {next_x_2:.2f}) ="
                        f" {next_val:.2f}. But assign x1, x2 -> n1, n2")
                else:
                    print(
                        f"f({current_x:.2f}, {current_x_2:.2f}) = {current_val:.2f} < f({next_x:.2f}, {next_x_2:.2f}) ="
                        f" {next_val:.2f}. Don't Assign x1, x2 -> n1, n2")
    return current_x, current_x_2


vals = main()
print(f"{vals} | {func(vals[0], vals[1])}")