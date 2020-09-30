"""
Given a text return an array stating which languages the text is 
given below is pangrams of english german and turkish

English = The quick brown fox jumps over the lazy dog
German = Falsches Üben von Xylophonmusik quält jeden größeren Zwerg
Turkish = Pijamalı hasta yağız şoföre çabucak güvendi
"""





def find_languages(text):
	English = "The quick brown fox jumps over the lazy dog"
	German = "Falsches Üben von Xylophonmusik quält jeden größeren Zwerg"
	Turkish = "Pijamalı hasta yağız şoföre çabucak güvendi"

	english = set("".join(English.lower().split(" ")))
	german = set("".join(German.lower().split(" ")))
	turkish = set("".join(Turkish.lower().split(" ")))
	res = []
	words = set("".join(text.lower().split(" ")))
	if words.issubset(english):
		res.append('English')
	if words.issubset(german):
		res.append('German')
	if words.issubset(Turkish):
		res.append('Turkish')
	return res




print(find_languages("text"))
print(find_languages("Foo Bar"))
print(find_languages("nasılsın"))
print(find_languages("Valeska Gert Straße Berlin Germany"))

