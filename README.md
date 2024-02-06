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
    4)I'd like to clarify the algorithm I chose to go with in finding the 5 heaviest pokemons of fire type:
        A)built a dictionary of pokemon_name : pokemon_weight for all pokemons from fire type
        B)for each step from 1 to 5 (flexible to change!)
           take the heaviest pokemon out of the dictionary and add it to the return value which is going to be a dictionary of 5 items.
        other algorithms I considered:
          2)make a dictionary of weights as key and each value for key will be a list of pokemon names that share that weight
          3)having a fixed list of 5 pokemons which are going to always hold the heaviest and modify it on the fly as I iterate the pokemons apis
        these are both good algorithms when the amount of pokemon is very large, but in our case what really takes time is the get api requests and NOT finding the heaviest pokemons afterwards, so I chose to go with the simple algorithm and ofcourse making sure not         to make repeated unneccessary api requests.

# Author
Sami Shekh

# Help
for help you can contact me directly on my email account: samisnow97@gmail.com
