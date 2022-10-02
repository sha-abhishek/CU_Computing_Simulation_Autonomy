def solution(list, num): 
    a=0 
    b=0 
    '''find a and b in array that a+b=num'''
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            a = list[i]
            b = list[j]
            if list[i] + list[j] == num:
                return a, b
    print ("sum for", num, "not found")
     
  
#numbers = [0, 21, 78, 19, 90, 13]

numbers = [0,21,78,19,90,13,23,22,3,1,5,8,2] 
print(solution(numbers, 21)) 
print(solution(numbers, 25)) 
print(solution(numbers,11))
