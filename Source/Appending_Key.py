import json 

with open('../Data/FinalData/FinalData_2500_6000/Cool511.json', 'r') as fin:

	for line in fin:

		data = json.loads(line)

for k, v in data.items():

	if k == "Sung Il Roh":

		v['Hindi']['QID'] = "Q10856200"

with open('../Data/FinalData/FinalData_2500_6000/Cool511.json', 'w') as fout:

	json.dump(data, fout)