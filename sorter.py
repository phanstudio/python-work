import operator
def start_sort(fileSort):
    fn = open(fileSort, "r")
    text = fn.read()
    words = text.lower().split()
    cleanList = []
    for eachWord in words:
        cleanList.append(eachWord)
    clean_up_list(cleanList)
      
def clean_up_list(list):
    cleanUpList = []
    for word in list:
        dontAdd = "!@#$%^&*()_+=-}{[]|:\"';,.></?"
        for i in range(0, len(dontAdd)):
            word = word.replace(dontAdd[i], "")
        if len(word) > 0:
            cleanUpList.append(word)
    sorter(cleanUpList)

def sorter(list):
    wordCount = {}
    counter = {}
    for sort in list:
        if sort in wordCount:
            wordCount[sort] += 1
        else:
            wordCount[sort] = 1
    for key, value in sorted(wordCount.items(), key=operator.itemgetter(1)):
        counter[key] = value
        print(key, value)
    #print(counter)

start_sort("InstallationLog.txt")