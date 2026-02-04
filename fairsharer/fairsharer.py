import numpy as np


def fair_sharer(values, num_iterations, share=0.1):
    values = np.array(values, dtype=float)

    for _ in range(num_iterations):
        max_index = int(np.argmax(values))
        max_value = values[max_index]

        share_amount = max_value * share
        left = (max_index - 1) % len(values)
        right = (max_index + 1) % len(values)

        # apply changes directly
        values[max_index] -= 2 * share_amount
        values[left] += share_amount
        values[right] += share_amount

    return [int(round(x)) for x in values.tolist()]


if __name__ == "__main__":
    print(fair_sharer([0, 1000, 800, 0], 1))
    print(fair_sharer([0, 1000, 800, 0], 2))
