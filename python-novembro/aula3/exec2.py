data = input("Informe a data: ")

print(data)

data = data.split('-')

print(data)

# data.reverse()

print(data)

data = "%s/%s/%s" % (data[2], data[1], data[0])

# data = "/".join(data)

print(data)