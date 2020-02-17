
def dictionary(input):
    keys=[]
    values=[]
    for i in input:
        keys.append(i[0])
        values.append(i)

    return dict(zip(keys,values))





print (dictionary(["ahmed","Mohamed"]))
