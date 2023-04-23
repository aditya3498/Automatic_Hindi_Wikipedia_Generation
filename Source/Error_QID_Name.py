import json

from qwikidata.linked_data_interface import get_entity_dict_from_api

to_be_updated = {}

for i in range(1501, 1721):

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			template_data = json.loads(line)

	with open('../QID_NAME_MAP_1.json', 'r') as fin:

		for line in fin:

			map_data = json.loads(line)

	for key, value in template_data.items():

		for k, v in map_data.items():

			if value['QID'] == k:

				if key != v:

					print(i)

					print(key, value)

					template_data[v] = template_data.pop(key)

	#print(template_data)

	'''for key, value in template_data.items():

		#flag = True

		for k, v in map_data.items():

			try:

				if value['QID'] == k:

					#flag = False

					template_data[v] = template_data.pop(key)

					break

			except:

				print(i)

				print(value)

				break

		#if flag == True:

		#	print(key, value)

		#	print(i)

			#print(key, value)

	#print(template_data.keys())

	#print("\n")'''

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'w') as fout:
		
		json.dump(template_data, fout)