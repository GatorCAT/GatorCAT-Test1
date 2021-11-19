# Collatz Chains

## Wesley Long

## Program Input and Output

### What is the output from running the following command?

`poetry run collatzcreator --minimum 1 --maximum 10 --display`

```
🕵  Let's investigate the behavior of the Collatz sequence!

  The first input to try will be 1
  The last input to try will be 10

The inputs to the Collatz function:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

✨ What is the length of the Collatz chain before the function produces the value of 1?

📏 The length of the resulting Collatz chain:

[1, 2, 8, 3, 6, 9, 17, 4, 20, 7]

✨ What is the summary information about the length of the Collatz chain?

  The minimum length of a Collatz chain is: 1
  The maximum length of a Collatz chain is: 20
  The mean of the length of a Collatz chain is: 7.70
  The median of the length of a Collatz chain is: 6.50
  The standard deviation of the length of a Collatz chain is: 5.97

🤷 Can you find a pattern between the input number and the length of the Collatz chain?

📦 Check the file called 'graphs/collatz.pdf' to see a graph that visualizes the results!
```

### What is the output from running the following command?

`poetry run collatzcreator --minimum 1 --maximum 100`

```
🕵  Let's investigate the behavior of the Collatz sequence!

  The first input to try will be 1
  The last input to try will be 10

The inputs to the Collatz function:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

✨ What is the length of the Collatz chain before the function produces the value of 1?

📏 The length of the resulting Collatz chain:

[1, 2, 8, 3, 6, 9, 17, 4, 20, 7]

✨ What is the summary information about the length of the Collatz chain?

  The minimum length of a Collatz chain is: 1
  The maximum length of a Collatz chain is: 20
  The mean of the length of a Collatz chain is: 7.70
  The median of the length of a Collatz chain is: 6.50
  The standard deviation of the length of a Collatz chain is: 5.97

🤷 Can you find a pattern between the input number and the length of the Collatz chain?

📦 Check the file called 'graphs/collatz.pdf' to see a graph that visualizes the results!
```

## Source Code

### Describe in detail how the following source code works

#### Explain the source code statement `if number % 2 == 0:`


This source code statement is meant to determine whether or not `number` is even.  It performs this operation using modulus arithmetic.  This modulus attempts to divide the given input by 2, and if the remainder is `0` then the input number is even.

## Explain `number = number // 2`

This code segment is performing regular division, but then rounding down to the nearest integer.  In class, this operator (`//`) was described as using integer division.  It can be called this, as no matter what this operator is used on, if it outputs a valid value, that value is in turn converted to an integer.  If we are given `15 / 2` we would normally write the output as `7.5`.  But if the operation is written as `15 // 2` instead, then the output ends up being `7`.

## Explain the meaning and purpose of the following two lines of source code

```
numbers_internal = copy.deepcopy(numbers)
numbers_internal.sort()
```

This code segment is performing a copy of our given array of inputs.  The copy created in this way is a deep copy, meaning that the copy is initialized with the actual values, opposed to references to the given values.  Meaning that if we had made a shallow copy, then we may have ended up altering and ruining further analysis of out data.  In this instance, we create a copy to sort and analyze, instead of manipulating the original array.

## Use one paragraph to explain the meaning of the following test case

```
def test_collatz_input_three():
    """Ensure that input of the number 3 produces the sequence suggested by Stavely on page 92."""
    number = 3
    # create a generator function of all of the outputs
    collatz_output_generator = collatz.Collatz(number)
    # materialize a list from the generator function, which
    # will support multiple assertions on the list
    collatz_output_list = list(collatz_output_generator)
    # ensure that there are eight values in the list
    assert len(list(collatz_output_list)) == 8
    # confirm that the contents of the list are correct
    assert list(collatz_output_list) == [3, 10, 5, 16, 8, 4, 2, 1]
```

This test case simulates what should be happening exactly for the given input, 3.  The operations performed within this test case are the same as the ones being preformed within the `main.py` file.  As this is the same code, just on a much smaller scale and without any print statements, outside the ones that are printed when the test suite is run.  This test case runs through exactly how the program would get to it's output at this point, and then that output is compared to the expected output that we had already run through on our own.  Either by hand, or through other methods.

## Professional Development

### What was the greatest technical challenge that you faced and how did you overcome it?

I did not feel that I encountered any challenges during the implementation of this lab.  I mainly found some issue with initially coming up with a solution to solving the problems asked of me during this lab, but during some thinking and planning I was able to reach the correct implementations for my functions in order to complete the goals and requirements set for this project.  The only other issues I had during this lab was using python packages that I have no previous experience with.  That package being the `copy` package that as used within the `summarize.py` module.  Allowing us quick and easy implementation of a deep copy of an array to fiddle and alter as we saw fit for analysis purposes.

### How did this assignment leverage Python source code from previous assignments?

This assignment leveraged code that was previously used within the

### What is one topic in the scope of this course that you would like to learn more about? Why?

TODO: Provide a one paragraph response to this question

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.

## At your own option, do you have any other insights to share about this assignment?

TODO: Provide a one paragraph response to this question

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.
