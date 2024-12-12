from twarc import Twarc2
import tkinter as tk
from tkinter import simpledialog

# Configura tu acceso a la API
client = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAALlB4gAAAAAA6nOG3P2b2CSw0hQOr0txMguuOco%3DMdJ8qbHQ64wdU7p7wvL8KJvcd926cN8rF5EvQKwWwLri0QN8k3")

# Nombre de usuario
username = simpledialog.askstring("Input", "Enter your data:")

# Obtener los tweets
def fetch_tweets(username, limit=50):
    user = client.user_lookup([username])
    user_id = next(user)['data'][0]['id']  # Obtener ID del usuario
    tweets = client.timeline(user_id, max_results=limit)
    return [tweet['text'] for tweet in tweets]

tweets = fetch_tweets(username, limit=50)
for tweet in tweets:
    print(tweet)
