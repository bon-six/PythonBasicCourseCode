import random
 
# create the country and capital dictionary
countries_capitals = {}
countries_capitals['Malaysia'] = 'Kuala Lumpur'
countries_capitals['Singapore'] = 'Singapore'
countries_capitals['Thailand'] = 'Bangkok'
countries_capitals['Indonesia'] = 'Jakarta'
countries_capitals['USA'] = 'Washington D.C.'
countries_capitals['Canada'] = 'Ottawa'
countries_capitals['China'] = 'Beijing'
countries_capitals['France'] = 'Paris'
countries_capitals['UK'] = 'London'
countries_capitals['Germany'] = 'Berlin'
countries_capitals['Russia'] = 'Moscow'
countries_capitals['Japan'] = 'Tokyo'
countries_capitals['South Africa'] = 'Cape Town'
countries_capitals['Australia'] = 'Canberra'
countries_capitals['New Zealand'] = 'Wellington'
countries_capitals['India'] = 'New Delhi'
countries_capitals['Greece'] = 'Athens'
 
def get_random_country():
    country = random.choice(list(countries_capitals.keys()))
    capital = countries_capitals[country]
    return (country, capital)

total_round = 0
correct = 0
wrong = 0

while True:
    player_choice = input('Play(p) or Quit(q): ')
    player_choice = player_choice.lower()
    if player_choice == 'p':
        total_round += 1
        print('Loading game')
        country, capital = get_random_country()
        print('Country : ', country)
        player_answer = input('Capital: ')
        if str(player_answer) == capital:
            print('Correct')
            correct += 1
        else: 
            print('Wrong')
            wrong += 1
    elif player_choice == 'q':
        print('You have done {0} round(s), correctly answered {1} time(s), and wrong for {2} time(s)'.format(total_round,correct,wrong))
        break
    else:
        print('Wrong Choice')       
 
