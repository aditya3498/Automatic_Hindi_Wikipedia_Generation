import json 

from qwikidata.linked_data_interface import get_entity_dict_from_api

with open('../Data/FinalData/FinalData_1_2500/Cool246.json', 'r') as fin:

	for line in fin:

		data = json.loads(line)

#x = get_entity_dict_from_api(data['Peter Wright']['QID'])['claims'].keys()

#for keys in x:

#	y = get_entity_dict_from_api(keys)

#del data['Mikhail Krishtal']

data['Nikolay Mel\'nikov']['QID'] = "Q4289886"

with open('../Data/FinalData/FinalData_1_2500/Cool246.json', 'w') as fout:

	json.dump(data, fout)