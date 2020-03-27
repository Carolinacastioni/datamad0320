
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
        
    def attack(self):
        return self.strength     
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return f"Odin Owns You All!"
        
        

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War

import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack (self):
        rand_viking = random.choice(self.vikingArmy)
        rand_saxon = random.choice(self.saxonArmy)
        if rand_viking.strength >= rand_saxon.receiveDamage():
            saxonArmy -= rand_saxon
            return f"result of calling {receiveDamage()} of a Saxon with the strength of a Viking"
        else:
            return f"result of calling {receiveDamage()} of a Saxon with the strength of a Viking"
    
    def saxonAttack (self):
        rand_viking = random.choice(self.vikingArmy)
        rand_saxon = random.choice(self.saxonArmy)
        if rand_saxon.strength >= rand_viking.receiveDamage():
            vikingArmy -= rand_viking
            return f"result of calling {receiveDamage()} of a Saxon with the strength of a Viking"
        else:
            return f"result of calling {receiveDamage()} of a Viking with the strength of a Saxon"

    def showStatus (self):
        return f"Currently situation is:" len(vikingArmy) "and" len(saxonArmy)
        if len(saxonArmy)<1:
            return f"Vikings have won the war of the century!"
        elif len(vikingArmy)<1:
            return f"Saxons have fought for their lives and survive another day..." 
        elif len(saxonArmy)>1 or len(vikingArmy) >1:
            return f"Vikings and Saxons are still in the thick of battle."
    
