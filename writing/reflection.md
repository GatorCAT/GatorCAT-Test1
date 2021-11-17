# Collatz Chains

## Add Your Name Here

## Program Input and Output

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

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

TODO: Use a fenced code block to provide the output for this command.

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

TODO: Use one paragraph to explain the aforementioned source code statement

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

## Explain `number = number // 2`

TODO: Use one paragraph to explain the aforementioned source code statement

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

## Explain the meaning and purpose of the following two lines of source code

```
numbers_internal = copy.deepcopy(numbers)
numbers_internal.sort()
```

TODO: Use one paragraph to explain the aforementioned source code segment

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

TODO: Use one paragraph to explain the aforementioned source code segment

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

## Professional Development

### What was the greatest technical challenge that you faced and how did you overcome it?

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

### How did this assignment leverage Python source code from previous assignments?

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
