def solution(list, num):
    hasht = {}
    
    for a in list:
        b = num - a
        #print(hasht)
        if b>=0:
            if b in hasht:
            #print(hasht[b],b)
                return print(hasht[b],b)
            
            hasht[a] = b
            #print(hasht)
    return print("sum for", num, "not found")
    
    
list = [1,5,7,0,11,15,22,25]
solution(list,26)
