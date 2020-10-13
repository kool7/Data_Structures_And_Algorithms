import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp -= dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enermy strikes for", dmg, "Current HP:", playerhp)

    if playerhp == 30:
        print("Go charge your health")
        break