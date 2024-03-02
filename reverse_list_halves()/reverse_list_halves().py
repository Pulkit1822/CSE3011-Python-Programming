
L=list(map(int,input("Enter the list elements: ").split(',')))

first_half=L[:len(L)//2]
second_half=L[len(L)//2:]

first_half.reverse()
second_half.reverse()

L[len(L)//2:]=first_half
L[:len(L)//2]=second_half

print(L)