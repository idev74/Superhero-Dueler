import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):
        if self.abilities or opponent.abilities:
            battle = True
            while battle == True:
                attack_damage = self.attack()
                opponent_damage = opponent.attack()

                self.take_damage(opponent_damage)
                opponent.take_damage(attack_damage)

                if self.is_alive() == True and opponent.is_alive() == False:
                    print(f'{self.name} has emerged victorious over {opponent.name}!')
                    self.add_kill(), opponent.add_death()
                    break
                elif self.is_alive() == False and opponent.is_alive() == True:
                    print(f'{opponent.name} has emerged victorious over {self.name}!')
                    self.add_death(), opponent.add_kill()
                    break
                else:
                    print(f'Unfortunately, neither fighter made it out alive...')
                    self.add_death(), opponent.add_death()
                    self.add_kill(), opponent.add_kill()
                    break

        else:
            print("It's a draw!")

    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        attack_damage = damage - self.defend()
        self.current_health -= attack_damage
        if self.current_health > 0:
            print(f'{self.name} heroically took {attack_damage} damage and has {self.current_health} HP remaining!')
        else:
            print(f'{self.name} has fallen after taking {attack_damage}...')
        return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else: 
            return True

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths