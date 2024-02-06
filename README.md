# pokemon-api-test
This project is for the purpose of an assignment to test capabilites and skills in regard to python, pytest and REST API

Getting Started
# Dependencies
python 3.x
need to install packages to your python:
pip install pytest
pip install requests

# Executing program
need to Run with pytest command

# Important Notes
 - I used scope=class for the fixtures so that they don't have to run multiple times when there is no need.
 - I decided to divide the last test into multiple small ones to avoid having multiple assertions in one test which could lead to assertions not to be executed at all in case of failure.
 - error handling cases I covered:
    1)json parse issues
    2)issue in reading the api response
    3)edge cases like having less than 5 fire pokemons, not finding the fire type for pokemons, in case there are more than 5 pokemons that share the heaviest weight then it will return the first 5 found.

# Author
Sami Shekh

# Help
for help you can contact me directly on my email account: samisnow97@gmail.com
