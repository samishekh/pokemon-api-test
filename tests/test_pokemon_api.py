# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 01:49:24 2024

@author: Sami
"""

import pytest
from read_pokemon_api import read_pokemon_type_api, get_fire_pokemon_names, get_five_heaviest_fire_pokemons

class TestPokemonAPI:
    def test_type_api_response_is_json(self, read_pokemon_type_api):
        if read_pokemon_type_api:
            content_type = read_pokemon_type_api.headers.get('content-type', '')
            assert 'application/json' in content_type, 'Failed: response is not json type!'
            
    def test_pokemon_types_equal_20(self, read_pokemon_type_api):
        if read_pokemon_type_api:
            pokemon_types = read_pokemon_type_api.json()
            assert pokemon_types.get('count') == 20, 'Failed: pokemon types count is not equal to 20!'
            
    def test_charmander_is_fire_pokemon(self, get_fire_pokemon_names):
        if get_fire_pokemon_names:
            assert 'charmander' in get_fire_pokemon_names, 'Failed: charmander is not found in fire pokemon list!'
            
    def test_bulbasaur_is_not_fire_pokemon(self, get_fire_pokemon_names):
        if get_fire_pokemon_names:
            assert 'bulbasaur' not in get_fire_pokemon_names, 'Failed: bulbasaur is actually a part of fire pokemons!'
            
    def test_charizard_gmax_is_in_five_heaviest_fire_pokemons(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert 'charizard-gmax' in get_five_heaviest_fire_pokemons.keys(), 'Failed: charizard-gmax is not one of five heaviest fire pokemons!'
            
    def test_cinderace_gmax_is_in_five_heaviest_fire_pokemons(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert 'cinderace-gmax' in get_five_heaviest_fire_pokemons.keys(), 'Failed: cinderace-gmax is not one of five heaviest fire pokemons!'
            
    def test_coalossal_gmax_is_in_five_heaviest_fire_pokemons(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert 'coalossal-gmax' in get_five_heaviest_fire_pokemons.keys(), 'Failed: coalossal-gmax is not one of five heaviest fire pokemons!'
            
    def test_centiskorch_gmax_is_in_five_heaviest_fire_pokemons(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert 'centiskorch-gmax' in get_five_heaviest_fire_pokemons.keys(), 'Failed: centiskorch-gmax is not one of five heaviest fire pokemons!'
            
    def test_groudon_primal_is_in_five_heaviest_fire_pokemons(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert 'groudon-primal' in get_five_heaviest_fire_pokemons.keys(), 'Failed: groudon-primal is not one of five heaviest fire pokemons!'
            
    def test_verify_charizard_gmax_weight(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert get_five_heaviest_fire_pokemons.get('charizard-gmax') == 10000, 'Failed: charizard-gmax weight is not equal to 10000'
            
    def test_verify_cinderace_gmax_weight(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert get_five_heaviest_fire_pokemons.get('cinderace-gmax') == 10000, 'Failed: cinderace-gmax weight is not equal to 10000' 
            
    def test_verify_coalossal_gmax_weight(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert get_five_heaviest_fire_pokemons.get('coalossal-gmax') == 10000, 'Failed: coalossal-gmax weight is not equal to 10000'         
            
    def test_verify_centiskorch_gmax_weight(self, get_five_heaviest_fire_pokemons):
        if get_five_heaviest_fire_pokemons:
            assert get_five_heaviest_fire_pokemons.get('centiskorch-gmax') == 10000, 'Failed: centiskorch-gmax weight is not equal to 10000'         
    
    def test_verify_groudon_primal_weight(self, get_five_heaviest_fire_pokemons):
       if get_five_heaviest_fire_pokemons:
           assert get_five_heaviest_fire_pokemons.get('groudon-primal') == 9997, 'Failed: groudon-primal weight is not equal to 9997'