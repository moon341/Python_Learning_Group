def graph_dict(tuple_of_connected_nodes):
    c={}
    f=[]
    g=0
    for key,value in tuple_of_connected_nodes:
        if key != g:
            g=key
            #c={key:f}
            del f
            f=[]
            f.append(value)
            #c={key:f}
            c.update({key:f})
        elif key == key:
            g=key 
            f.append(value)
            continue
    return c

d=((1,2),(2,1),(2,6),(2,7),(2,3),(3,4),(3,2),(3,5),(4,2),(4,3),(4,5),(5,3),(5,4),(6,2),(7,2),(8,9),(9,8))
t=graph_dict(d)
print(t)