



def FormatInteger(number):
	result = []
	for i in range(len(number)):
		if i+1 < len(number):
			if int(number[i])%2 ==0 and int(number[i+1]) %2 == 0:
				result.append(number[i])
				result.append('*')
			elif int(number[i])%2 == 1 and int(number[i+1])%2 == 1:
				result.append(number[i])
				result.append('-')
			else:
				result.append(number[i])
		else:
			result.append(number[i])
	output = ''.join(each for each in result)
	return output
	



if __name__ == "__main__":
	line = "12467930 "
	print FormatInteger("12467930")
	print FormatInteger('1234567')
	