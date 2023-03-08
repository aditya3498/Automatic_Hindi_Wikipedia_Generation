import json, re

def import_all_data():
	
	finaldata_1_2500, finaldata_2500_6000, finaldata_10000_12500, finaldata_6000_10000, finaldata_12500_15000, finaldata_15000_Final = [], [], [], [], [], []

	with open('../Data/TemplateSentences/Template_Sentences_Triple_Pair_Sentences.json', 'r') as fin:

		for line in fin:

			triple_pair = json.loads(line)

	with open('../Data/TemplateSentences/Template_Sentences_Double_Pair_Sentences.json', 'r') as fin:

		for line in fin:

			double_pair = json.loads(line)

	with open('../Data/TemplateSentences/Template_Sentences_Single_Pair_Sentence.json', 'r') as fin:

		for line in fin:

			single_pair = json.loads(line)

	for i in range(1, 250):

		with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'r') as fin:

			for line in fin:

				finaldata_1_2500.append(json.loads(line))

	for i in range(251, 601):

		with open('../Data/FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'r') as fin:

			for line in fin:

				finaldata_2500_6000.append(json.loads(line))

	for i in range(601, 1001):

		with open('../Data/FinalData/FinalData_6000_10000/Cool' + str(i) + '.json', 'r') as fin:

			for line in fin:

				finaldata_6000_10000.append(json.loads(line))

	for i in range(1001, 1251):

		with open('../Data/FinalData/FinalData_10000_12500/Cool' + str(i) + '.json', 'r') as fin:

			for line in fin:

				finaldata_10000_12500.append(json.loads(line))

	for i in range(1251, 1501):

		with open('../Data/FinalData/FinalData_12500_15000/Cool' + str(i) + '.json', 'r') as fin:

			for line in fin:

				finaldata_12500_15000.append(json.loads(line))

	for i in range(1501, 1721):

		with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

			for line in fin:

				finaldata_15000_Final.append(json.loads(line))

	return triple_pair, double_pair, single_pair, finaldata_1_2500, finaldata_2500_6000, finaldata_6000_10000, finaldata_10000_12500, finaldata_12500_15000, finaldata_15000_Final

def get_data_from_name():

	triple_pair, double_pair, single_pair, finaldata_1_2500, finaldata_2500_6000, finaldata_6000_10000, finaldata_10000_12500, finaldata_12500_15000, finaldata_15000_Final = import_all_data()

	string_input = input("Enter the Scientist for which Hindi Wiki Page is to be created\n")

	template_data = []

	for sets in finaldata_1_2500:

		if string_input in sets.keys():

			template_data = sets[string_input]

			break

	for sets in finaldata_2500_6000:

		if string_input in sets.keys():

			template_data = sets[string_input]

			break

	for sets in finaldata_6000_10000:

		if string_input in sets.keys():

			template_data = sets[string_input]

			break

	for sets in finaldata_10000_12500:

		if string_input in sets.keys():

			template_data = sets[string_input]

			break

	for sets in finaldata_12500_15000:

		if string_input in sets.keys():

			template_data = sets[string_input]

			break

	for sets in finaldata_15000_Final:

		if string_input in sets.keys():

			template_data = sets[string_input]

			break	

	return template_data

def template_creation_triple_first():

	triple_pair, double_pair, single_pair, finaldata_1_2500, finaldata_2500_6000, finaldata_6000_10000, finaldata_10000_12500, finaldata_12500_15000, finaldata_15000_Final = import_all_data()

	template_data = get_data_from_name()

	template_data_remaining_keys = []

	triple_pair_dict, double_pair_dict, single_pair_dict, triple_pair_dict_sentence_regex, double_pair_dict_sentence_regex, single_pair_dict_sentence_regex = {}, {}, {}, {}, {}, {}

	template_sentence, template = "", ""

	count = 1

	for sentence in triple_pair:

		keys = re.findall(r'\{\{(.*?)\}\}', sentence)

		triple_pair_dict["3_Key" + '_' + str(count)] = sentence

		triple_pair_dict_sentence_regex["3_Key" + '_' + str(count)] = keys

		count += 1

	count = 1

	for sentence in double_pair:

		keys = re.findall(r'\{\{(.*?)\}\}', sentence)

		double_pair_dict[count] = sentence

		double_pair_dict_sentence_regex[count] = keys

		count += 1

	count = 1

	for sentence in single_pair:

		keys = re.findall(r'\{\{(.*?)\}\}', sentence)

		single_pair_dict[count] = sentence

		single_pair_dict_sentence_regex[count] = keys

		count += 1

	for key, val in list(triple_pair_dict_sentence_regex.items()):

		if key != "3_Key_5" or key != "3_Key_3" or key != "3_Key_4":

			count = 1

			for i in range(1, len(val)):

				for j in range(i + 1, len(val)):

					if key == "3_Key_2":

						val.insert(0, val.pop(val.index("Scientist")))

					list_temp = [val[0], val[i], val[j]]

					for keys, values in list(double_pair_dict_sentence_regex.items()):

						if key == "3_Key_2" and "Scientist" in list_temp:
	 
							list_temp.remove("Scientist")

						if set(list_temp) == set(values):

							double_pair_dict_sentence_regex[key + '_2_Key_' + str(count)] = double_pair_dict_sentence_regex.pop(keys)

							count += 1

							break

	for key, val in list(triple_pair_dict_sentence_regex.items())[2:4]:

		count = 1

		for i in range(0, len(val)):

			for j in range(i + 1, len(val)):

				for k in range(j + 1, len(val)):

					list_temp = [val[0], val[i], val[j], val[k]]

					for keys, values in list(double_pair_dict_sentence_regex.items()):

						if set(list_temp) == set(values):

							double_pair_dict_sentence_regex[key + '_2_Key_' + str(count)] = double_pair_dict_sentence_regex.pop(keys)

							count += 1

							break

	for key, val in list(triple_pair_dict_sentence_regex.items())[4:5]:

		count = 1

		for i in range(0, len(val)):

			for j in range(i + 1, len(val)):

				list_temp = [val[i], val[j]]

				for keys, values in list(double_pair_dict_sentence_regex.items()):

					if set(list_temp) == set(values):

						double_pair_dict_sentence_regex[key + '_2_Key_' + str(count)] = double_pair_dict_sentence_regex.pop(keys)

						count += 1

						break

	for key, val in list(double_pair_dict.items()):

		keys = re.findall(r'\{\{(.*?)\}\}', val)

		for k, values in double_pair_dict_sentence_regex.items():

			if keys == values:

				double_pair_dict[k] = double_pair_dict.pop(key)

	print(triple_pair_dict_sentence_regex)

	print("\n")

	print(triple_pair_dict)

	print("\n")

	print(double_pair_dict)

	print("\n")

	print(double_pair_dict_sentence_regex)

	print("\n")

	temp_to_remove = []

	if 'पुरस्कार प्राप्त' in template_data.keys():

		template_data['Reason'] = {}

		for item in template_data['पुरस्कार प्राप्त']:

			if isinstance(item, dict):

				for k, v in item.items():

					template_data['Reason'][k] = v

	if 'Reason' in template_data.keys():

		for k, v in template_data['Reason'].items():

			for item in template_data['पुरस्कार प्राप्त']:

				if isinstance(item, dict):

					for key in item.keys():

						if k == key:

							template_data['पुरस्कार प्राप्त'].append(k)

	if 'पुरस्कार प्राप्त' in template_data.keys():

		for item in template_data['पुरस्कार प्राप्त']:

			if isinstance(item, dict):

				temp_to_remove.append(item)

	try:

		template_data['पुरस्कार प्राप्त'] = [x for x in template_data['पुरस्कार प्राप्त'] if x not in temp_to_remove]

	except:

		pass

	print(template_data)

	print("\n")

	list_keys_scientist = [key for key in template_data]

	template_data_remaining_keys = list_keys_scientist

	for key, val in triple_pair_dict_sentence_regex.items():

		temp_scientist_list = []

		list_check = [x for x in val if x not in list_keys_scientist]

		if key == "3_Key_4":

			continue

		print(key, val)

		if not list_check:

			template_data_remaining_keys = list(set(template_data_remaining_keys) - set(val))

			for i in range(0, len(val)):

				if len(template_data[val[i]]) <= 1:

					temp_scientist_list.append(template_data[val[i]][0])

				else:

					temp_scientist_list.append(template_data[val[i]])

			#print(temp_scientist_list)

			for i in range(0, len(temp_scientist_list)):

				if isinstance(temp_scientist_list[i], list):

					string_convert = ', '.join(temp_scientist_list[i][:-1]) + ' और ' + temp_scientist_list[i][-1]

					temp_scientist_list[i] = string_convert

			template_sentence = triple_pair_dict[key]

			print("\ntriple\n")

			#print("Template Sentence : ", template_sentence)

			print(temp_scientist_list)

			print("\n")

			for i in range(0, len(val)):

				template_sentence = re.sub(r'\{\{(.*?)\}\}', temp_scientist_list[i], template_sentence, count = 1)

			template += str(" ") + template_sentence

			print("Template Sentence:", template_sentence)

			print("\n")

			print("Final Template Combined:", template)

			print("\n")

		else:

			list_after_triple_check = [x for x in val if x in list_keys_scientist]

			if len(list_after_triple_check) == len(val) - 1:

				template_data_remaining_keys = list(set(template_data_remaining_keys) - set(val))

				print("YO", list_after_triple_check)

				for i in range(0, len(list_after_triple_check)):

					if len(template_data[list_after_triple_check[i]]) <= 1:

						temp_scientist_list.append(template_data[list_after_triple_check[i]][0])

					else:

						temp_scientist_list.append(template_data[list_after_triple_check[i]])

				for i in range(0, len(temp_scientist_list)):

					if isinstance(temp_scientist_list[i], list):

						string_convert = ', '.join(temp_scientist_list[i][:-1]) + ' और ' + temp_scientist_list[i][-1]

						temp_scientist_list[i] = string_convert

				if key == "3_Key_2":

					list_after_triple_check.remove('Scientist')

					temp_scientist_list.pop(0)

				list_temp = []

				'''if len(list_after_triple_check) == 4:

					for i in range(1, 4):

						for j in range(i + 1, 4):

							list_temp = [list_after_triple_check[0], list_after_triple_check[i], list_after_triple_check[j]]

							for k, v in double_pair_dict_sentence_regex.items():

								if list_temp == v:

									print("SRSLY")

									template_sentence = double_pair_dict[k]

									break'''

				for k, v in double_pair_dict_sentence_regex.items():

					if v == list_after_triple_check:

						print(k)

						print("YOOOO")

						template_sentence = double_pair_dict[k]

						break

				print("\ndouble\n")

				#print("Template Sentence :", template_sentence)

				for i in range(len(list_after_triple_check)):

					template_sentence = re.sub(r'\{\{(.*?)\}\}', temp_scientist_list[i], template_sentence, count = 1)

				template += str(" ") + template_sentence

				print(template_sentence)

				print("\n")

				print(template)

				print("\n")

			else:

				if 'Scientist' in list_after_triple_check:

					list_after_triple_check.remove('Scientist')

				if len(list_after_triple_check) == 0:

					print("KEYS NOT AVAILABLE FOR PRESENT SCIENTIST\n")

					continue

				template_data_remaining_keys = list(set(template_data_remaining_keys) - set(val))

				for i in range(len(list_after_triple_check)):

					if len(template_data[list_after_triple_check[i]]) <= 1:

						temp_scientist_list.append(template_data[list_after_triple_check[i]][0])

					else:

						temp_scientist_list.append(template_data[list_after_triple_check[i]])

				for i in range(len(temp_scientist_list)):

					if isinstance(temp_scientist_list[i], list):

						string_convert = ', '.join(temp_scientist_list[i][:-1]) + ' और ' + temp_scientist_list[i][-1]

						temp_scientist_list[i] = string_convert

				print(temp_scientist_list)

				print(list_after_triple_check)

				print("SINGLE")

				print("\n")

	#print(list_temp)

	#print(temp_scientist_list)

	for key, val in triple_pair_dict_sentence_regex.items():

		temp_scientist_list = []

		if key == "3_Key_4":

			reason, prize = [], []

			print(key, val)

			list_check = [x for x in val if x not in list_keys_scientist]

			if not list_check:

				template_data_remaining_keys = list(set(template_data_remaining_keys) - set(val))

				if len(template_data['Reason']) <= 1:

					reason_insert = template_data['Reason'][list(template_data['Reason'].keys())[0]]

					prize_insert = list(template_data['Reason'].keys())[0]

					template_data['पुरस्कार प्राप्त'].remove(prize_insert)

					if len(template_data['पुरस्कार प्राप्त']) > 1:

						string_convert = ', '.join(template_data['पुरस्कार प्राप्त'][:-1]) + ' और ' + template_data['पुरस्कार प्राप्त'][-1]

					else:

						string_convert = template_data['पुरस्कार प्राप्त'][0]

					temp_scientist_list = [template_data['Scientist'][0], reason_insert, prize_insert, string_convert]
					
					print(temp_scientist_list)

					print("\n")

					template_sentence = triple_pair_dict[key]

					for i in range(len(temp_scientist_list)):

						template_sentence = re.sub(r'\{\{(.*?)\}\}', temp_scientist_list[i], template_sentence, count = 1)

					template += str(" ") + template_sentence

					print("Template Sentence:", template_sentence)

					print("\n")

					print("Final Template :", template)

					print("\n")

				else:

					for k, v in template_data['Reason'].items():

						reason.append(v)

						prize.append(k)

						template_data['पुरस्कार प्राप्त'].remove(k)

					if len(template_data['पुरस्कार प्राप्त']) > 1:

						string_convert = ', '.join(template_data['पुरस्कार प्राप्त'][:-1]) + ' और ' + template_data['पुरस्कार प्राप्त'][-1]

					else:

						string_convert = template_data['पुरस्कार प्राप्त'][0]

					reason_insert = ', '.join(reason[:-1]) + ' एवं ' + reason[-1]

					prize_insert = ', '.join(prize[:-1]) + ' एवं ' + prize[-1]

					temp_scientist_list = [template_data['Scientist'][0], reason_insert, prize_insert, string_convert]

					print(temp_scientist_list)

					print("\n")

					template_sentence = triple_pair_dict[key]

					for i in range(len(temp_scientist_list)):

						template_sentence = re.sub(r'\{\{(.*?)\}\}', temp_scientist_list[i], template_sentence, count = 1)

					template += str(" ") + template_sentence

					print("Template Sentence:", template_sentence)

					print("\n")

					print("Final Template :", template)

					print("\n")

			else:

				list_after_check = [x for x in val if x in list_keys_scientist]

				if len(list_after_check) == len(val) - 1:

					template_data_remaining_keys = list(set(template_data_remaining_keys) - set(val))

					if 'Reason' in list_after_check:

						if len(template_data['Reason']) <= 1:

							reason_insert = template_data['Reason'][list(template_data['Reason'].keys())[0]]

							prize_insert = list(template_data['Reason'].keys())[0]

							template_data['पुरस्कार प्राप्त'].remove(prize_insert)

							if len(template_data['पुरस्कार प्राप्त']) > 1:

								string_convert = ', '.join(template_data['पुरस्कार प्राप्त'][:-1]) + ' और ' + template_data['पुरस्कार प्राप्त'][-1]

							else:

								string_convert = template_data['पुरस्कार प्राप्त'][0]

							temp_scientist_list = [template_data['Scientist'][0], reason_insert, prize_insert, string_convert]
					
							print(temp_scientist_list)

							print("\n")

							for k, v in double_pair_dict_sentence_regex.items():

								if v == list_after_check:

									template_sentence = double_pair_dict[k]

									break

							for i in range(len(temp_scientist_list)):

								template_sentence = re.sub(r'\{\{(.*?)\}\}', temp_scientist_list[i], template_sentence, count = 1)

							template += str(" ") + template_sentence

							print("Template Sentence Reason:", template_sentence)

							print("\n")

							print("Final Template :", template)

							print("\n")

						else:

							for k, v in template_data['Reason'].items():

								reason.append(v)

								prize.append(k)

								template_data['पुरस्कार प्राप्त'].remove(k)

							if len(template_data['पुरस्कार प्राप्त']) > 1:

								string_convert = ', '.join(template_data['पुरस्कार प्राप्त'][:-1]) + ' और ' + template_data['पुरस्कार प्राप्त'][-1]

							else:

								string_convert = template_data['पुरस्कार प्राप्त'][0]

							reason_insert = ', '.join(reason[:-1]) + ' एवं ' + reason[-1]

							prize_insert = ', '.join(prize[:-1]) + ' एवं ' + prize[-1]

							temp_scientist_list = [template_data['Scientist'][0], reason_insert, prize_insert, string_convert]

							print(temp_scientist_list)

							print("\n")

							for k, v in double_pair_dict_sentence_regex.items():

								if v == list_after_check:

									template_sentence = double_pair_dict[k]

									break

							for i in range(len(temp_scientist_list)):

								template_sentence = re.sub(r'\{\{(.*?)\}\}', temp_scientist_list[i], template_sentence, count = 1)

							template += str(" ") + template_sentence

							print("Template Sentence REASON:", template_sentence)

							print("\n")

							print("Final Template :", template)

	print("\n")

	print(template_data_remaining_keys)	

	print("\n")	

	print(single_pair_dict_sentence_regex)

	print("\n")

	print(single_pair_dict)			

template_creation_triple_first()