import json

for i in range(1501, 1721):

	keys_delete = []

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			alive_status_added = json.loads(line)

	for key, val in alive_status_added.items():

		try:

			dob = val['Hindi']['मृत्यु तिथि']

			val['Hindi']['alivestatus/wgok'] = ['थी', 'था']

			val['Hindi']['alivestatus'] = ['था']

			if val['Hindi']['लिंग'][0] == 'महिला':

				val['Hindi']['alivestatus/wgop'] = ['थी']

				val['Hindi']['हुए/हुई'] = ['हुई']

				val['Hindi']['के/की'] = ['की']

				val['Hindi']['रखती/रखते'] = ['रखती']

				val['Hindi']['जुड़े/जुडी'] = ['जुडी']

			else:

				val['Hindi']['alivestatus/wgop'] = ['थे']

				val['Hindi']['के/की'] = ['के']

				val['Hindi']['हुए/हुई'] = ['हुए']

				val['Hindi']['रखती/रखते'] = ['रखते']

				val['Hindi']['जुड़े/जुडी'] = ['जुड़े']

		except:

			val['Hindi']['alivestatus'] = ['है']

			val['Hindi']['alivestatus/wgok'] = ['है']

			val['Hindi']['alivestatus/wgop'] = ['है']

			try:

				if val['Hindi']['लिंग'][0] == 'महिला':

					val['Hindi']['हुए/हुई'] = ['हुई']

					val['Hindi']['रखती/रखते'] = ['रखती']

					val['Hindi']['के/की'] = ['की']

					val['Hindi']['जुड़े/जुडी'] = ['जुडी']

				else:

					val['Hindi']['हुए/हुई'] = ['हुए']

					val['Hindi']['रखती/रखते'] = ['रखते']

					val['Hindi']['के/की'] = ['के']

					val['Hindi']['जुड़े/जुडी'] = ['जुड़े']

			except:

				keys_delete.append(key)

	for key in keys_delete:

		del alive_status_added[key]

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'w') as fout:

		json.dump(alive_status_added, fout)