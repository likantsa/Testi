import random
name = "antsa"
name2 = "enemy"
health = 100
health2 = 100   
turn = 0

def take_damage(health, damage):
    health -= damage
    health = max(health, 0)
    return health

def resolve_attack(fighter_name, fighter_health, damage, random_number):
    if random_number < 50:
        fighter_health = take_damage(fighter_health, damage)
        print(f"{fighter_name} took {damage} damage and now has {fighter_health} health left.")
    elif random_number == 90:
        fighter_health = min(fighter_health + 10, 100)
        print(f"{fighter_name} found a health pack and now has {fighter_health} health.")
    else:
        print(f"{fighter_name} is immune to damage and remains at {fighter_health} health.")
    return fighter_health

def take_turn(health, health2):
    damage_taken = random.randint(10, 30)
    random_number = random.randint(1, 100)
    roll = random.randint(1, 2)

    if roll == 1:
        health = resolve_attack(name, health, damage_taken, random_number)
    else:
        health2 = resolve_attack(name2, health2, damage_taken, random_number)
    return health, health2

while health > 0 and health2 > 0:
    turn += 1
    print(f"Turn {turn}:")
    health, health2 = take_turn(health, health2)
    
if health < health2:
    print(f"{name2} wins with {health2} health left!")
else:
    print(f"{name} wins with {health} health left!")