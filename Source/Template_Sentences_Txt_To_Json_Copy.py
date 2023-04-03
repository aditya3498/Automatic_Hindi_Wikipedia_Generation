import json

template_sentences_single_pair = ['वह एक प्रसिद्ध {{व्यवसाय}} {alivestatus/wgop} |',
	'वह {{जन्म तिथि}} को पैदा {हुए/हुई} {alivestatus/wgop} |',
	'उनको {{दिया गया नाम}} के नाम से भी जाना जाता {alivestatus/wgok} |',
	'उनकी नागरिकता {{नागरिकता}} देश की {alivestatus/wgok} |',
	'उनका जन्म {{जन्म स्थान}} देश में हुआ {alivestatus/wgok} |',
	'वह {{मातृसंस्था}} {के/की} पूर्व छात्र {alivestatus/wgop} |',
	'वह {{नियोक्ता}} में कार्यरत {alivestatus/wgop} |',
	'उनका देहांत {{मृत्यु तिथि}} में हुआ {alivestatus/wgok} |',
	'उनकी बोली या लिखी भाषा {{बोली या लेखी भाषा}} {alivestatus/wgok} |',
	'उनके परिवार का नाम {{परिवार का नाम}} {alivestatus/wgok} |',
	'उन्हें {{पुरस्कार प्राप्त}} से भी सम्मानित किया गया {alivestatus} |',
	'उनका अंतिम विश्राम का स्थान {{मृत्यु का स्थान}} {alivestatus/wgok} |',
	'उनके कार्यक्षेत्र में {{कार्य क्षेत्र}} शामिल {alivestatus/wgok} |',
	'उन्होंने {{शैक्षिक दर्जा/उपाधि}} की डिग्री भी प्राप्त की {alivestatus/wgok} |',
	'वह {{का सदस्य}} {के/की} भी सदस्य {alivestatus/wgop} |',
	'उनके अंतिम विश्राम का स्थान {{अंतिम विश्राम का स्थान}} {alivestatus/wgok} |',
	'उनकी मातृभाषा {{मातृ भाषा}} {alivestatus/wgok} |',
	'उनके डॉक्टरल एडवाइजर् {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} |',
	'वह {{राजनीतिक दल के सदस्य}} राजनीतिक दल {के/की} सदस्य भी {alivestatus/wgop} |',
	'उन्हें {{पद पर आसीन}} के पद से भी सम्मानित किया गया {alivestatus} |',
	'वह {{डॉक्टरेट छात्र}} {के/की} डॉक्टरल एडवाइजर्स {alivestatus/wgop} |',
	'उनका निवास {{निवास}} में {alivestatus/wgok} |',
	'उन्होंने अपने जीवनकाल में {{संघर्ष में भाग लिया}} के संघर्ष में भी भाग लिया {alivestatus/wgok} |',
	'उनके पिता का नाम {{पिता}} {alivestatus/wgok} |',
	'वह {{धर्म}} धरम {के/की} अनुयायी {alivestatus/wgop} |',
	'वह {{जातीय समूह}} जातीय समूह से सम्बंदित {alivestatus/wgop} |',
	'वह {{के छात्र }} {के/की} छात्र {alivestatus/wgop} |',
	'उनके कुछ उल्लेखनीय कार्य में {{उल्लेखनीय कार्य}} शामिल {alivestatus/wgok} |',
	'उनकी संतान {{संतान}} {alivestatus/wgok} |',
	'उनका कार्य स्थान {{कार्य स्थल}} {alivestatus/wgok} |',
	'उनका देहांत {{मृत्यु का कारण}} की वजह से हुआ {alivestatus/wgok} |',
	'उनके जीवन साथी का नाम {{जीवन साथी}} {alivestatus/wgok} |',
	'एक प्रोफेसर के रूप में, उनके छात्रों में {{छात्र}} भी शामिल {alivestatus/wgok} |',
	'उनके सहोदर {{सहोदर}} {alivestatus/wgok} |',
	'उनकी निष्ठा {{निष्ठा}} के साथ {alivestatus/wgok} |',
	'सेना में उनकी सैन्य रैंक {{सैनिक स्तर;}} {alivestatus/wgok} |',
	'उनके माता का नाम {{माता}} {alivestatus/wgok} |',
	'उन्होंने {{में भागीदार}} में भी हिस्सा लिया {alivestatus} |',
	'वह सेना की {{सैन्य शाखा}} का हिस्सा {alivestatus/wgop} |',
	'उनके प्रेरणास्रोत {{से प्रभावित}} {alivestatus/wgok}',
	'उनका {{संबंधन}} से संबंध {alivestatus/wgok}',
	'वह {{परिवार}} परिवार का हिस्सा {alivestatus/wgop}',
	'वह {{का भाग}} समूह का हिस्सा {alivestatus/wgop}',
	'उनके रिश्तेदार {{संबंधी}} {alivestatus/wgok}',
	'वह {{धार्मिक आदेश}} के धार्मिक आदेश से संबंधित {alivestatus/wgop}',
	'उनकी {{बच्चों की संख्या}} संतान {alivestatus/wgok}',
	'उन्हें कई पुरस्कारों के लिए नामांकित किया गया {alivestatus}, जिनमें से {{नामांकित किया गया}} भी शामिल {alivestatus}',
	'उनके जीवन में एक महत्वपूर्ण घटना हुई है जिनमे से {{महत्वपूर्ण घटना}} शामिल {alivestatus/wgok}',
	'वह {{इसमें अनुरक्त}} में भी रुचि {रखती/रखते} {alivestatus/wgop}',
	'उन्हें {{महान शीर्षक}} की महान उपाधि से सम्मानित किया गया {alivestatus}',
	'उनका छद्म नाम {{कृतकनाम}} {alivestatus/wgok}',
	'उनका अकादमिक प्रमुख {{शैक्षिक विशेष अध्ययन}} में {alivestatus/wgok}',
	'उनकी एक चिकित्सा स्थिति है जिसे {{व्याधि दशा}} के रूप में जाना जाता {alivestatus/wgok}',
	'अपने जीवनकाल में, उन्हें {{कैद करने के का स्थान}} में भी हिरासत में लिया गया {alivestatus}'
]

