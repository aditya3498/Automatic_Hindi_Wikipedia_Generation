import json

list_to_remove = []

new_dup = {}

count = 0

for i in range(1501, 1721):

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			data = json.loads(line)

	with open('Duplicated.json', 'r') as fin:

		data_dup = json.load(fin)

	'''for k, v in data_dup.items():

		for key, value in data.items():

			if k == value['QID']:

				count += 1

				print(i)

				print(key, value)'''

	for key, val in data.items():

		for k, v in data_dup.items():

			if key == v:

				list_to_remove.append(k)

#print(count)

print(len(list_to_remove))

print(len(data_dup))

for x in list_to_remove:

	try:

		del data_dup[str(x)]

	except:

		#print(data_dup)

		print(x)

print(len(data_dup))

with open('Duplicated.json', 'w') as fout:

	json.dump(data_dup, fout)