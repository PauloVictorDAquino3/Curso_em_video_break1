num_int= float(input("Digite um numero flutuante que você quer a tabuada: "))

x1=num_int * 1
x2=num_int * 2
x3=num_int * 3
x4=num_int * 4
x5=num_int * 5
x6=num_int * 6
x7=num_int * 7
x8=num_int * 8
x9=num_int * 9
x10=num_int * 10

while num_int != x10:
  for c in range (1, 11):
    print (f"{num_int} * {c} = {num_int * c} ")
  break
