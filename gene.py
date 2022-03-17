from random import randint, choice, randrange, choices
from math import log

entity = {}
create = 400
eneration = 0
NATURES_GIFT = 15
natural_occurance = ["eat", "kill", "live", "mate"]
li_nam = [["bear", "goat", "horse", "sheep"], ["dragon", "griffin"]]
affinities = ["Hp", "Att", "Def", "Spd", "Lck", "SpA", "SpD"]
environment = {"envr": "fire", "ntl_res": 1_000, "dift" : 5, "req_aff": ["Hp", "Att"]}

def base_stat_generator(aff, can_move = 1):
    stats = {i : 0 for i in affinities}
    stat, clas, afn = NATURES_GIFT, affinities, randint(4, 10)
    div = stat // len(clas)
    stats = {i : randint(can_move, div) for i in clas}
    stat -= sum(stats.values())
    for _ in range(stat):
        stats[choice(affinities)] += 1
    if type(aff) == type([]):
        for i in aff:
            if len(aff) > afn:
                stats[i] += 1
            else:
                n =round(afn/len(aff))
                stats[i] += n
                if afn - n:
                    stats[choice(aff)] += afn - n
    else:
        stats[aff] += 5
    return stats

def entity_generator(nam= "", affinity = "Hp", lspan = 50):
    base_stats = base_stat_generator(affinity)
    return {"name": nam.capitalize(), "aff": affinity, "stats" : base_stats, "lifespan" : randint(round(lspan / 5), lspan*2)}

def life(ent, envr):
    ls = ent["lifespan"]
    li = list(ent["stats"][i] for i in envr["req_aff"])
    ar = round(envr["ntl_res"] / envr["ntl_res"])
    eb = 0
    svd =  (envr["dift"]* len(envr["req_aff"]))
    sve = sum(li)
    sv = svd/sve

    for _ in range(5):
        if eb == 100:
            eb = 100+ 1
        for _ in range(10):
            rd = randint(0,int(ls/10))*10
            geno = ((ls-(rd* sv)+ar)/ (-100+eb))
            eb += 10 - (envr["dift"]*sv)
        ls += geno
    ls = round(ls)
    return [sve, ent["stats"], ls]
    
def create_new_gen(envir, nam= "boar", aff= 1, lspan = 50):
    best = [0,0,0]
    for _ in range(1000):
        entity = entity_generator(nam, affinities[aff], lspan)
        sve = life(entity, envir)
        if sve[0] > best[0]:
            best = sve
    new_gene = {"name":envir["envr"].capitalize() + entity["name"].capitalize(), "aff": envir["req_aff"], "lifespan": best[2]}
    return new_gene

def grow(ent, envr, en= 0, mult= 1.2, exp= 50):
    env = randint(0,1)
    luck = randrange(100, envr["ntl_res"], 5)
    if env == 0: yrs = round(randint(0, (ent["lifespan"]+1)) - (5 * 1.5)) 
    else: yrs = round(randint(0, ent["lifespan"]) - (5 / 1.5))
    stat = sum(ent["stats"].values())
    ext = 0.25
    if yrs > 100: ext = 10
    if yrs > 1000: ext = 100
    expr = yrs * luck * (365 + randint(-1, 0)) * ext
    maxexp, exprt, dis_stat = exp*(mult**1), exp, 1
    if "level" in ent.keys(): maxexp, dis_stat, expr = (exp * (mult**en["level"]), en["level"], expr) # check
    while True:
        prev = exprt
        if expr > exprt:
            maxexp *= mult
            exprt = round(maxexp)
            exprt += prev
        else:
            exprt -= expr
            break
    lvl = round(log((maxexp/exp), mult))
    maxexp = round(maxexp)
    stats = {j : round(i/stat * 100) for j, i in ent["stats"].items()}
    for j, i in stats.items(): stats[j] = ent["stats"][j] + round((i/ 100) * ((lvl-dis_stat)*round(NATURES_GIFT/3)))
    if yrs < 1: yrs= 1
    return {"name": ent["name"], "age": yrs, "lvl": lvl, "aff": ent["aff"], "stats" : stats, "lsn" : ent["lifespan"]}

for i in range(create):
    ent = choices(["normal", "advanced", "rare", "epic", "heaven"], [40,20,10,5,1])
    aff = randint(0, 6)
    nam, r_nam = (choice(li_nam[0]), choice(li_nam[1]))
    for j in range(randrange(1, 5)):
        k = 0
        if ent[0] == "normal":
            enty = entity_generator(nam, affinities[aff])
        elif ent[0] == "advanced":
            enty = entity_generator(nam, [affinities[aff], affinities[aff]])
        elif ent[0] == "rare":
            new_gene = create_new_gen(environment, nam, aff, 200)
            enty = entity_generator(new_gene["name"], new_gene["aff"], new_gene["lifespan"])
        elif ent[0] == "epic":
            enty = entity_generator(r_nam, [affinities[aff], affinities[aff]], 400)
        elif ent[0] == "heaven":
            new_aff = [affinities[aff]]
            new_gene = create_new_gen(environment, r_nam, aff, 800)
            for n in new_gene["aff"]: new_aff.append(n)
            enty = entity_generator(new_gene["name"], new_aff, new_gene["lifespan"])
        while str(k) in entity.keys(): k+=1
        entity[str(k)] = grow(enty, environment)

for i in entity:
    if entity[i]["stats"]["Hp"] > 100 and entity[i]["age"] < 100:
        print(entity[i])
