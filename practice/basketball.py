class Player: # Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
    def __init__(self, dict_id):
        self.dict_id = dict_id
    def player_info(self, key):
        print({self.dict_id[key]})

kevin_durant = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
    }
jason_tatum = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
    }
kyrie_irving = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
    }

# create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.
JT = Player(jason_tatum)
KD = Player(kevin_durant)
KI = Player(kyrie_irving)

# given the example list of players at the top of this module (the one with many players) 
# write a for loop that will populate an empty list with Player objects from the original list of dictionaries.
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
	"age":16, 
	"position": "P", 
	"team": "en"
    }
]

new_list = []
for i in range(0, len(players)):
    new_list.append(players[i])

print(new_list)