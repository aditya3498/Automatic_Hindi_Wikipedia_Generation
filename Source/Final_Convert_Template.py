import json

tf_sum, count, flag = 0, 0, 0

final_data = []

frequency_item, inverse_document_item = {}, {}

for i in range(1, 250):

	with open('FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			final_data.append(json.loads(line))

			for item in final_data:

				for val in item.values():

					if 'के छात्र ' in val['Hindi'] and i != 1:

						print(i)

						flag = 1

						break

				if flag == 1:

					break

			if flag == 1:

				break

	if flag == 1:

		break

'''for i in range(251, 601):

	with open('FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			final_data.append(json.loads(line))

for i in range(601, 1001):

	with open('FinalData/FinalData_6000_10000/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			final_data.append(json.loads(line))

for i in range(1001, 1251):

	with open('FinalData/FinalData_10000_12500/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			final_data.append(json.loads(line))

for i in range(1251, 1501):

	with open('FinalData/FinalData_12500_15000/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			final_data.append(json.loads(line))

for i in range(1501, 1721):

	with open('FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			final_data.append(json.loads(line))

for item in final_data:

	for val in item.values():

		del val['English']

#print(final_data[0])

for item in final_data:

	for val in item.values():

		for key in val['Hindi'].keys():

			if key in frequency_item:

				frequency_item[key] += 1

			else:

				frequency_item[key] = 1

#print(frequency_item.keys())

for val in frequency_item.values():

	tf_sum += val

for key, val in frequency_item.items():

	frequency_item[key] = val / tf_sum

for item in sorted(frequency_item, key = frequency_item.get, reverse = True):

	print(item, frequency_item[item])

	print("\n")'''