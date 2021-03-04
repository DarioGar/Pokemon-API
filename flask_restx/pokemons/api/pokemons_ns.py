#!/usr/bin/python3

# Copyright 2020 BISITE Research Group
# See LICENSE for details.

import datetime
from flask_restx import Resource
import numpy as np
import pandas as pd
import psycopg2 as psycopg2
from api.v1 import api
from pokemons.core import cache, limiter
from pokemons.api.pokemons_models import pokemon_model
from pokemons.api.pokemons_parsers import pokemon_args_name_arguments, pokemon_body_name_arguments, pokemon_arguments
from pokemons.utils import handle400error, handle404error, handle500error

pokemons_ns = api.namespace('pokemons', description='Provides pokemons information')

pokemons_model = {}
con = psycopg2.connect(database= "pokemon",user="postgres",password="563412",host="127.0.0.1",port="5432")

@pokemons_ns.route('/pokemons')
class pokemonsCollection(Resource):

    @limiter.limit('1000/hour') 
    @api.expect(pokemon_args_name_arguments)
    @api.response(200, 'OK')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @cache.cached(timeout=1, query_string=True)
    @api.marshal_with(pokemon_model, code=200, description='OK', as_list=True)
    def get(self):
        """
        Returns a pokemon if that pokemon exists in the database, else returns all pokemons in the database
        """
        # retrieve and chek arguments
        try:
            args = pokemon_args_name_arguments.parse_args()
            cur = con.cursor()
            if args['pokemon'] is not None:
                query= f"select * from public.pokemon where name = '{args['pokemon']}'"
                cur.execute(query)
                rows = cur.fetchall()
                if len(rows) != 0:
                    pokemon_name = rows[0]
                else:
                    pokemon_name =  None
            else:
                pokemon_name = None
            print (pokemon_name)
        except:
            return handle400error(pokemons_ns, 'The provided arguments are not correct. Please, check the swagger documentation at /v1')

        # check parameters
        if pokemon_name is None and (args['pokemon']) is not None:
            return handle404error(pokemons_ns, 'The provided pokemon was not found.')

        # build result 
        try:
            if pokemon_name is None:
                query= "select * from public.pokemon"
                cur=con.cursor()
                cur.execute(query)
                rows = cur.fetchall()
                pokemons = "Test"
            else:
                pokemons = "pokemon_name"
        except:
            return handle500error(pokemons_ns)
        # if there is not pokemons found, return 404 error
        if not pokemons:
            return handle404error(pokemons_ns, 'No pokemons founds.')

        return pokemons

    @limiter.limit('1000/hour') 
    @api.expect(pokemon_arguments)
    @api.response(200, 'OK')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @cache.cached(timeout=1, query_string=True)
    def post(self):
        """
        Creates a cat
        

        # retrieve and chek arguments
        try:
            args = cat_arguments.parse_args()
            cat_name = args['cat']
            cat_properties = args['properties']
        except:
            return handle400error(pokemons_ns, 'The providen arguments are not correct. Please, check the swagger documentation at /v1')

        # check parameters
        if cat_name in pokemons_model:
            return handle400error(pokemons_ns, 'The providen cat was already created')

        # build cat 
        try:
            pokemons_model[cat_name] = cat_properties
        except:
            return handle500error(pokemons_ns)
        """
        return "post"
    @limiter.limit('1000/hour') 
    @api.expect(pokemon_arguments)
    @api.response(200, 'OK')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @cache.cached(timeout=1, query_string=True)
    def put(self):
        """
        Updates a cat
        

        # retrieve and chek arguments
        try:
            args = cat_arguments.parse_args()
            cat_name = args['cat']
            cat_properties = args['properties']
        except:
            return handle400error(pokemons_ns, 'The providen arguments are not correct. Please, check the swagger documentation at /v1')

        # check parameters
        if cat_name not in pokemons_model:
            return handle404error(pokemons_ns, 'The providen cat was not found')

        # update cat 
        try:
            pokemons_model[cat_name] = cat_properties
        except:
            return handle500error(pokemons_ns)
        """
        return "put"
    @limiter.limit('1000/hour') 
    @api.expect(pokemon_body_name_arguments)
    @api.response(200, 'OK')
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @cache.cached(timeout=1, query_string=True)
    def delete(self):
        """
        Deletes a cat
        

        # retrieve and chek arguments
        try:
            args = cat_body_name_arguments.parse_args()
            cat_name = args['cat']
        except:
            return handle400error(pokemons_ns, 'The providen arguments are not correct. Please, check the swagger documentation at /v1')

        # check parameters
        if cat_name not in pokemons_model:
            return handle404error(pokemons_ns, 'The providen cat was not found')

        # update cat 
        try:
            del pokemons_model[cat_name]
        except:
            return handle500error(pokemons_ns)
        """
        return "delete"