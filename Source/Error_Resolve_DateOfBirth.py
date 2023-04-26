import json

from qwikidata.linked_data_interface import get_entity_dict_from_api

input1 = str(input())

input2 = str(input())

with open('../Data/FinalData/FinalData_2500_6000/Cool' + input1 + '.json', 'r') as fin:
	
	for line in fin:

		data = json.loads(line)

	try:

		text_dob = get_entity_dict_from_api(data[input2]['QID'])['claims']['P569']

		data[input2].update({'जन्म तिथि' : text_dob[0]['mainsnak']['datavalue']['value']})

	except:

		print("QID ERROR")

		#print(key, val)

	try:

		text_dod = get_entity_dict_from_api(data[input2]["QID"])['claims']['P570']

		data[input2].update({'मृत्यु तिथि' : text_dod[0]['mainsnak']['datavalue']['value']})

		print(data[input2])

	except:

		print("DEATH")

			#print(i)

			#print(key, value)'''

	#print(data[input2])

	#print(data)				

	#print(data)

	#with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'w') as fout:

	#	json.dump(data, fout)

	'''for key, val in data.items():

		if 'QID' in val['Hindi'].keys():

			try:

				text_dod = get_entity_dict_from_api(val['Hindi']['QID'])['claims']['P570']

				val['Hindi'].update({'मृत्यु तिथि' : text_dod[0]['mainsnak']['datavalue']['value']})				

			except:

				delete_again_2.append(key)

				continue

	for item in delete_again_2:

		del data[item]

	#print(len(data))'''

with open('../Data/FinalData/FinalData_2500_6000/Cool' + input1 + '.json', 'w') as fout:
	
	json.dump(data, fout)