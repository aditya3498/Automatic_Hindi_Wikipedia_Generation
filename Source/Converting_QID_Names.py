import json

from qwikidata.linked_data_interface import get_entity_dict_from_api

updated_key, finaldict = {}, {}

for i in range(1251, 1501):

	with open('../Data/FinalData/FinalData_12500_15000/Cool' + str(i) + '.json', 'r') as f:

		for line in f:

			finaldata = json.loads(line)

	for key in finaldata.keys():

		try:

			x = get_entity_dict_from_api(finaldata[key]['QID'])['labels']['en']['value']

			updated_key[key] = str(x)

		except:

			finaldata = {k:v for k, v in finaldata.items() if k != key}

	finaldata = dict((updated_key[key], value) for (key, value) in finaldata.items())

	with open('../Data/FinalData/FinalData_12500_15000/Cool' + str(i) + '.json', 'w') as fout:

		json.dump(finaldata, fout)