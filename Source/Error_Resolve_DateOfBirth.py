import json

from qwikidata.linked_data_interface import get_entity_dict_from_api

exceptions, map_data = [], []

for i in range(1, 334):

	with open('../QID_MAP/QID_NAME_MAP' + str(i) + '.json', 'r') as fin:

		for line in fin:

			map_data.append(json.loads(line))

for i in range(570, 571):

	with open('../Data/FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'r') as fin:
	
		for line in fin:

			data = json.loads(line)

	for val in data.values():

		new_dict = {key : value for key, value in val['Hindi'].items() if key != 'QID'}

		val['Hindi'] = new_dict

	delete = []

	for key, value in data.items():

		flag = 0

		for item in map_data:

			for k, v in item.items():

				if key == v:

					value['Hindi']['QID'] = k

					flag = 1

					break

			if flag == 1:

				break

		if flag == 0:

			#print(i)

			#print(key)

			delete.append(key)

	for item in delete:

		del data[item]

	#print(data)

	delete_again = []

	for key, val in data.items():

		if 'QID' in val['Hindi'].keys():

			try:

				text_dob = get_entity_dict_from_api(val['Hindi']['QID'])['claims']['P569']

				val['Hindi'].update({'जन्म तिथि' : text_dob[0]['mainsnak']['datavalue']['value']})				

			except:

				delete_again.append(key)

				continue

	for item in delete_again:

		del data[item]

	delete_again_2 = []

	for key, val in data.items():

		if 'QID' in val['Hindi'].keys():

			try:

				text_dod = get_entity_dict_from_api(val['Hindi']['QID'])['claims']['P570']

				val['Hindi'].update({'मृत्यु तिथि' : text_dod[0]['mainsnak']['datavalue']['value']})				

			except:

				delete_again_2.append(key)

				continue

	for item in delete_again_2:

		del data[item]

	#print(len(data))

	with open('../Data/FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'w') as fout:
	
		json.dump(data, fout)