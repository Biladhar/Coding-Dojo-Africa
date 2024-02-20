class user:
    def __init__(self, first_name,last_name,email,age,is_rewards_member = False ,gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age 
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
# * adding display_info method
    def display_info(self):
        print("First name: ",self.first_name)
        print("Last name: ", self.last_name)
        print("email: ", self.email)
        print("age: ", self.age)
        print("is rewards member: ", self.is_rewards_member)
        print("Gold card points: ", self.gold_card_points)
# * adding enroll method
    def enroll(self):
        if (self.is_rewards_member == True):
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
# * adding spend_point method
    def spend_points(self,amount):
        if(self.gold_card_points>= amount):
            self.gold_card_points = self.gold_card_points - amount
        else:
            no_point = "You don't have enough points"
            print(no_point)
            return no_point





user1 = user("foulen","benfoulen","f@f.f",30)
user1.display_info()
user1.enroll()

cristiano = user("Cristiano", "Ronaldo", "cristiano@ronaldo.com", 39)
messi = user("leo","messi", "leo@messi.com", 40 )


cristiano.display_info()

print("="*30)

cristiano.enroll()

print("="*30)

cristiano.display_info()

print("="*30)

cristiano.spend_points(50)

print("="*30)

messi.enroll()

print("="*30)

messi.spend_points(80)

print("="*30)

messi.display_info()
print("="*30)
cristiano.display_info()
print("="*30)
cristiano.enroll()
print("="*30)
messi.spend_points(300)











