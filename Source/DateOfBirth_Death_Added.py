from datetime import date

import json

finaldata = []

def month_to_text(month):

	switcher = {

		1 : "January",
		2 : "February",
		3 : "March",
		4 : "April",
		5 : "May",
		6 : "June",
		7 : "July",
		8 : "August",
		9 : "September",
		10 : "October",
		11 : "November",
		12 : "December"
	}

	return switcher.get(month, "N/A")

for i in range(1, 250):

	with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			finaldata = json.loads(line)

	for key, val in finaldata.items():

		for k, value in val.items():

			if k == 'जन्म तिथि':

				try:

					dob = value['time'][1:11].split('-')

					if int(dob[1]) == 0 and int(dob[2]) == 0:

						final_dob = date(int(dob[0]), 1, 1)

						val.update({k : [str(final_dob.year)]})

					elif int(dob[2]) == 0 and int(dob[1]) != 0:

						final_dob = date(int(dob[0]), int(dob[1]), 1)

						dob_text_final = month_to_text(final_dob.month) + " " + str(final_dob.year)

						val.update({k : [dob_text_final]})

					else:

						final_dob = date(int(dob[0]), int(dob[1]), int(dob[2]))

						dob_text_final = str(final_dob.day) + " " + month_to_text(final_dob.month) + " " + str(final_dob.year)

						val.update({k : [dob_text_final]})

				except:

					print(i)	

					print("DOB")

					print(key, val)

					print(k, value)

			if k == 'मृत्यु तिथि':

				try:

					dob = value['time'][1:11].split('-')

					if int(dob[1]) == 0 and int(dob[2]) == 0:

						final_dob = date(int(dob[0]), 1, 1)

						val.update({k : [str(final_dob.year)]})

					elif int(dob[2]) == 0 and int(dob[1]) != 0:

						final_dob = date(int(dob[0]), int(dob[1]), 1)

						dob_text_final = month_to_text(final_dob.month) + " " + str(final_dob.year)

						val.update({k : [dob_text_final]})

					else:

						final_dob = date(int(dob[0]), int(dob[1]), int(dob[2]))

						dob_text_final = str(final_dob.day) + " " + month_to_text(final_dob.month) + " " + str(final_dob.year)

						val.update({k : [dob_text_final]})

				except:

					print("DOD")

					print(key, val)

					print(k, value)

	#print(finaldata)

	#with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'w') as fout:

	#	json.dump(finaldata, fout)