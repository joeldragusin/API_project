from random import choice
import requests
import pyfiglet
from termcolor import colored

msg = "Dad Jokes 3000"
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color = 'red')
print(ascii_art)


user_input = input("What would you like to search for?: ")

url = "https://icanhazdadjoke.com/search"
res = requests.get(url, 
	headers = {"Accept": "application/json"},
	params = {"term": user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]

if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}. Here's one!")
	print(choice(results)['joke'])
elif num_jokes == 1:
	print(f"I found one joke about {user_input}: ")
	print(results[0]['joke'])
else:
	print(f"Sorry, couldn't find a joke with your term: {user_input}")
