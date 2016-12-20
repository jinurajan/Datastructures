

def find_employees(mapping_dict):
	result_dict = {}
	for pair in mapping_dict:
		if pair[1] not in result_dict:
			result_dict[pair[1]] = [pair[0]]
		else:
			result_dict[pair[1]] =  result_dict[pair[1]]+([pair[0]])

	return result_dict

def count_employees(mapping_dict):
	result_dict = {}
	for pair in mapping_dict:
		if pair[1] not in result_dict:
			result_dict[pair[1]] = 1
		else:
			result_dict[pair[1]] =  result_dict[pair[1]]+1

	return result_dict


def main():
	mapping_dict = [( "A", "C" ),( "B", "C" ),( "C", "F" ),("D", "E" ),( "E", "F" ),( "F", "F" ) ]
	print find_employees(mapping_dict)
	print count_employees(mapping_dict)




if __name__ == "__main__":
	main()