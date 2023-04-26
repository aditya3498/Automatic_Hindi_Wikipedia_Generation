import json

from anuvaad import Anuvaad

anu = Anuvaad('english-hindi')

for i in range(1, 250):

	with open('./Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			template_data = json.loads(line)

	for k, v in template_data.items():

		if 'बच्चों की संख्या' in v.keys():

			temp_dict, new_dict = {}, {}

			temp_dict['बच्चों की संख्या'] = {}

			temp_dict['बच्चों की संख्या']['amount'] = template_data[k]['बच्चों की संख्या']['amount']

			v.update({list(temp_dict.keys())[0] : temp_dict['बच्चों की संख्या']})

			text_translate = anu.anuvaad(list(template_data[k]['बच्चों की संख्या'].keys())[0])

			new_dict[text_translate] = template_data[k]['बच्चों की संख्या']['amount']

			v.update({list(temp_dict.keys())[0] : new_dict})

			#print(template_data[k])

			value = v['बच्चों की संख्या']['राशि'][-1]

			v.update({'बच्चों की संख्या' : [value]})

			print(template_data[k])

			#print(template_data[k])

	#with open('./Cool' + str(i) + '.json', 'w') as fout:

	#	json.dump(template_data, fout)