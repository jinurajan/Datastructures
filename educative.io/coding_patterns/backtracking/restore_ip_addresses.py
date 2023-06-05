"""
Given a string s containing digits, return a list of all possible valid IP addresses that can be obtained from the string.

A valid IP address is made up of four numbers separated by dots for example 255.255.255.123. Each number falls between 0 and  255 including 0 and 255, and none of them can have leading zeros.

The input string s consists of digits only
4 <= s.length <= 12
"""


def valid(segment):
    if len(segment) > 3:
        return False
    return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1


def update_segment(s, curr_pos, segments, result):
    segment = s[curr_pos+1: len(s)]
    if valid(segment):
        segments.append(segment)
        result.append(".".join(segments))
        segments.pop()


def backtrack(s, prev_pos,dots, segments, result):
    size = len(s)
    for curr_pos in range(prev_pos+1, min(size-1, prev_pos+4)):
        segment = s[prev_pos+1: curr_pos+1]
        if valid(segment):
            segments.append(segment)

            if dots-1 == 0:
                update_segment(s, curr_pos, segments, result)
            else:
                backtrack(s, curr_pos, dots-1, segments, result)
            segments.pop()

def restore_ip_addresses(s):
    result, segments = [], []
    backtrack(s, -1, 3, segments, result)
    return result


# driver code
def main():
    # input streams of IP addresses
    ip_addresses = ["0000", "25525511135", "12121212",
                    "113242124", "199219239", "121212", "25525511335"]

    # loop to execute till the lenght of input IP addresses
    for i in range(len(ip_addresses)):
        print(i + 1, ".\t Input addresses: '", ip_addresses[i], "'", sep="")
        print("\t Possible valid IP Addresses are: ",
              restore_ip_addresses(ip_addresses[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()