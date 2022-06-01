capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia': 'Moscow'}

#print(capital['Russia'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

capitals.update({'Germany':'Berlim'})
#capitals.update({'USA':'Houston'})
#capitals.pop('China')
capitals.clear()

for key, value in capitals.items():
    print(key, value)