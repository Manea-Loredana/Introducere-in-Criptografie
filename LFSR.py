def xor(state, inputs, length, invert):
    """Computes XOR digital logic

    Parameters:

        :param str state  : Current state of the register
        :param list inputs: Position to tap inputs from register
    Returns:

        :return output: Output of the XOR gate digital logic
        :rtype int :
    """

    # Obtain bits to feed into Xor gate given index value
    input_a = int(state[inputs[0]])
    input_b = int(state[inputs[1]])

    result = bool((input_a & ~input_b) | (~input_a & input_b))

    # Checks if an XNOR is needed
    if invert is True: result = not result

    # Shift result of xor to MSB
    return result << length


if __name__ == "__main__":

    current_state = "001"

    # Position to tap for Xor gate
    index_inputs = [0, 2]
    max_clock = 100
    invert = False

    for clock in range(0, max_clock + 1):

        print(clock, current_state)

        xor_output = xor(current_state, index_inputs, len(current_state) - 1,
                         invert)

        shift = int(current_state, 2) >> 1

        # Re-assign the current state and pad with zeroes
        current_state = format(xor_output | shift, '0{}b'.format(len(
            current_state)))