template_sentences_two_pairs = ['{{Scientist}} को {{इससे अलग}} से भ्रमित नहीं करना चाहिए',

	'{{Scientist}} एक प्रसिद्ध {{व्यवसाय}} {alivestatus/wgop} जिनका जन्म {{जन्म तिथि}} को हुआ {alivestatus}',
	'{{Scientist}} एक प्रसिद्ध {{व्यवसाय}} {alivestatus/wgop} जिनका जन्म {{जन्म स्थान}} देश में हुआ {alivestatus}',
	'{{Scientist}} का जनम {{जन्म तिथि}} को {{जन्म स्थान}} में हुआ {alivestatus}',

	'उनका कार्य क्षेत्र {{कार्य क्षेत्र}} में {alivestatus/wgok} और उनके उल्लेखनीय कार्य में {{उल्लेखनीय कार्य}} शामिल {alivestatus/wgok}',

	'वह {{नागरिकता}} {के/की} नागरिक {alivestatus/wgop} और वह {{मातृसंस्था}} {के/की} पूर्व छात्र भी {alivestatus/wgop}',
	'उन्होंने {{शैक्षिक दर्जा/उपाधि}} की डिग्री भी प्राप्त की {alivestatus/wgok} और वह {{मातृसंस्था}} {के/की} पूर्व छात्र भी {alivestatus/wgop}',
	'वह {{नागरिकता}} {के/की} नागरिक {alivestatus/wgop} और उन्होंने {{शैक्षिक दर्जा/उपाधि}} की डिग्री भी प्राप्त की {alivestatus/wgok}',

	'{{Scientist}} की मृत्यु {{मृत्यु तिथि}} को {{मृत्यु का स्थान}} देश में हुई',
	'{{Scientist}} की मृत्यु {{मृत्यु तिथि}} को {{मृत्यु का कारण}} की वजह से हुई',
	'{{Scientist}} की मृत्यु {{मृत्यु तिथि}} को हुई और उनके अंतिम विश्राम का स्थान {{अंतिम विश्राम का स्थान}} में था',
	'{{Scientist}} की मृत्यु {{मृत्यु का स्थान}} देश में हुई और उनके अंतिम विश्राम का स्थान {{अंतिम विश्राम का स्थान}} में था',
	'{{Scientist}} की मृत्यु {{मृत्यु का स्थान}} देश में {{मृत्यु का कारण}} की वजह से हुई',
	'{{Scientist}} की मृत्यु {{मृत्यु का कारण}} की वजह से हुई और उनके अंतिम विश्राम का स्थान {{अंतिम विश्राम का स्थान}} में था',

	'{{Scientist}} को {{पुरस्कार प्राप्त}} से सम्मानित किया गया और उन्हें {{नामांकित किया गया}} के लिए नामांकित भी किया गया {alivestatus}',
	'{{Scientist}} को {{Reason}} के लिए {{Reason_Award}} से सम्मानित किए जाने के साथ-साथ {{पुरस्कार प्राप्त}} से सम्मानित किया गया |',
	
	'उनकी मातृभाषा {{मातृ भाषा}} {alivestatus/wgok} परन्तु उनकी बोली या लेखी भाषा {{बोली या लेखी भाषा}} {alivestatus/wgok}',

	'{{Scientist}} के शिक्षक {{के छात्र }} {alivestatus/wgok}, डॉक्टरेट एडवाइजर् {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} और वह स्वयं {{डॉक्टरेट छात्र}} {के/की} डॉक्टरेट एडवाइजर् भी {alivestatus/wgop}',
	'{{Scientist}} के डॉक्टरेट एडवाइजर् {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} और वह स्वयं {{डॉक्टरेट छात्र}} {के/की} डॉक्टरेट एडवाइजर् होने के साथ साथ {{छात्र}} के शिक्षक भी {alivestatus/wgop}',
	'{{Scientist}} के शिक्षक {{के छात्र }} {alivestatus/wgok}, डॉक्टरेट एडवाइजर {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} और वह {{छात्र}} के शिक्षक भी {alivestatus/wgop}',
	'{{Scientist}} के शिक्षक {{के छात्र }} {alivestatus/wgok} और वह स्वयं {{डॉक्टरेट छात्र}} {के/की} डॉक्टरेट एडवाइजर् होने के साथ साथ {{छात्र}} के शिक्षक भी {alivestatus/wgop}',
	'{{Scientist}} के डॉक्टरेट एडवाइजर् {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} और वह स्वयं {{डॉक्टरेट छात्र}} {के/की} डॉक्टरेट एडवाइजर् भी {alivestatus/wgop}',
	'{{Scientist}} के डॉक्टरेट एडवाइजर् {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} और इसके अलावा, वह {{छात्र}} {के/की} शिक्षक भी {alivestatus/wgop}',
	'{{Scientist}} स्वयं {{डॉक्टरेट छात्र}} {के/की} डॉक्टरेट एडवाइजर् {alivestatus/wgop}, और इसके अलावा, उनके शिक्षक {{के छात्र }} {alivestatus/wgok}',
	'{{Scientist}} स्वयं {{डॉक्टरेट छात्र}} {के/की} डॉक्टरेट एडवाइजर् {alivestatus/wgop}, और इसके अलावा, वह {{छात्र}} {के/की} शिक्षक भी {alivestatus/wgop}',
	'{{Scientist}} के शिक्षक {{के छात्र }} {alivestatus/wgok} और वह {{छात्र}} {के/की} शिक्षक भी {alivestatus/wgop}',
	'{{Scientist}} के डॉक्टरेट एडवाइजर् {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} और उनके शिक्षक {{के छात्र }} {alivestatus/wgok}',

	'{{Scientist}} {{का भाग}} का हिस्सा होने के साथ-साथ, {{का सदस्य}} का हिस्सा भी {alivestatus/wgop}',
	'{{Scientist}} {{का भाग}} का हिस्सा होने के साथ-साथ, {{राजनीतिक दल के सदस्य}} राजनितिक दाल {के/की} सदस्य भी {alivestatus/wgop}',
	'{{Scientist}} {{का सदस्य}} का हिस्सा {alivestatus/wgop} और वह {{राजनीतिक दल के सदस्य}} राजनितिक दाल {के/की} सदस्य भी {alivestatus/wgop}',

	'{{Scientist}} {{सैन्य शाखा}} में एक {{सैनिक स्तर;}} {alivestatus/wgop}',
	'{{Scientist}} {{सैन्य शाखा}} का हिस्सा {alivestatus/wgop} और उन्होंने {{संघर्ष में भाग लिया}} के संघर्ष में भी भाग लिया {alivestatus}',
	'{{Scientist}} एक {{सैनिक स्तर;}} {alivestatus/wgop} और उन्होंने {{संघर्ष में भाग लिया}} के संघर्ष में भी भाग लिया {alivestatus}',
	'{{Scientist}}, जिनकी निष्ठा {{निष्ठा}} के साथ {alivestatus/wgok}, वह {{सैन्य शाखा}} का हिस्सा {alivestatus/wgop}',
	'{{Scientist}} एक {{सैनिक स्तर;}} {alivestatus/wgop} जिनकी निष्ठा {{निष्ठा}} के साथ {alivestatus/wgok}',
	'{{Scientist}}, जिनकी निष्ठा {{निष्ठा}} के साथ {alivestatus/wgok}, उन्होंने {{संघर्ष में भाग लिया}} संघर्ष में भाग लिया {alivestatus}',

	'{{Scientist}} के माता और पिता {{माता}} और {{पिता}} {alivestatus/wgok} और उनका सहोदर भी {alivestatus} जिनका नाम {{सहोदर}} {alivestatus} |',
	'{{Scientist}} के माता और पिता {{माता}} और {{पिता}} {alivestatus/wgok} और उनके रिश्तेदारों में {{संबंधी}} भी शामिल {alivestatus/wgok}|',
	'{{Scientist}} की माता का नाम {{माता}} {alivestatus} और उनका सहोदर भी {alivestatus} जिनका नाम {{सहोदर}} {alivestatus} | उनके रिश्तेदारों में {{संबंधी}} भी शामिल {alivestatus/wgok}|',
	'{{Scientist}} के पिता {{पिता}} {alivestatus/wgok} और उनका सहोदर भी {alivestatus} जिनका नाम {{सहोदर}} {alivestatus}| उनके रिश्तेदारों में {{संबंधी}} भी शामिल {alivestatus/wgok}|',
	'{{Scientist}} की माता का नाम {{माता}} {alivestatus} और उनका सहोदर भी {alivestatus} जिनका नाम {{सहोदर}} {alivestatus}',
	'{{Scientist}} की माता का नाम {{माता}} {alivestatus} और उनके रिश्तेदारों में {{संबंधी}} भी शामिल {alivestatus/wgok}|',
	'{{Scientist}} के सहोदर {{सहोदर}} {alivestatus/wgok} और उनके रिश्तेदारों में {{संबंधी}} भी शामिल {alivestatus/wgok}|',
	'{{Scientist}} के माता और पिता {{माता}} और {{पिता}} {alivestatus/wgok}',
	'{{Scientist}} के पिता {{पिता}} {alivestatus/wgok} और उनका सहोदर भी {alivestatus} जिनका नाम {{सहोदर}} {alivestatus}',
	'{{Scientist}} के पिता {{पिता}} {alivestatus/wgok} और उनके रिश्तेदारों में {{संबंधी}} भी शामिल {alivestatus/wgok}|',

	'उनका उपनाम {{परिवार का नाम}} {alivestatus} और वह {{परिवार}} परिवार का हिस्सा {alivestatus/wgop}',
	'उनका उपनाम {{परिवार का नाम}} {alivestatus} और वह {{जातीय समूह}} जातीय समूह से सम्बंधित {alivestatus/wgop}',
	'उनका उपनाम {{परिवार का नाम}} {alivestatus} और वह {{संबंधन}} समूह से {जुड़े/जुडी} {alivestatus/wgop}',
	'वह {{परिवार}} परिवार का हिस्सा होने के साथ-साथ {{जातीय समूह}} जातीय समूह से भी सम्बंधित {alivestatus/wgop}',
	'वह {{परिवार}} परिवार का हिस्सा होने के साथ-साथ {{संबंधन}} समूह से भी {जुड़े/जुडी} {alivestatus/wgop}',
	'वह {{जातीय समूह}} जातीय समूह से सम्बंधित {alive status} और वे {{संबंधन}} से भी {जुड़े/जुडी} {alivestatus/wgop}',

	'{{Scientist}} का कार्यस्थल {{कार्य स्थल}} {alivestatus}, और वह {{पद पर आसीन}} के रूप में भी कार्यरत {alivestatus/wgop}',
	'{{Scientist}} का कार्यस्थल {{कार्य स्थल}} {alivestatus}, और वह {{नियोक्ता}} में भी कार्यरत {alivestatus/wgop}',
	'{{Scientist}} को {{नियोक्ता}} में {{पद पर आसीन}} के रूप में नियुक्त किया गया {alivestatus}',

	'वह {{धार्मिक आदेश}} के धार्मिक आदेश का हिस्सा {alivestatus/wgop} और {{धर्म}} {के/की} अनुयायी भी {alivestatus/wgop}',

	'{{Scientist}} {के/की} जीवन साथी {{जीवन साथी}} {alivestatus/wgok} और उनके {{बच्चों की संख्या}} बच्चे {alivestatus/wgok}',
	'{{Scientist}} {के/की} जीवन साथी {{जीवन साथी}} {alivestatus/wgok} और उनके बच्चों का नाम {{संतान}} {alivestatus}',
	'{{Scientist}} के {{बच्चों की संख्या}} {{बच्चे/बच्चा}} {alivestatus/wgok} जिनका नाम {{संतान}} {alivestatus}'
]

