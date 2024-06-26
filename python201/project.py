import requests

while True:
    pokemon = input('Search for a pokemon by name(quit for stopping): ').rstrip().lstrip().lower()

    if pokemon == 'quit':
        break

    req  = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if(req.status_code == 200):
        data = req.json()
        print(f"Results found:\nName: {data['name']}\nBase Experience: {data['base_experience']}")
        if data['abilities'] and len(data['abilities']) > 0:
            print('Abilities:')
            for index, item in enumerate(data['abilities']):
                print(f"\t{index+1}-{item['ability']['name']}{'(Hidden)' if item['is_hidden'] else ''}")
        try_again = input('Continue?(Y/N): ').lower()
        if try_again != 'y':
            break        
    else:
        try_again = input('Pokemon not found! Try again?(Y/N): ').lower()
        if try_again != 'y':
            break          
