n = int(input())
for i in range(1,n+1): #control number of rows
    for u in range(1,i+1): #controlling internal loop and print 1 to i
        print(u,end=' ') #print digits and don't turn to newline
    print() #newline
for i in range(1,n+1):
    for u in range(1,n-i+2): #each row prints one less number than the previous
        print(u,end=' ')
    print()
for i in range(1,n+1):
    for u in range(n,i-1,-1): # print numbers from n down to i
        print(u,end=' ')
    print()
for i in range(1,n+1):
    for j in range(n-i): # repeat n-i times
        print(' ',end=' ') #printing spaces for right alignment
    for j in range(1,i+1): # controlling internal loop and print 1 to i
        print(j,end=' ') # print numbers from 1 to i
    print()
