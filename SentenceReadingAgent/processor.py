if 'Who' in question[0]:
	 if question[1] in verbs:
	 	if sentence[1] in names:
	 		return sentence.get("VERB")[0]