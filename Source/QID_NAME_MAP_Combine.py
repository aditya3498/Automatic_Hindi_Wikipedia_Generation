import json 

with open('../QID_MAP/QID_NAME_MAP333.json', 'r') as fin:

	for line in fin:

		data = json.loads(line)

data['Q6681655'] = 'Lorraine Lisiecki'

data['Q6763142'] = 'Hussein Hamid'

data['Q12755420'] = 'Milorad Pavlović'

data['Q7331943'] = 'Rickey B. Cotton'

data['Q6763142'] = 'Hussein Hamid'

with open('../QID_MAP/QID_NAME_MAP333.json', 'w') as fout:

	json.dump(data, fout)