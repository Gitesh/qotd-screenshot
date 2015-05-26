#convert this to a FUNCTION and include in the main py

from twython import Twython

APP_KEY='02pbNPpOuxttsJgKjpB3zpwt6'
APP_SECRET='JkU1qLP9HJYmABuzgvyUw13nTUXUNTH7htQx6JBCbUjRNaT81e'
OAUTH_TOKEN='3190228199-Q5CBx59UPS78uO7gtD6wNQF7mFxbxSKxpCI6RwI'
OAUTH_TOKEN_SECRET='JYmj1GuvNSwZZTa6xoJ8cLjDWlbJS0Tm11A7A3LUrAWiH'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

text = "This is a quote"
photo = open('output.gif', 'rb')

twitter.update_status_with_media(status=text, media=photo)
