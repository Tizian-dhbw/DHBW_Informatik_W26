nterms = 10
n1 = 0
n2 = 1
count = 0

for i in range(5,20,2):
    print(i)


# while-Schleife: solange Kriterium erfüllt ist, wird Schleife durchlaufen
while count < nterms: 
       # The next is a smart version of print(str(n1) + ' , ')
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
