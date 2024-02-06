# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:39:32 2024

@author: Sami
"""

import pytest
import requests
import json

POKEMON_TYPE_API = "https://pokeapi.co/api/v2/type"

def read_api(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            response.raise_for_status()
        else:
            return response
    except requests.exceptions.RequestException as e:
        print("ERROR occurred while making the api request: {}".format(e))
        return None
    
def find_id_of_fire_type_pokemons():
    pokemon_types_response = read_api(POKEMON_TYPE_API)
    if pokemon_types_response:
        try:
            pokemon_types = pokemon_types_response.json()
        except json.JSONDecodeError as e:
            print("ERROR in decoding json: {}".format(e))
            return None
        fire_url = None
        for result in pokemon_types.get('results', []):
            if result.get('name') == 'fire':
                fire_url = result.get('url')
                break
        if fire_url:
            return fire_url.split('/')[-2]
        else:
            print("ERROR: pokemon type fire is not found!")
            return None
            

def get_fire_pokemons():
    fire_id = find_id_of_fire_type_pokemons()
    if fire_id:
        fire_pokemons_api = POKEMON_TYPE_API + '/' + fire_id
        response = read_api(fire_pokemons_api)
        try:
            fire_pokemons = response.json().get('pokemon')
        except json.JSONDecodeError as e:
            print("ERROR in decoding json: {}".format(e))
            return None    
        return fire_pokemons

def find_heaviest_pokemon(pokemon_weights):
    max_weight = 0
    for name in pokemon_weights.keys():
        if pokemon_weights[name] > max_weight:
            max_weight = pokemon_weights[name]
            max_pokemon = name
    return max_pokemon, max_weight


@pytest.fixture(scope="class")
def read_pokemon_type_api():
    url = POKEMON_TYPE_API
    response = read_api(url=url)
    return response


@pytest.fixture(scope="class")
def get_fire_pokemon_names():
    fire_pokemons = get_fire_pokemons()
    if fire_pokemons:
        fire_pokemon_names = [pokemon['pokemon']['name'] for pokemon in fire_pokemons]
        return fire_pokemon_names
    else:
        print("ERROR: no fire pokemons found!")
        return None


@pytest.fixture(scope="class")
def get_five_heaviest_fire_pokemons():
    pokemon_weights = {}
    fire_pokemons = get_fire_pokemons()
    for pokemon in fire_pokemons:
        pokemon_name = pokemon['pokemon']['name']
        pokemon_url = pokemon['pokemon']['url']
        pokemon_api_response = read_api(pokemon_url)
        try:
            pokemon_weight = pokemon_api_response.json()['weight']
        except json.JSONDecodeError as e:
            print("ERROR in decoding json: {}".format(e))
            return None
        pokemon_weights[pokemon_name] = pokemon_weight
    if len(pokemon_weights) < 5:
        print('ERROR: there are less than 5 fire pokemons!')
        return None
    heaviest_pokemons = {}
    for i in range(5):
        max_pokemon, max_weight = find_heaviest_pokemon(pokemon_weights)
        heaviest_pokemons[max_pokemon] = max_weight
        del pokemon_weights[max_pokemon]
    return heaviest_pokemons

        
        