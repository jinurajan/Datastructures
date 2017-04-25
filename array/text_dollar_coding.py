

DIGITS_TEXT = {1:'One', 2: 'Two', 3:'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',	
			  8: 'Eight', 9: 'Nine'}
TENS_TEXT = {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
			70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

TEENS_TEXT = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
			 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}


HUNDREDS_TEXT = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million'}


def Textify(number, result):
	if number >=1 and number <=9:
		result.append(DIGITS_TEXT[number])
	elif number >=11 and number <=19:
		result.append(TEENS_TEXT[number])
	else:
		thousand = number/100
		if thousand > 0:
			Textify(thousand, result)
			number = number -(thousand*100)
			Textify(number, result)
		else:
			tens = number / 10
			if tens > 0:
				print("tens: ", tens)
				result.append(TENS_TEXT[tens])
				number = number-(tens*10)
				Textify(number, result)
	return result



def NumberToText(number):
	final_text = []
	n = len(str(number))
	if n > 6:
		# million value
		mill = number/1000000
		Textify(mill, final_text)
		final_text.append(HUNDREDS_TEXT[1000000])
		number =  number - (mill*1000000)

		thousand = number/1000
		Textify(thousand, final_text)
		final_text.append(HUNDREDS_TEXT[1000])
		number =  number - (thousand*1000)

		hundred = number/100
		final_text.append(Textify(hundred, final_text))
		final_text.append(HUNDREDS_TEXT[100])
		number =  number - (hundred*100)
		Textify(number, final_text)
	if n >3:
		thousand = number/1000
		Textify(thousand, final_text)
		final_text.append(HUNDREDS_TEXT[1000])
		number =  number - (thousand*1000)
		hundred = number/100
		Textify(hundred, final_text)
		final_text.append(HUNDREDS_TEXT[100])
		number =  number - (hundred*100)
		Textify(number, final_text)
	elif n > 2:
		hundred = number/100
		Textify(hundred, final_text)
		final_text.append(HUNDREDS_TEXT[100])
		number =  number - (hundred*100)
		Textify(number, final_text)
	else:
		Textify(number, final_text)

	final_text.append("Dollars")
	return final_text

	
def DollarCoding(number):
	value = NumberToText(number)
	print(' '.join(val for val in value))

if __name__ == "__main__":
	DollarCoding(1234567)
	# DollarCoding(123456)
	# DollarCoding(12645)
	# DollarCoding(126)
	# DollarCoding(12)
	# DollarCoding(1)
