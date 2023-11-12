class Pokemon:
    def __init__(self, name, level, current_health, max_health, pokemon_type, is_knocked_out):
      self.name = name
      self.level = level
      self.current_health = current_health
      self.max_health = max_health
      self.pokemon_type = pokemon_type
      self.is_knocked_out = is_knocked_out

    def lose_health(self, decrease):
      hp_lost = self.current_health - max_health
      print("health was lost", hp_lost)
      return self.current_health - hp_lost

    def gain_health(self, increase):
      hp = self.current_health
      self.current_health = self.current_health + increase
      if self.current_health < max_health:
        self.current_health = max_health
      new_hp = self.current_health - hp
      print('{} health was restored'.format(new_hp))
      return self.current_health

    def knocked_out(self):
        if self.knocked_out < 0 and self.knocked_out == False:
          self.knocked_out = True
        return self.knocked_out

    def total_health(self):
        return '{name}now has {current}/{max} health'.format(name = self.name, current = self.current_health, max = self.max_health)
      
    def attack(self, target):
        hp = 0
        if self.knocked_out:
          print("{name} can't attack because it is knocked out!".format(name = self.name))
        elif (self.pokemon_type == 'Fire' and target.pokemon_type == 'Water') or (self.pokemon_type == 'Water' and target.pokemon_type == "Electric"):
          print("Half-Damage dealt.\n{attacker} {victim} for {damage}".format(attacker = self.name, victim = self.target, damage = round(self.level * 0.5)))
          damage = self.level * 0.5
        elif (self.pokemon_type == "Fire" and target.pokemon_type == "Ice") or (self.pokemon_type == "Electric" and target.pokemon_type == "Water"):
          print("Double-Damage dealt.\n{attacker} attacked {victim} for {damage} damage".format(attakcer = self.name, victim = target.name, damage = self.level * 2))
          damage = self.level * 2.0
        else:
          print("{attacker} attacked {victim} for {damage} damage".format(attacker = self.name, victim = target.name, damage = self.level))
          damage = self.level
        return target.health_decrease(damage)


class Trainer:
  '''Class representing the trainer'''

  
  def __init__(self, pokemons, potions, name, current_pokemon):
    self.pokemons = pokemons
    self.potions = potions
    self.name = name
    self.current_pokemon = current_pokemon

  def use_potion(self, pokemon):
    print ("{trainer} uses potion on {target}".format(trainer = self.name, target = self.current_pokemon))
    return Pokemon.health_increase(pokemon)
  
  def attack(self, target):
    print('{attacker} attacks {target}'.format(attacker = self.current_pokemon, target = target))
    return Pokemon.health_decrease(target)
  
  def is_active(self, current_pokemon):
    print('{} is the active Pokemon.'.format(current_pokemon))


venesaur = Pokemon('Venesaur', 1, 100, 100, 'grass', False)
charizard = Pokemon('Charizard', 1, 100, 100, 'fire', False)
slowbro = Pokemon('Slowbro', 1, 0, 100, 'water', True)
pikachu = Pokemon('Pikachu', 5, 100, 100, 'electric', False)
ash = Trainer([pikachu, charizard], 5, 'Ash', pikachu)
lisa = Trainer([venesaur, slowbro], 3, 'Lisa', venesaur)