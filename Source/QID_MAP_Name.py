import json, time

from qwikidata.linked_data_interface import get_entity_dict_from_api

with open('QID_NAME_MAP.json', 'r') as fin:

	for line in fin:

		data = json.loads(line)

count = 14100

updated_dict, exceptions = {}, {}

for key, val in data.items():

	try:

		time.sleep(5)

		x = get_entity_dict_from_api(key)

		text = x['labels']['en']['value']

		updated_dict[key] = text

		count += 1

		if count % 100 == 0:

			partition_num = str(count / 100).split('.')[0]

			with open('../QID_NAME_MAP' + partition_num + '.json', 'w') as fout:

				json.dump(updated_dict, fout)

			updated_dict = {}

			print("CHECKPOINT %d Reached \n" % (count / 100), end = ' ')

	except:

		exceptions[key] = val

		continue

print(exceptions)