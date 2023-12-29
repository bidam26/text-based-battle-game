import os
from character import *
from weapon import *



hero = Hero(name="Hero name", health=100)
enemy = Enemy(name="Enemy Name", health=80, weapon=fists)



while True:
    os.system("cls")
    hero.equip_weapon(iron_sword)

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()


    # print(f"{hero.name}'s health : {hero.health}")
    # print(f"{enemy.name}'s health : {enemy.health}")

    input()

