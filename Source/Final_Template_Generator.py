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

	triple_pair_dict, double_pair_dict, single_pair_dict, triple_pair_dict_sentence_regex, double_pair_dict_sentence_regex, single_pair_dict_sentence_regex = {}, {}, {}, {}, {}, {}

	template_sentence = ""

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

	for key, val in list(triple_pair_dict_sentence_regex.items())[:10]:

		if key != "3_Key_5":

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

	list_keys_scientist = [key for key in template_data]

	for key, val in triple_pair_dict_sentence_regex.items():

		temp_scientist_list = []

		list_check = [x for x in val if x not in list_keys_scientist]

		#print(list_check)

		if not list_check:

			for i in range(0, len(val)):

				if len(template_data[val[i]]) <= 1:

					temp_scientist_list.append(template_data[val[i]][0])

				else:

					temp_scientist_list.append(template_data[val[i]])

			for i in range(0, len(temp_scientist_list)):

				if isinstance(temp_scientist_list[i], list):

					string_convert = ', '.join(temp_scientist_list[i][:-1]) + ' और ' + temp_scientist_list[i][-1]

					temp_scientist_list[i] = string_convert

			template_sentence = triple_pair_dict[key]

			print("triple")

			print(template_sentence)

			print("\n")

			print(temp_scientist_list)

			print("\n")

			'''for i in range(0, len(val)):

				template_sentence = re.sub(r'\{\{(.*?)\}\}', temp_scientist_list[i], template_sentence, count = 1)

			print(template_sentence)

			print("\n")'''

		else:

			list_after_triple_check = [x for x in val if x in list_keys_scientist]

			print(list_after_triple_check)

			if len(list_after_triple_check) == len(val) - 1:

				#print("X")

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

				for k, v in double_pair_dict_sentence_regex.items():

					if v == list_after_triple_check:

						print("YOOOO")

						template_sentence = double_pair_dict[k]

						break

				print("double")

				print(template_sentence)

				print("\n")

				print(temp_scientist_list)

				print("\n")

			else:

				pass					

template_creation_triple_first()