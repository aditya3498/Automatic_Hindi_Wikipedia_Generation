import json

from alphabet_detector import AlphabetDetector

ad = AlphabetDetector()

from anuvaad import Anuvaad

anu = Anuvaad('english-hindi')

for i in range(1, 250):

	finaldata = {}

	with open('RA_OUTPUTS/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			data = json.loads(line)

	for val in data.values():

		for key, value in val['Hindi'].items():

			if key == "पुरस्कार प्राप्त":

				if len(value) > 1:

					for j in range(0, len(value)):

						if isinstance(value[j], dict):

							new_dict = {}

							for k, v in value[j].items():

								if k != "Copley Medal":

									if ad.only_alphabet_chars(str(k), "LATIN"):

										text = anu.anuvaad(k)

										k = text

									text_value = anu.anuvaad(v)

									v = text_value

									new_dict[k] = v

								else:

									text_value = anu.anuvaad(v)

									v = text_value

									new_dict[k] = v

							value[j] = new_dict

						else:

							if ad.only_alphabet_chars(str(value[j]), "LATIN"):

								text = anu.anuvaad(value[j])

								value[j] = text

				else:

					if ad.only_alphabet_chars(str(value[0]), "LATIN"):

						text = anu.anuvaad(value[0])

						value[0] = text

			else:

				if len(value) > 1:

					for j in range(0, len(value)):

						if isinstance(value[j], dict):

							temp_dict = {}

							for k, v in value[j].items():

								if ad.only_alphabet_chars(str(k), "LATIN"):

									text = anu.anuvaad(k)

									k = text

								text_value = anu.anuvaad(v)

								v = text_value

								temp_dict[k] = v

							value[j] = temp_dict

						else:

							if ad.only_alphabet_chars(str(value[j]), "LATIN"):

								text = anu.anuvaad(str(value[j]))

								value[j] = text

				else:

					if isinstance(value[0], dict):

						temp_dict = {}

						for k, v in value[0].items():

							if ad.only_alphabet_chars(str(k), "LATIN"):

								text = anu.anuvaad(k)

								k = text

							text_value = anu.anuvaad(v)

							v = text_value

							temp_dict[k] = v

						value[0] = temp_dict

					else:

						if ad.only_alphabet_chars(str(value[0]), "LATIN"):

							text = anu.anuvaad(value[0])

							value[0] = text

	for val in data.values():

		list_delete = [key for key in val if key == 'English']

		for key in list_delete:

			del val[key]

	for key, val in data.items():

		hindi_content_dict = val['Hindi']

		finaldata[key] = hindi_content_dict

	print(i)

	print(finaldata)

	print("\n")

	with open('RA_OUTPUTS/FinalData/FinalData_1_2500/Cool_Temp' + str(i) + '.json', 'w') as fout:

		json.dump(finaldata, fout)
