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

			template_data = sets[string_input]['Hindi']

			break

	for sets in finaldata_2500_6000:

		if string_input in sets.keys():

			template_data = sets[string_input]['Hindi']

			break

	for sets in finaldata_6000_10000:

		if string_input in sets.keys():

			template_data = sets[string_input]['Hindi']

			break

	for sets in finaldata_10000_12500:

		if string_input in sets.keys():

			template_data = sets[string_input]['Hindi']

			break

	for sets in finaldata_12500_15000:

		if string_input in sets.keys():

			template_data = sets[string_input]['Hindi']

			break

	for sets in finaldata_15000_Final:

		if string_input in sets.keys():

			template_data = sets[string_input]['Hindi']

			break	

	return template_data

def template_creation_single_third():

	return 0

def template_creation_double_second():

	return 0

def template_creation_triple_first():

	triple_pair, double_pair, single_pair, finaldata_1_2500, finaldata_2500_6000, finaldata_6000_10000, finaldata_10000_12500, finaldata_12500_15000, finaldata_15000_Final = import_all_data()

	template_data = get_data_from_name()

	triple_pair_dict, triple_pair_dict_sentence_regex = {}, {}

	count = 1

	for sentence in triple_pair:

		keys = re.findall(r'\{\{(.*?)\}\}', sentence)

		triple_pair_dict[count] = sentence

		triple_pair_dict_sentence_regex[count] = keys

		count += 1

	print(triple_pair_dict)

	print(triple_pair_dict_sentence_regex)

	print(template_data)

	list_keys_scientist = [key for key in template_data]

	for key, val in triple_pair_dict_sentence_regex.items():

		temp_scientist_list = []

		list_check = [x for x in val if x not in list_keys_scientist]

		if not list_check:

			for i in range(0, len(val)):

				if len(template_data[val[i]]) <= 1:

					temp_scientist_list.append(template_data[val[i]][0])

				else:

					temp_scientist_list.append(template_data[val[i]])

		print(temp_scientist_list)

		print(key, val)

template_creation_triple_first()