class Player: # Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
    def __init__(self, dict_id):
        self.dict_id = dict_id
    def player_info(self, key):
        print({self.dict_id[key]})

kevin_durant = {"name": "Kevin Durant",
                "age": 34,
                "position": "small forward",
                "team": "Brooklyn Nets"
                }
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

KD = Player(kevin_durant)
KD.player_info("age")