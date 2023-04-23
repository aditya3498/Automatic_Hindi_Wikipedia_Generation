import json

for i in range(1, 250):

	with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			data = json.loads(line)

	with open('Duplicated.json', 'r') as fin:

		for line in fin:

			data_dup = json.loads(line)

	for k, v in data_dup.items():

		for key, value in data.items():

			if k == value['QID']:

				print(i)

				print(key, value)