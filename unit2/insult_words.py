import random

body_parts = ['nose', 'mouth', 'face', 'hair', 'eyes']

adjectives = ['smelly', 'boring', 'stupid', 'disgusting', 'poor']

things = ['fly', 'marmot', 'stick', 'monkey', 'rat']

random_body_part = body_parts[random.randint(0, 4)]

random_adjective = adjectives[random.randint(0,4)]

random_thing = things[random.randint(0,4)]

insult_words = f'Your {random_body_part} is like a {random_adjective} {random_thing}!!!'

print(insult_words)
