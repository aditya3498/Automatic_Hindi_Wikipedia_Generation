import json 

from qwikidata.linked_data_interface import get_entity_dict_from_api

input1 = str(input())

input2 = str(input())

with open('../Data/FinalData/FinalData_15000_Final/Cool' + input1 + '.json', 'r') as fin:

	for line in fin:

		data = json.loads(line)

#x = get_entity_dict_from_api(data['Peter Wright']['QID'])['claims'].keys()

#for keys in x:

#	y = get_entity_dict_from_api(keys)

del data[input2]['मृत्यु तिथि']

#del data[input2]['जन्म तिथि']

#data['Pavel Komárek']['QID'] = "Q95227850"

with open('../Data/FinalData/FinalData_15000_Final/Cool' + input1 + '.json', 'w') as fout:

	json.dump(data, fout)