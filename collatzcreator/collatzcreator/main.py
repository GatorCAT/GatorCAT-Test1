"""Define the command-line interface for the collatzcreator program."""

import pathlib
from typing import List

from rich.console import Console

from matplotlib import pyplot  # type: ignore

import typer

from collatzcreator import collatz
from collatzcreator import summarize

cli = typer.Typer()

console = Console()


@cli.command()
def main(
    number: List[int] = typer.Option([]),
    minimum: int = typer.Option(1),
    maximum: int = typer.Option(10),
    graph_name: str = typer.Option("collatz.pdf"),
    display: bool = typer.Option(False),
):
    """Run an experiment with the Collatz function to see if it terminates for each given number."""
    # create a list of the input numbers that has
    # a name that is more convenient to remember
    collatz_inputs = list(number)
    # if no list of numbers was specified through the (potentially repeated)
    # use of the "--number" command-line argument, then create a list of
    # values using the range for a specified minimum and maximum value
    if collatz_inputs == []:
        collatz_inputs = list(range(minimum, maximum + 1))
    # create an empty list that can store the length of the Collatz chain
    collatz_output_list_length = []
    # display the debugging output for the program's command-line arguments
    console.print(
        ":detective:  Let's investigate the behavior of the Collatz sequence!"
    )
    # execute the collatz function for each of the numbers in the list
    for collatz_input in collatz_inputs:
        # call the function named compute_collatz_chain and save its output
        # materialize the list from the returned generator function
        collatz_output_generator = collatz.compute_collatz_chain(collatz_input)
        collatz_output_list = list(collatz_output_generator)
        collatz_output_list_length.append(len(collatz_output_list))
    # display the details about the numbers that were input to the function
    console.print()
    console.print(f"  The first input to try will be {collatz_inputs[0]}")
    console.print(
        f"  The last input to try will be {collatz_inputs[len(collatz_inputs) - 1]}"
    )
    console.print()
    if display:
        console.print("The inputs to the Collatz function:")
        console.print()
        console.print(str(collatz_inputs))
        # display the details about the length of the output chain
        console.print()
        console.print(
            ":sparkles: What is the length of the Collatz chain before the function produces the value of 1?"
        )
        console.print("")
        console.print(":straight_ruler: The length of the resulting Collatz chain:")
        console.print()
        console.print(str(collatz_output_list_length))
        console.print()
    # compute the minimum and maximum length of the Collatz chain
    minimum_chain_length = min(collatz_output_list)
    maximum_chain_length = max(collatz_output_list)
    # compute the mean, median, and standard deviation of the length of the Collatz chain
    mean_chain_length = summarize.compute_mean(collatz_output_list)
    median_chain_length  = summarize.compute_median(collatz_output_list)
    stdev_chain_length = summarize.compute_standard_deviation(collatz_output_list)
    # display the summary information about the Collatz chains
    console.print(
        ":sparkles: What is the summary information about the length of the Collatz chain?"
    )
    console.print()
    console.print(f"  The minimum length of a Collatz chain is: {minimum_chain_length}")
    console.print(f"  The maximum length of a Collatz chain is: {maximum_chain_length}")
    console.print(
        f"  The mean of the length of a Collatz chain is: {mean_chain_length:.2f}"
    )
    console.print(
        f"  The median of the length of a Collatz chain is: {median_chain_length:.2f}"
    )
    console.print(
        f"  The standard deviation of the length of a Collatz chain is: {stdev_chain_length:.2f}"
    )
    console.print()
    # create a visualization in the form of a scatter plot
    # Reference:
    # https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
    pyplot.style.use("seaborn-whitegrid")
    pyplot.plot(collatz_inputs, collatz_output_list_length, "o", color="black")
    pyplot.xlabel("Integer Input to the Collatz Function")
    pyplot.ylabel("Length of the Output Collatz Chain")
    # save the scatterplot in a PDF that a person can easily view
    pathlib.Path("graphs").mkdir(parents=True, exist_ok=True)
    pyplot.savefig("graphs/" + graph_name)
    # display a question about the relationship between the input number and the length of the chain
    console.print(
        ":person_shrugging: Can you find a pattern between the input number and the length of the Collatz chain?"
    )
    console.print("")
    console.print(
        f":package: Check the file called 'graphs/{graph_name}' to see a graph that visualizes the results!"
    )
    console.print("")
