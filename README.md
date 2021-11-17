# Collatz Chains

## Assigned: Wednesday, November 17, 2021
## Due: Wednesday, December 1, 2021

After cloning this repository to your computer, please take the following steps:

- Follow the instructions on the Proactive Programmers web site for this project
- Use the `cd` command to change into the directory for this repository.
- Change into the program directory by typing `cd datauniquifier`.
- Install the dependencies for the project by typing `poetry install`
- Run the program with the correct input file by typing:
  - Run the program with few inputs: `poetry run collatzcreator --minimum 1 --maximum 10 --display`
  - Run the program with many inputs: `poetry run collatzcreator --minimum 1 --maximum 1000`
  - Run the program in Project Euler configuration: `poetry run collatzcreator --minimum 1 --maximum 1000000 --display`
  - Please note that the program will not work unless you add the required source code
  - You should also try to run the program with only the `--help` flag
- Confirm that the program is producing the expected output
- Use a `docker run` command for your operating system to run GatorGrader
- Provide all of the required responses in the `writing/reflection.md` file
- Refer to the [Project Euler](https://projecteuler.net/problem=14) site for more details
