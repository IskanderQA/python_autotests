import os
from dotenv import load_dotenv

load_dotenv()

HTTP_SCHEMA = os.getenv('HTTP_SCHEMA')
POKEMONS_HOST = os.getenv('POKEMONS_HOST')
POKEMONS_PORT = os.getenv('POKEMONS_PORT')
POKEMONS_URL = f'{HTTP_SCHEMA}{POKEMONS_HOST}:{POKEMONS_PORT}'

# Trainer data
token=os.getenv('TOKEN')
trainer_id=os.getenv('TRAINER_ID')

# User data
email=os.getenv('EMAIL')
password=os.getenv('PASSWORD')

# Card data
card_number=os.getenv('CARD_NUMBER')
card_csv=os.getenv('CARD_CSV')
card_actual=os.getenv('CARD_ACTUAL')
num=os.getenv('NUM')
