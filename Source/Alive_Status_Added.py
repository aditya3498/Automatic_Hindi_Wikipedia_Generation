import json

for i in range(1501, 1721):

	keys_delete = []

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'r') as fin:

		for line in fin:

			alive_status_added = json.loads(line)

	for key, val in alive_status_added.items():

		try:

			dob = val['मृत्यु तिथि']

			val['alivestatus/wgok'] = ['थे', 'थी']

			val['alivestatus'] = ['था']

			val['alivestatus/gen'] = ['थी']

			if val['लिंग'][0] == 'महिला':

				val['alivestatus/wgop'] = ['थी']

				val['हुए/हुई'] = ['हुई']

				val['के/की'] = ['की']

				val['रखती/रखते'] = ['रखती']

				val['जुड़े/जुडी'] = ['जुडी']

				val['करते/करती'] = ['करती']

			else:

				val['alivestatus/wgop'] = ['थे']

				val['के/की'] = ['के']

				val['हुए/हुई'] = ['हुए']

				val['रखती/रखते'] = ['रखते']

				val['जुड़े/जुडी'] = ['जुड़े']

				val['करते/करती'] = ['करते']

		except:

			val['alivestatus'] = ['है']

			val['alivestatus/wgok'] = ['है']

			val['alivestatus/wgop'] = ['है']

			val['alivestatus/gen'] = ['है']

			try:

				if val['लिंग'][0] == 'महिला':

					val['हुए/हुई'] = ['हुई']

					val['रखती/रखते'] = ['रखती']

					val['के/की'] = ['की']

					val['जुड़े/जुडी'] = ['जुडी']

					val['करते/करती'] = ['करती']

				else:

					val['हुए/हुई'] = ['हुए']

					val['रखती/रखते'] = ['रखते']

					val['के/की'] = ['के']

					val['जुड़े/जुडी'] = ['जुड़े']

					val['करते/करती'] = ['करते']

			except:

				keys_delete.append(key)

	for key in keys_delete:

		del alive_status_added[key]

	with open('../Data/FinalData/FinalData_15000_Final/Cool' + str(i) + '.json', 'w') as fout:

		json.dump(alive_status_added, fout)