from typing import Any, List
import numpy as np
line = 8
def calculate(li:List[Any]):
    """
    This function is used to calculate different matrics\n
    => li: IN the parameter the list should contain '9 elements'\n
    The output is the mean, std, var, max, sum, min of the matrix
    """
    if len(li) != 9: print("Traceback (most recent call last):", r"  File 'c:\Users\Phantom\Desktop\Visual_studio_code\mean_var_std.py', " + f"line {line}, in <module>",
    "    "+str(li) + "; len(li) != 9" + " The values in the list 'should be 9'", "Length Error", sep= "\n"); quit()
    x1 = np.array(li)
    x = np.resize(x1, (3,3))

    y = []
    y1 =[]
    dic = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "max" : [],
        "min" : [],
        "sum" : []
    }
    for i in range(2):
        y.append((
            (list(np.mean(x, i))),
            (list(np.var(x, i))),
            (list(np.std(x, i))),
            (list(np.max(x, i))),
            (list(np.min(x, i))),
            (list(np.sum(x, i)))
        ))

        for j, l in enumerate(dic):
            dic[l].append(y[i][j])

    y1.append((
            (np.mean(x1)), (np.var(x1)), (np.std(x1)), (np.max(x1)), (np.min(x1)), (np.sum(x1))
        ))
    for j, l in enumerate(dic):
        dic[l].append(y1[0][j])
    return dic

li = [i for i in range(9)]
x= calculate(li)
print(x)