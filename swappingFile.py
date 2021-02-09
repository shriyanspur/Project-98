def swapData():
  file_a = input('Enter the first file name: ')
  file_b = input('Enter another file name: ')

  with open(file_a, 'r') as a:
    data_a = a.read()
  
  with open(file_b, 'r') as b:
    data_b = b.read()

  with open(file_a, 'w') as a:
    a.write(data_b)

  with open(file_b, 'w') as b:
    b.write(data_a)

swapData()