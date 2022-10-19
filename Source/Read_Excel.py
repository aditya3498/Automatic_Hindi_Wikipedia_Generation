import pandas as pd

import json

import itertools

df = pd.read_excel('Final_Output_6000.xlsx', sheet_name = 'Final_Output(1-2500)', header = 8, skipfooter = 1, usecols = "A, C, E, F")

df_dict = df.T.to_dict()

final_dict = {}

list_next_entity = []

count, start, end, counter = -1, -1, 0, 0

for key, val in df_dict.items():

	count += 1

	if val['English Key '] == 'Next Entity':

		list_next_entity.append(count)

print(len(list_next_entity))

for i in range(0, len(list_next_entity)):

	end = list_next_entity[i]

	if end == start + 1:

		final_dict[counter] = {}

		final_dict[counter]['English_Key'] = ['Next Entity']

		final_dict[counter]['Hindi_Translation_Manual'] = ['Next Entity']

		final_dict[counter]['English_Value'] = ['Next Entity']

		final_dict[counter]['Hindi_Translation_Manual_1'] = ['Next Entity']

		counter += 1

		start = end

	else:

		final_dict[counter] = {}

		final_dict[counter]['English_Key'] = list()

		final_dict[counter]['Hindi_Translation_Manual'] = list()

		final_dict[counter]['English_Value'] = list()

		final_dict[counter]['Hindi_Translation_Manual_1'] = list()

		for j in range(start + 1, end):

			final_dict[counter]['English_Key'] += [df_dict[int(j)]['English Key ']]

			if df_dict[int(j)]['English Key '] == "Continued":	

				final_dict[counter]['Hindi_Translation_Manual'] += [str(df_dict[int(j)]['Hindi_Translation_Manual'])]

			else:

				final_dict[counter]['Hindi_Translation_Manual'] += [df_dict[int(j)]['Hindi_Translation_Manual']]

			final_dict[counter]['English_Value'] += [df_dict[int(j)]['English Value']]

			if pd.isna(df_dict[int(j)]['Hindi_Translation_Manual.1']):

				final_dict[counter]['Hindi_Translation_Manual_1'] += [str(df_dict[int(j)]['Hindi_Translation_Manual.1'])]

			else:

				final_dict[counter]['Hindi_Translation_Manual_1'] += [df_dict[int(j)]['Hindi_Translation_Manual.1']]

		counter += 1

		start = end

with open('English_Translated.json', 'w') as fout:

	json.dump(final_dict, fout)
