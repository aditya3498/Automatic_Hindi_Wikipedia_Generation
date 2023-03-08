import json

a, b, c = [], [], []

with open('../Data/TemplateSentences/Template_Sentences_Single_Pair_Sentence.json', 'r') as fin:

	for line in fin:

		x = json.loads(line)

with open('../Data/TemplateSentences/Template_Sentences_Triple_Pair_Sentences.json', 'r') as fin:

	for line in fin:

		y = json.loads(line)

with open('../Data/TemplateSentences/Template_Sentences_Double_Pair_Sentences.json', 'r') as fin:

	for line in fin:

		z = json.loads(line)

for item in x:

	if item[-1] != '|':

		item += ' |'

	a.append(item)

for item in y:

	if item[-1] != '|':

		item += ' |'

	b.append(item)

for item in z:

	if item[-1] != '|':

		item += ' |'

	c.append(item)

with open('../Data/TemplateSentences/Template_Sentences_Single_Pair_Sentence.json', 'w') as fout:

	json.dump(a, fout)

with open('../Data/TemplateSentences/Template_Sentences_Double_Pair_Sentences.json', 'w') as fout:

	json.dump(c, fout)

with open('../Data/TemplateSentences/Template_Sentences_Triple_Pair_Sentences.json', 'w') as fout:

	json.dump(b, fout)