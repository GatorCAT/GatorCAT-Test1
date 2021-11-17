"""Add test cases for the function in the collatz module."""


from collatzcreator import collatz


def test_collatz_input_three():
    """Ensure that input of the number 3 produces the sequence suggested by Stavely on page 92."""
    number = 3
    # create a generator function of all of the outputs
    collatz_output_generator = collatz.compute_collatz_chain(number)
    # materialize a list from the generator function, which
    # will support multiple assertions on the list
    collatz_output_list = list(collatz_output_generator)
    # ensure that there are eight values in the list
    assert len(list(collatz_output_list)) == 8
    # confirm that the contents of the list are correct
    assert list(collatz_output_list) == [3, 10, 5, 16, 8, 4, 2, 1]
