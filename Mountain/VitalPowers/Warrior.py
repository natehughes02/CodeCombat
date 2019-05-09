def pickUpNearestCoin():
    items = hero.findItems ()
    nearestCoin = hero.findNearest(items)
    if nearestCoin and hero.distanceTo(nearestCoin) < 30:
        if hero.isReady("jump"):
            hero.jumpTo(nearestCoin.pos)
        else:
            hero.move(nearestCoin.pos)


def summonSoldier():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")


def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)


def attack(target):
    if target:
        if (hero.isReady("stomp")):
            hero.stomp(target)
        elif (hero.canCast('chain-lightning', target)):
            hero.cast('chain-lightning', target)
        else:
            hero.attack(target)


def tacktick():
    enemies = hero.findEnemies ()
    nearest = hero.findNearest(enemies)
    friends = hero.findFriends()
    
    # Only if there is an enemy on us do we stop to attack, we want coins for soldiers.
    if nearest and (hero.distanceTo(nearest) < 5):
        attack(nearest)
    else:
        pickUpNearestCoin()


while True :
    tacktick()
    summonSoldier()
    commandSoldiers()
