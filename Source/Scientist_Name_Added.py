import json

for i in range(1501, 1721):

    with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

        for line in fin:

            finaldata = json.loads(line)

    for key, val in finaldata.items():

        val['Hindi']['Scientist'] = str(key)

    with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'w') as fout:

        json.dump(finaldata, fout)