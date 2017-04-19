#################################################################################################
#utopian tree:
'''
def calc_height(n):
    if  n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        height = 1
        while n>0:
            height = height * 2
            n = n - 1
            if not n:
                break
            else:
                height = height+1
                n= n - 1
    
    return height


t = int(raw_input('enter the number of test inputs:').strip())
for a0 in xrange(t):
    n = int(raw_input('enter the intial height of the tree:').strip())
    height = calc_height(n)
    print height
'''
#################################################################################################
# class to cancel or not 
'''
def check_status(a, k):
    cnt = 0
    for x in a:
        if x<=0:
            cnt+=1
    return True if cnt < k else  False

    
    


t = int(raw_input('enter tests:').strip())
for a0 in xrange(t):
    n,k = raw_input('enter n, k :').strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input('enter student list:').strip().split(' '))
    status = check_status(a,k)
    print status
'''
####################################################################################
#no of days going to movie    
''''     
x,y,z = map(int, (raw_input().split()))
cnt = 0 
for eve in xrange(x,y+1):
    t = abs(eve-int(str(eve)[::-1]))% z
    if t == 0:
        cnt+=1

print cnt
'''
###############################################################################
from module3 import differnces
def addition(x, y ):
    diff = differnces(x, y)
    return diff
 




    
    
