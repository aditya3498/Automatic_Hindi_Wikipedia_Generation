from Final_Template_Generator import import_all_data, get_data_from_name

finaldata_1_2500, finaldata_2500_6000, finaldata_10000_12500, finaldata_6000_10000, finaldata_12500_15000, finaldata_15000_Final, template_data = [], [], [], [], [], [], []

triple_pair, double_pair, single_pair, finaldata_1_2500, finaldata_2500_6000, finaldata_6000_10000, finaldata_10000_12500, finaldata_12500_15000, finaldata_15000_Final = import_all_data()

for item in finaldata_1_2500:

	template_data.append(item)

for item in template_data:

	for k, v in item.items():

		temp_to_remove = []

		if 'पुरस्कार प्राप्त' in v.keys():

			v['Reason'] = {}

			for items in v['पुरस्कार प्राप्त']:

				if isinstance(items, dict):

					for key, value in items.items():

						v['Reason'][key] = value

		#print(k, v)

		if 'Reason' in v.keys():

			for key, value in v['Reason'].items():

				for items in v['पुरस्कार प्राप्त']:

					if isinstance(items, dict):

						for keys in items.keys():

							if key == keys:

								v['पुरस्कार प्राप्त'].append(key)

			#print(k, v)

		if 'पुरस्कार प्राप्त' in v.keys():

			for items in v['पुरस्कार प्राप्त']:

				if isinstance(items, dict):

					temp_to_remove.append(items)

		try:

			v['पुरस्कार प्राप्त'] = [x for x in v['पुरस्कार प्राप्त'] if x not in temp_to_remove]

		except:

			pass

count, flag = 0, False

for item in template_data[:100]:

	count += 1

	#print(item)

	for key, val in item.items():

		if 'बच्चों की संख्या' in val.keys():

			#if len(val['Reason']) == 0 and 'नामांकित किया गया' in val.keys():

			flag = True

			print(count)

			print(key, val)