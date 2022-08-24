import json

alive_status_added = []

for i in range(1, 2):

	with open('../Data/FinalData/FinalData_1_2500/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			alive_status_added = json.loads(line)

		for key, val in alive_status_added.items():

			try:

				dob = val['Hindi']['मृत्यु तिथि']

				val['Hindi']['alivestatus/wgok'] = ['थी', 'था']

				if val['Hindi']['लिंग'][0] == 'महिला':

					val['Hindi']['alivestatus/wgop'] = ['थी']

					val['Hindi']['हुए/हुई'] = ['हुई']

					val['Hindi']['के/की'] = ['की']

					val['Hindi']['रखती/रखते'] = ['रखती']

				else:

					val['Hindi']['alivestatus/wgop'] = ['थे']

					val['Hindi']['के/की'] = ['के']

					val['Hindi']['हुए/हुई'] = ['हुए']

					val['Hindi']['रखती/रखते'] = ['रखते']

			except:

				val['Hindi']['alivestatus'] = ['है']

				val['Hindi']['alivestatus/wgop'] = ['है']

				val['Hindi']['alivestatus/wogop'] = ['है']

				if val['Hindi']['लिंग'][0] == 'महिला':

					val['Hindi']['हुए/हुई'] = ['हुई']

					val['Hindi']['रखती/रखते'] = ['रखती']

					val['Hindi']['के/की'] = ['की']

				else:

					val['Hindi']['हुए/हुई'] = ['हुए']

					val['Hindi']['रखती/रखते'] = ['रखते']

					val['Hindi']['के/की'] = ['के']

			print(key, val)

			print("\n")