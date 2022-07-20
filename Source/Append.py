import json

from collections import OrderedDict

append, really = {}, {}

list_remove = ["social media followers", "oral history at", "CANTIC ID (old)", "PAN member", "academic appointment", "alternate names", "chairperson", "CNRS Talent page", "College de France professor ID (1909-1939)", "commander of (DEPRECATED)", "Consolidated code of the electronic catalog of libraries of Belarus", "copyright representative", "GEPRIS-Historisch ID (Person)", "GitHub username", "Google Play Music artist ID (former scheme)", "GUI number", "Hacker News username", "has written for", "heritage designation", "inspired by", "instrument", "Lattes Platform number", "LIGA profile", "McCune-Reischauer romanization", "Medium username", "member of military unit", "official blog", "parliamentary group", "Revised Romanization", "Scandinavian middle family name", "Skype username", "social classification", "special rank", "student register of the University of Helsinki ID (1853–1899)", "student register of the University of Helsinki ID (1640–1852)", "subject has role", "test taken", "website account on", "Wikimedia username", "Apple Music artist ID (US version)", "Artists in Canada record number", "studied by", "depicted by", "patient of", "sponsor", "astronaut mission", "PAN member", "professorship", "consecrator", "honorific prefix", "described at URL", "ResearcherID", "Library of Congress Classification", "Colon Classification", "canonization status", "feast day", "archival creator authority record at the Archives nationales", "RIA Novosti reference", "instrument", "Royal Academy new identifier", "SVT Open archive", "time period", "spoken text audio", "culture", "Nupill Literatura Digital - Author", "NLC authorities", "audio recording of the subject's spoken voice", "parliament.uk biography pages", "UK Parliament identifier", "candidacy in election", "amateur radio callsign", "Instagram username", "partner in business or sport", "diocese", "test taken", "owner of", "facial hair", "DOI", "Academia.edu profile URL", "VK username", "Baltisches Biographisches Lexikon digital ID (former scheme)", "Tumblr username", "NSDAP membership number (1925–1945)", "presenter", "title of chess person", "country for sport", "PhilPeople profile", "patronym or matronym for this person", "Québec cultural heritage directory people identifier", "penalty", "e-mail address", "website account on", "IPI name number", "related image"]

list_remove_final = list(set(list_remove))

for i in range(1, 340):

	with open('hindi_keyvalue_pairs' + str(i) + '.json', 'r') as fin:

		for line in fin:

			append = json.loads(line)

	for key, value in append.items():

		for key_hindi in list(value['Hindi'].keys()):

			if key_hindi in list_remove_final:

				del(value['Hindi'][key_hindi])

		final_list = [x for x in value['English'] if x not in list_remove_final]

		value['English'] = final_list

	'''for key, value in append.items():

		for key_hindi, val in value['Hindi'].items():

			if key_hindi not in value['English']:

				for j in range(len(val)):

					val[j] = anu.anuvaad(val[j])'''

	#print(append)

	with open('hindi_keyvalue_pairs' + str(i) + '.json', 'w') as fout:

		json.dump(append, fout)
