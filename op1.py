dictionary1 = {"Google" : 1,
               "Facebook" : 2,
               "microsoft" :3}

dictionary2 = {"GFG" : 1,
               "microsoft" : 2,
               "Youtube" :3}

dictionary1.update(dictionary2)
for key,values in (dictionary1.items()):
    print(key,values)

