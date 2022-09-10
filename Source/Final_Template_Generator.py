import json

with open('../Data/TemplateSentences/Template_Sentences_Triple_Pair_Sentences.json', 'r') as fin:

	for line in fin:

		triple_pair = json.loads(line)

with open('../Data/TemplateSentences/Template_Sentences_Double_Pair_Sentences.json', 'r') as fin:

	for line in fin:

		double_pair = json.loads(line)

with open('../Data/TemplateSentences/Template_Sentences_Single_Pair_Sentence.json', 'r') as fin:

	for line in fin:

		single_pair = json.loads(line)

with open('../Data/FinalData/FinalData_1_2500/Cool1.json', 'r') as fin:

	for line in fin:

		finaldata = json.loads(line)

print(triple_pair)

def triple_double_single():

	for sentence in triple_pair: