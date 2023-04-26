import json, itertools

from qwikidata.linked_data_interface import get_entity_dict_from_api

tf_sum, count, flag = 0, 0, 0

final_data = []

exceptions = {}

for i in range(1, 250):

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			final_data = json.loads(line)

	for key, val in final_data.items():

		award_qid_dict = {}

		if 'पुरस्कार प्राप्त' in val['Hindi']:

			try:

				x = get_entity_dict_from_api(str(key))['claims']['P166']

				for item in x:

					if 'qualifiers' in item.keys():

						if 'P6208' in item['qualifiers'].keys():

							text = item['qualifiers']['P6208'][0]['datavalue']['value']['text']

							try:

								label = get_entity_dict_from_api(item['mainsnak']['datavalue']['value']['id'])['labels']['hi']['value']

							except:

								label = get_entity_dict_from_api(item['mainsnak']['datavalue']['value']['id'])['labels']['en']['value']

							award_qid_dict[label] = text

				for k, v in award_qid_dict.items():

					if k in val['Hindi']['पुरस्कार प्राप्त']:

						value.append({k : v})

						value.remove(k)

			except:

				print("AWARD RECEIVED KEY PRESENT WHEN IT SHOULD NOT HAVE")

				print(key)

				print(i)

				exceptions[key] = i

			print(i)

			print(award_qid_dict)

		else:

			print(i)

			print("NO AWARD KEY FOUND")

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'w') as fout:

		json.dump(final_data, fout)

final_data = []

for key, val in exceptions.items():

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(val) + '.json', 'r') as fin:

		for line in fin:

			final_data = json.loads(line)

	print(final_data[key]['Hindi'].keys())

	final_data[key]['Hindi'] = {k : v for k, v in final_data[key]['Hindi'].items() if k != 'पुरस्कार प्राप्त'}

	print(final_data[key]['Hindi'].keys())

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(val) + '.json', 'w') as fout:

		json.dump(final_data, fout)