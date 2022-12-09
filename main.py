with open('C:\\Users\\andri\\OneDrive\\Робочий стіл\\proj\\text') as f:
   i = 1
   for line in f:
      sym = len(line)
      words = len(line.split(" "))
      print("Line ",i," кількість слів ",words," кількість символів ",sym,"\n")
      i+=1