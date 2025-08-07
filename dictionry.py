def q1():
    field=("name","age","city")
    data=("Alice",21,"Delhi")
    print(dict(zip(field,data)))
def q2():
    data = {"a": [1], "b": [1, 2, 3], "c": [1, 2]}
    def get_length(item):
        return len(item[1])
    sorted_dict = dict(sorted(data.items(), key=get_length))
    print(sorted_dict)
def q3():
    data=[(1, 2), (2, 3), (1, 2), (2, 3), (2, 3)]
    d={}
    for i in data:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)
q3()


