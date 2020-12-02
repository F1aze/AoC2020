input = open('../in/2.in', 'r')

data = []

for line in input:
	data.append(line.strip())

lowerBounds = []
upperBounds = []
keys  =[]
passwords = []
	
for line in data:
	lowerBounds.append(int(line.split('-')[0]))
	upperBounds.append(int(line.split(' ')[0].split('-')[1]))
	keys.append(line.split(' ')[1].split(':')[0])
	passwords.append(line.split(": ")[-1])

result = 0
i = 0
lowerbool = 0
upperbool = 0

while i < 1000:
	print(i)
	if passwords[i][lowerBounds[i]-1] == keys[i] and passwords[i][upperBounds[i]-1] != keys[i]:
		result = result + 1
	if passwords[i][lowerBounds[i]-1] != keys[i] and passwords[i][upperBounds[i]-1] == keys[i]:
		result = result + 1
	i = i + 1
	
print(result)