import json

from qwikidata.linked_data_interface import get_entity_dict_from_api

with open('../QID_NAME_MAP.json', 'r') as fin:

	for line in fin:

		x = json.loads(line)

for k, v in x.items():

	try:

		x.update({k : get_entity_dict_from_api(str(k))['labels']['en']['value']})

	except:

		print(k, v)

with open('../QID_NAME_MAP_1.json', 'w') as fout:

	json.dump(x, fout)