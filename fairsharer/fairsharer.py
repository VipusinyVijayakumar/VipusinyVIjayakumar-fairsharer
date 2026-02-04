import numpy as np

def fair_sharer(values, num_iterations, share=0.1):
    values = np.array(values, dtype=float)

    for _ in range(num_iterations):
        new_values = values.copy()

        #the highest value and its index are being searched
        max_index = np.argmax(values)
        max_value = values[max_index]

        #amount that will be shared 
        share_amount = max_value * share

        #neighbors of left and right
        left = (max_index -1) % len(values)
        right = (max_index + 1) % len(values)

        #update values
        new_values[max_index] -= 2 * share_amount 
        new_values[left] += share_amount
        new_values[right] += share_amount

        #new values for tge next time
        values = new_values
    return new_values


if __name__ == "__main__":
    result = fair_sharer([0, 1000, 800, 0], 1)
    print(result)
    # output: [100. 800. 900.   0.]

    result = fair_sharer([0, 1000, 800, 0], 2)
    print(result)
    #output: [100. 890. 720.  90.]
    