def solution(list, num):
    hasht = {}
    
    for a in list:
        b = num - a
        #print(hasht)
        if b in hasht:
            print(hasht[b],b)
            return hasht[b],b
            
        hasht[a] = b
        print(hasht)
        
    else:    
        return ('not found')
    
    
list = [1,5,7,0,11,15,22,25]
solution(list,16)