template_sentences_three_pairs = ['{{Scientist}} एक प्रसिद्ध {{व्यवसाय}} {alivestatus/wgop} जिनका जन्म {{जन्म तिथि}} को {{जन्म स्थान}} देश में हुआ {alivestatus}',
	'{{नागरिकता}} में पैदा {हुए/हुई} {{Scientist}} {{मातृसंस्था}} {के/की} पूर्व छात्र {alivestatus/wgop} और आगे चलके उन्होंने {{शैक्षिक दर्जा/उपाधि}} की डिग्री भी प्राप्त की',
	'{{Scientist}} का कार्यस्थल {{कार्य स्थल}} {alivestatus}, और वह {{नियोक्ता}} में एक {{पद पर आसीन}} के रूप में भी कार्यरत {alivestatus/wgop}',
	'{{Scientist}} के शिक्षक {{के छात्र }} {alivestatus/wgok} और वह {{छात्र}} {के/की} शिक्षक भी {alivestatus/wgop} और इसके आलावा उनके डॉक्टरेट एडवाइजर् {{डॉक्टरेट सलाहकार}} {alivestatus/wgok} और वह स्वयं {{डॉक्टरेट छात्र}} {के/की} डॉक्टरेट एडवाइजर् भी {alivestatus/wgop} |',
	'{{Scientist}} को {{Reason}} के लिए {{Reason_Award}} से सम्मानित किए जाने के साथ-साथ {{पुरस्कार प्राप्त}} से सम्मानित किया गया | उन्हें {{नामांकित किया गया}} के लिए नामांकित भी किया गया',
	'{{Scientist}} के माता और पिता {{माता}} और {{पिता}} {alivestatus/wgok} और उनका सहोदर भी {alivestatus} जिनका नाम {{सहोदर}} {alivestatus} | उनके रिश्तेदारों में {{संबंधी}} भी शामिल {alivestatus/wgok}|',
	'उनका उपनाम {{परिवार का नाम}} {alivestatus} और वह {{परिवार}} परिवार का हिस्सा होने के साथ-साथ {{जातीय समूह}} जातीय समूह के {alivestatus/wgok} और वह {{संबंधन}} से भी {जुड़े/जुडी} {alivestatus/wgop}',
	'{{Scientist}} {{का भाग}} का हिस्सा होने के साथ-साथ {{का सदस्य}} का हिस्सा {alivestatus/wgop} और इसके अलावा वह {{राजनीतिक दल के सदस्य}} राजनितिक दाल {के/की} सदस्य भी {alivestatus/wgop}',
	'{{Scientist}} {के/की} जीवन साथी {{जीवन साथी}} {alivestatus/wgok} और उनके {{बच्चों की संख्या}} बच्चे {alivestatus/wgok} जिनका नाम {{संतान}} {alivestatus}',
	'{{Scientist}}, जिनकी निष्ठा {{निष्ठा}} के साथ {alivestatus/wgok}, वह {{सैन्य शाखा}} में {{सैनिक स्तर;}} {alivestatus/wgop} और उन्होंने {{संघर्ष में भाग लिया}} संघर्ष में भी भाग लिया {alivestatus}',	
	'{{Scientist}} की मृत्यु {{मृत्यु तिथि}} को {{मृत्यु का स्थान}} देश में {{मृत्यु का कारण}} की वजह से हुई और उनके अंतिम विश्राम का स्थान {{अंतिम विश्राम का स्थान}} में था',
]

with open('../Data/TemplateSentences/Template_Sentences_Single_Pair_Sentence.json', 'w') as fout:

	json.dump(template_sentences_single_pair, fout)

with open('../Data/TemplateSentences/Template_Sentences_Double_Pair_Sentences.json', 'w') as fout:

	json.dump(template_sentences_two_pairs, fout)

with open('../Data/TemplateSentences/Template_Sentences_Triple_Pair_Sentences.json', 'w') as fout:

	json.dump(template_sentences_three_pairs, fout)