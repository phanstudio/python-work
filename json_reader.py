import json
class Custom_json:
    @staticmethod
    def json_loader(path: str):
        with open(path, "r") as f:
            data = json.load(f)

        i = ""
        li = {}
        ti = []
        ui = set()
        l = data.keys()
        for y in l:
            i = str(y)
            #print(len(data[i][0]))
        for choices in data[i]:
            for x in choices.keys():
                ui.add(x)
        for z in data[i]:
            for x in range(2):
                ti.extend(z)
                #ti.append(data[i][x][z])
        for choices in data[i]:
            for key in choices.keys():
                #li[key] = ti[0]
                pass
        print(ui)
        #print(li)
        return li

Custom_json.json_loader("questions.json")