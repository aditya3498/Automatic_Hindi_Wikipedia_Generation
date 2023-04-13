import json

for i in range(251, 601):

	with open('../Data/FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			template_data = json.loads(line)

	for k, v in template_data.items():

		if 'बच्चों की संख्या' in v.keys():

			try:

				value = v['बच्चों की संख्या'][0]['राशि'][-1]

				v.update({'बच्चों की संख्या' : [value]})

			except:

				print(i)

				print(k, v)

	#with open('../Data/FinalData/FinalData_2500_6000/Cool' + str(i) + '.json', 'w') as fout:

		#json.dump(template_data, fout)