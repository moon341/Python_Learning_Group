def graph_dict(tuple_of_connected_nodes):
    dicti={}
    for key,value in tuple_of_connected_nodes:
        if key in dicti:
            temp=[]
            temp = dicti[key]
            temp.append(value)
            dicti.update({key:temp})
        else:
            temp=[]
            temp.append(value)
            dicti.update({key:temp})
    return dicti

d=((1,2),(2,6),(2,7),(2,3),(3,4),(2,1),(3,2),(3,5),(4,2),(4,5),(5,3),(5,4),(6,2),(4,3),(7,2),(8,9),(9,8))
t=graph_dict(d)
print(t)
