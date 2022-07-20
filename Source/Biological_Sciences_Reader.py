import json, time

import pandas as pd

import itertools

from qwikidata.linked_data_interface import get_entity_dict_from_api

from qwikidata.entity import WikidataItem

#from anuvaad import Anuvaad

#anu = Anuvaad('english-hindi')

scientist, hindi_person_data, scientists, final_list = [], [], [], []

label_person_list, freq, append = {}, {}, {}

count = 0

remove_identifier = ['P1559', 'P2888', 'P949', 'P856', 'P6656', 'P1670', 'P9223', 'P7700', 'P434', 'P1449', 'P746', 'P1950', 'P2031', 'P2873', 'P1442', 'P1801', 'P2277', 'P2021', 'P2089', 'P2536', 'P1438', 'P947', 'P1814', 'P2428', 'P1248', 'P1260', 'P428', 'P835', 'P7704', 'P6385', 'P1477', 'P443', 'P485', 'P1225', 'P1150', 'P5821', 'P5008', 'P9037', 'P1695', 'P4839', 'P6379', 'P7763', 'P3919', 'P6482', 'P5101', 'P4431', 'P1017', 'P271', 'P646', 'P373', 'P691', 'P213', 'P1472', 'P727', 'P5587', 'P1343', 'P18', 'P227', 'P1144', 'P214', 'P345', 'P349', 'P409', 'P244']

with open('hindi_person_data.json', 'r') as f:

	for line in f:

		hindi_person_data.append(json.loads(line)['en_label'])

with open('Scientist.json', 'r') as fin:

	for line in fin:

		scientist = json.loads(line)

#print(scientist)

for item in scientist:

	if item['itemLabel'][1:].isnumeric():

		continue

	else:

		scientists.append(item['itemLabel'])

main_list = [x for x in scientists if x not in hindi_person_data]

for item in main_list:
	
	for item1 in scientist:
		
		if item == item1['itemLabel']:

			final_list.append(item1['item'].split('/')[-1])

			break
#print(final_list[:10])
#print(final_list[5358])
for item in final_list[5358:5359]:

	#time.sleep(5)

	count += 1

	#print(count)

	#print(item)

	person_labelled, label_list, english_label_list = {}, {}, {}

	non_labelled = []

	try:

		list_prop_value = get_entity_dict_from_api(str(item))['claims']

	except:

		print("PROBLEM")

		print(count)

		continue
	
	list_property = list(list_prop_value.keys())

	list_property = [x for x in list_property if x not in remove_identifier]

	for prop in list_property:

		#time.sleep(25)

		if prop not in label_list.keys():

			try:

				prop_det = get_entity_dict_from_api(prop)

				if 'hi' in prop_det['labels'].keys():

				#prop_det = get_entity_dict_from_api(prop)

					prop_label = prop_det['labels']['hi']['value']

				#if prop_label.split(" ")[-1].lower() != 'id':

					if prop_label.split(" ")[-1].lower() != 'अभिज्ञापक':

						label_list[prop] = prop_label

				else:

					y = prop_det['labels']['en']['value']

					if y.split(" ")[-1].lower() != 'id':

					#english_label_list[prop] = y

						label_list[prop] = y

						non_labelled.append(y)

			except:

				continue

	list_property = list(label_list.keys())

	for prop in list_property:

		#time.sleep(25)

		labelled = []

		for val in list_prop_value[prop]:

			if val['mainsnak']['snaktype'] == 'value' and isinstance(val['mainsnak']['datavalue']['value'], str):	

				labelled.append(val['mainsnak']['datavalue']['value'])
	
			elif val['mainsnak']['snaktype'] == 'value' and isinstance(val['mainsnak']['datavalue']['value'], dict):
		
				if 'id' in val['mainsnak']['datavalue']['value'].keys():
			
					value_id = val['mainsnak']['datavalue']['value']['id']
			
					value_label = ''
			
					if value_id not in label_list.keys():

						try:
				
							value_details = get_entity_dict_from_api(value_id)

						except:

							continue

						try:

							value_label = value_details['labels']['hi']['value']
			
							label_list[value_id] = value_label

						except:

							try:

								value_label = value_details['labels']['en']['value']

								label_list[value_id] = value_label

							except:

								continue
							

					if value_label != '' or value_id in label_list.keys():
			
						labelled.append(label_list[value_id])
			
				else:
			
					labelled.append(val['mainsnak']['datavalue']['value'])

		if labelled:

			person_labelled[label_list[prop]] = labelled

			#person_labelled['Title'] = WikidataItem(get_entity_dict_from_api(str(item))).get_label()

	label_person_list[get_entity_dict_from_api(str(item))['id']] = {'Hindi' : person_labelled, "English" : non_labelled}

	#all_english.append(non_labelled)

	#time.sleep(30)

	#print(count)

	#print(item)

	print(label_person_list)

	'''if count % 10 == 0:
	
		partition_num = str(count / 10).split('.')[0]

		with open('RA_OUTPUTS/1-6000person/hindi_keyvalue_pairs' + partition_num + '.json', 'w') as fout:

			json.dump(label_person_list, fout)

		label_person_list = {}

		print("Checkpoint %d reached \n" % (count / 10), end = ' ')

	#all_english.append(non_labelled)'''

'''for i in range(1501, 1721):

	with open('RA_OUTPUTS/15000_Finalperson/hindi_keyvalue_pairs' + str(i) + '.json', 'r') as fin:

		for line in fin:

			append.update(json.loads(line))

final_english_tobetrans = {}

for orig_key, value in append.items():

	final_english_tobetrans[orig_key] = {}

	for key, val in value['Hindi'].items():

		if key in value['English']:

			if len(val) == 1:

				#final_english_tobetrans[orig_key] = {}

				final_english_tobetrans[orig_key][key] = val

			else:

				final_english_tobetrans[orig_key][key] = list()

				#for i in range(len(val)):

				final_english_tobetrans[orig_key][key].extend(val)
						
x, y, result = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

for val in final_english_tobetrans.values():

	for key in list(val.keys()):

		try:

			val[key] = list(dict.fromkeys(val[key]))

		except:

			print(key)

			del(val[key])

			#delete.append(key)		

print(final_english_tobetrans)

for val in final_english_tobetrans.values():

	for key, value in val.items():

		if len(value) == 1:

			x = x.append([key])

			y = y.append([value[0]])

		else:

			x = x.append([key])

			y = y.append([value[0]])

			for i in range(1, len(value)):

				x = x.append(['Continued'])

				y = y.append([value[i]])

	x = x.append(['Next Entity'])

	y = y.append(['Next Entity'])

	result = pd.concat([x, y], axis=1)

result.to_excel('output_15000.xlsx')'''