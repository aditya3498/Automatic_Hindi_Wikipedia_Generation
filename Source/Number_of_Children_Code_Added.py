import json

template_data = []

for i in range(1, 250):

	with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			template_data.append(json.loads(line))

for item in template_data:

	for k, v in item.items():

		if 'बच्चों की संख्या' in v.keys():

			value = v['बच्चों की संख्या'][0]['राशि'][-1]

			v.update({'बच्चों की संख्या' : [value]})

for i in range(1, 250):

	with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'w') as fout:

		json.dump(template_data, fout)