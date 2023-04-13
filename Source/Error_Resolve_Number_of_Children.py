import json

from qwikidata.linked_data_interface import get_entity_dict_from_api

for i in range(1251, 1501):

	with open('../Data/FinalData/FinalData_12500_15000/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			template_data = json.loads(line)

	for k, v in template_data.items():

		try:

			if 'बच्चों की संख्या' in v.keys():

				print("FINALLY")

				x = get_entity_dict_from_api(v['QID'])

				y = x['claims']['P1971'][0]['mainsnak']['datavalue']['value']

				v.update({'बच्चों की संख्या' : y})

		except:

			print(i)

			print(k, v)

	with open('../Data/FinalData/FinalData_12500_15000/Cool' + str(i) + '.json', 'w') as fout:

		json.dump(template_data, fout)