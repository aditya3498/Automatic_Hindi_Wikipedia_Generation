import json, itertools

from collections import OrderedDict

count, flag_count, flag_count_1 = 0, 0, 0

with open('../Data/FinalData/FinalData_15000_Final/Cool/English_Translated_5.json', 'r') as fin:

	for line in fin:

		English_Pairs_Translated = json.loads(line)

for i in range(1501, 1721):

	English_Pairs_10 = dict(itertools.islice(English_Pairs_Translated.items(), (i - 1500) * 10))

	with open('Hindi_Key_Value_Pairs/hindi_keyvalue_pairs' + str(i) + '.json', 'r') as fin:

		for line in fin:

			Hindi_Pairs_Old = json.loads(line)

	for key, val in Hindi_Pairs_Old.items():

		#print(count)

		#flag = 0

		list_to_delete = []

		if len(val['English']) == 0:

			count += 1

			if count == 1131:

				count = 1130

			if count == 1162:

				count = 1161

			if count == 1268:

				count = 1267

			if count == 1308:

				count = 1307

			if count == 1762:

				count = 1761

			if count == 2056:

				count = 2055

			if count == 2104:

				count = 2103

		else:

			print(count)

			keycount, valuecount = 0, 0 

			for item in val['English']:

				flag = 0

				print(item)

				print(keycount)

				list_value_to_delete = []

				try:

					x = len(val['Hindi'][item])

				except:

					print("Item does not exist in Hindi Part of the Dictionary")

					flag = 1

					list_to_delete.append(item)

				print(list_to_delete)

				val['English'] = [x for x in val['English'] if x not in list_to_delete]

				#print(flag)

				if item not in English_Pairs_10[str(count)]['English_Key']:

					print("Item does not exist in English Translated List")

					continue

				if flag == 0 and len(val['Hindi'][item]) > 1 and keycount < len(English_Pairs_10[str(count)]['Hindi_Translation_Manual']):

					print("KEYCOUNT IS" + " " + str(keycount))

					new_key = English_Pairs_10[str(count)]['Hindi_Translation_Manual'][keycount]

					val['Hindi'][new_key] = val['Hindi'].pop(item)

					val['Hindi'][new_key][0] = English_Pairs_10[str(count)]['Hindi_Translation_Manual_1'][valuecount]

					valuecount += 1

					keycount += 1

					print("2")

					print(new_key)

					print(len(val['Hindi'][new_key]))

					for j in range(1, len(val['Hindi'][new_key])):

						try:

							new_val = English_Pairs_10[str(count)]['Hindi_Translation_Manual_1'][valuecount]

						except:

							print("List count differs in English List to Hindi List so delete from Hindi List")

							list_value_to_delete.append(val['Hindi'][new_key][j])

						else:

							val['Hindi'][new_key][j] = new_val

							valuecount += 1

							keycount += 1

					val['Hindi'][new_key] = [x for x in val['Hindi'][new_key] if x not in list_value_to_delete]

				elif flag == 0 and len(val['Hindi'][item]) <= 1 and keycount < len(English_Pairs_10[str(count)]['Hindi_Translation_Manual']):

					print("YO")

					if item in English_Pairs_10[str(count)]['English_Key']:

						new_key = English_Pairs_10[str(count)]['Hindi_Translation_Manual'][keycount]

						new_val = English_Pairs_10[str(count)]['Hindi_Translation_Manual_1'][valuecount]

						print("1")

						print(new_key)

						print(new_val)

						val['Hindi'][new_key] = val['Hindi'].pop(item)

						val['Hindi'][new_key][0] = new_val

						valuecount += 1

					keycount += 1

			count += 1

		print(val)

		print("\n")

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'w') as fout:

		json.dump(Hindi_Pairs_Old, fout)