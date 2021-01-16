

def playerTurn(pHP, pMana, bHP, turns_s, turns_p, turns_r):
    # first apply any effects
    if turns_s > 0:
        turns_s -= 1

    if turns_p > 0:
        turns_p -= 1
        bHP -= 3
        if bHP <=0:
            return True, 0  # won, didn't use any mana

    if turns_r > 0:
        turns_r -= 1
        pMana += 101

    if pMana < 53:
        # ran out of mana, we lose
        return (False, 0)

    manausedwon = set()

    # try casting spells, if at least one wins, return the lease mana used
    # Magic missile!
    if bHP <= 4:
        # got him with MM, least mana cost possible so just return
        return (True, 53)

    pwon, usedmana = bossTurn(pHP, pMana-53, bHP-4, turns_s, turns_p, turns_r)
    if pwon:
        manausedwon.add(usedmana+53)

    # Drain!
    if pMana >= 73:
        if bHP <= 2:
            return (True, 73)

        pwon, usedmana = bossTurn(pHP+2, pMana-73, bHP-2, turns_s, turns_p, turns_r)
        if pwon:
            manausedwon.add(usedmana+73)

    # shield!
    if pMana >= 113 and turns_s == 0:
        pwon, usedmana = bossTurn(pHP, pMana-113, bHP, 6, turns_p, turns_r)
        if pwon:
            manausedwon.add(usedmana+113)
    # poison!
    if pMana >= 173 and turns_p == 0:
        pwon, usedmana = bossTurn(pHP, pMana-173, bHP, turns_s, 6, turns_r)
        if pwon:
            manausedwon.add(usedmana+173)

    # recharge!
    if pMana >= 229 and turns_r == 0:
        pwon, usedmana = bossTurn(pHP, pMana-229, bHP, turns_s, turns_p, 5)
        if pwon:
            manausedwon.add(usedmana+229)
   
    if len(manausedwon) > 0:
        return True, min(manausedwon)
    
    return False, 53






def bossTurn(pHP, pMana, bHP, turns_s, turns_p, turns_r):
    # first apply any effects
    if turns_s > 0:
        turns_s -= 1

    if turns_p > 0:
        turns_p -= 1
        bHP -= 3
        if bHP <=0:
            return True, 0  # won, didn't use any mana

    if turns_r > 0:
        turns_r -= 1
        pMana += 101

    if turns_s > 0:
        pHP -= 2
    else:
        pHP -= 9

    if pHP <= 0:
        return (False, 0)

    return playerTurn(pHP, pMana, bHP, turns_s, turns_p, turns_r)





pwon, manaused = playerTurn(50, 500, 58, 0, 0, 0)

print('Part 1: ', manaused)




