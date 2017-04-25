# -*- coding: utf-8 -*-


def longest_common_suffix(string1, string2):
    if not string1  or not string2:
        # if either of one becomes null string return ""
        return ""
    st1, str1 = string1[-1], string1[:-1]
    st2, str2 = string2[-1], string2[:-1]
    if st1 == st2:
        # if the first element of each string is equal append to the result recursively
        return longest_common_suffix(str1, str2) + st1
    else:
        # if they are not equal
        return ""
        # result_1 = longest_common_suffix(string1, str2)
        # result_2 = longest_common_suffix(str1, string2)
        # if len(result_1) > len(result_2):
        # 	return result_1
        # else:
        # 	return result_2


if __name__ == "__main__":
	line = "CornField,outField "
	str1, str2 = line.strip().split(",")
	print longest_common_suffix(str1, str2)