from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    self.team_one = Team('Team 1')
    self.team_two = Team('Team 2')

  def create_ability(self):
    name = input("What is the ability name?  ")
    max_damage = int(input("What is the max damage of the ability?  "))

    return Ability(name, max_damage)

  def create_weapon(self):
    weapon_name = input("What is the weapon name?  ")
    max_damage = int(input("What is the max damage of the weapon?  "))

    return Weapon(weapon_name, max_damage)

  def create_armor(self):
    armor_name = input("What is the armor name?  ")
    max_block = int(input("What is the max block of the armor?  "))

    return Armor(armor_name, max_block)

  def create_hero(self):
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        hero.add_ability(self.create_ability())
      elif add_item == "2":
         hero.add_weapon(self.create_weapon())
      elif add_item == "3":
        hero.add_armor(self.create_armor())
    return hero


  def build_team_one(self):
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
        hero = self.create_hero()
        self.team_one.add_hero(hero)
  
  def build_team_two(self):
    numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numOfTeamMembers):
        hero = self.create_hero()
        self.team_one.add_hero(hero)
    
  def team_battle(self):
    self.team_one.attack(self.team_two)

  def show_stats(self):
    print("\n")
    print(f'{self.team_one.name} statistics: ')
    self.team_one.stats()
    print("\n")
    print(f'{self.team_two.name} statistics: ')
    self.team_two.stats()
    print("\n")

    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(f'{self.team_one.name} average K/D was:{str(team_kills/team_deaths)}')
    
    for hero in self.team_two.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(f'{self.team_two.name} average K/D was:{str(team_kills/team_deaths)}')

    if self.team_two.team_deaths > self.team_one.team_deaths:
        print(f'Congratulations {self.team_one.name}! You are the ultimate champions!')
    else:
        print(f'Congratulations {self.team_two.name}! You are the ultimate champions!')
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print(f'survived from {self.team_one.name}: {hero.name}')
    for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print(f'survived from {self.team_two.name}: {hero.name}')


  if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False

        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()