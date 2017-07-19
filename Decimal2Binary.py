
def binary(n):

      if n==1:
        a.append(n)
        return

      elif (n % 2 in (0, 1)):
        a.append(n%2)
        n_nxt=int(n/2)
        binary(n_nxt)

a=[]
items=[int(x) for x in input("Enter the test cases: ").split(' ')]     #
for i in (items):
  binary(i)
  string = ''.join(str(e) for e in a[::-1])  # convert list to string using join, if list has string just ''.join(list)
  print(i,':',string)                              #list slicing to print in reverse order
  a.clear()                                   # for the next number to be fed into the list

# well 2 nd commit