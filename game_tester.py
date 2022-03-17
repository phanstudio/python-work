from dialog import DialogReader as dr
from random import randint as ri
hp = 3 #Health
defn = 2 #Defence
att = 1 #Attack
enemy_hp = 10
enemy_att = 100
max_enemy_hp = enemy_hp
max_hp = hp
hp_opt = 1
choice = ["att", "heal-opt", "heal"]
choice1 =["rush in and att", "hide and shot"] #low hp, rushing in rules
p = 1
l = 0
kill = 0

# option creator
i = ""
for c in choice1:
    i = i + f"[{c.capitalize()}[{c[0].upper()}]] "
i = i[:-1]

while True:
    #print(kill)
    opt = ""#dr.dialog("Kill: " + str(kill) + "\n" + 
    #"EnemyHp: " + str(enemy_hp) + "\n" + "Hp: " + str(hp) + "\n" + "what do you want to do?" + "\n" + i + "\n")
    if opt == "":
        opt = i[1]
    
    if p == 0:
        if opt[0].lower().strip() == "a":
            hp -= 1
        if opt[0].lower().strip() == "h" and not "o" in opt:
            if hp != max_hp:
                hp += hp_opt
            else:
                print("your hp is full")
            if hp > max_hp:
                hp = max_hp
        if opt[0].lower().strip() == "h" and "o" in opt:
            hp_opt = int(dr.dialog("select heal option?", ["numb"], quiter= False))
            if hp_opt > max_hp:
                hp_opt = max_hp
        
    elif p == 1:
        if opt[0].lower().strip() == "r":
            h = ri(0,2)
            if h == 0:
                if hp < max_hp + 1:
                    hp += 1
                else:
                    hp -= enemy_att / 2
                enemy_hp -= att
            elif h == 2:
                if hp == 1:
                    enemy_hp -= enemy_hp
                elif hp < max_hp + 1:
                    hp += 2
            else:
                hp -= enemy_att
        if opt[0].lower().strip() == "h":
            enemy_hp -= (att * 1.5)
            if enemy_hp > 0:
                hp -= enemy_att

    if hp > max_hp + 1:
        hp = max_hp + 1
    if hp <= 0:
        kill = 0
        print("you died!")
        if l < 40:
            l += 1
            hp = max_hp
        else:
            break
    elif enemy_hp <= 0:
        kill += 1
        print(kill)
        enemy_hp = max_enemy_hp