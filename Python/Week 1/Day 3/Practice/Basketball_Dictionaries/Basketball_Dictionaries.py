
# ! Challenge 1: Update the Constructor


# ? Default constructor
# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

# ? updated constructor

class Player:
    def __init__(self,player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]
    def player_info(self):
        print(f"{self.name} \n {self.age} \n {self.position} \n {self.team}")
    @classmethod
    def get_team(cls, team_list):
        player_list = [cls(player_dict)for player_dict in team_list]
        return player_list


# ? updated constructor test
# kevin= {
#     "name": "Kevin Durant", 
#     "age":34, 
#     "position": "small forward", 
#     "team": "Brooklyn Nets"
# }

# kevin_player = Player(kevin)
# print(kevin_player.name)


# ! Challenge 2: Create instances using individual player dictionaries.

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}


Create your Player instances here!
player_jason = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# ! Challenge 3: Make a list of Player instances from a list of dictionaries

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
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


new_team = [Player(player_dict)for player_dict in players]

for player in new_team:
    player.player_info()

print("/"*50)

# ! ninja bonus

for player in Player.get_team(players):
    player.player_info()
    print("="*50)

