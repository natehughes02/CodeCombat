# To disable the fire-traps add the lowest trap.value to the highest value.
# Move to the white X and say the answer to Kitty the cougar.
# Defeat all the ogres if you dare.
# Once all ogres are defeated move to the red X.
# Look out for potions to boost your health.

#whiteX = {'x':27, 'y':42} <--- this causes the character to bug
redX = {'x':151 , 'y': 118} #<--- this allows the character to move to target but stop to fight
hazards = hero.findHazards()
max = 99
min = 0
for hazard in hazards:
    if hazard.value > min:
        min = hazard.value
    if hazard.value < max:
        max = hazard.value
hero.moveXY(27, 42)
hero.say(min + max)

while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        hero.attack(enemy)
    elif item:
        hero.move(item.pos)
    elif not enemy and not item:
        hero.move(redX)
