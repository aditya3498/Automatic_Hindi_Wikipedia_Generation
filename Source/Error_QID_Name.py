import json

from qwikidata.linked_data_interface import get_entity_dict_from_api

to_be_updated = {}

for i in range(251, 601):

	with open('../Data/FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			template_data = json.loads(line)

	with open('../QID_NAME_MAP.json', 'r') as fin:

		for line in fin:

			map_data = json.loads(line)

	for key, value in template_data.items():

		for k, v in map_data.items():

			if key == v:

				if template_data[key]['QID'] != k:

					print("COOL")

					template_data[key].update({'QID' : k})

					break

				else:

					break

	#with open('../Data/FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'w') as fout:

	#	json.dump(template_data, fout)