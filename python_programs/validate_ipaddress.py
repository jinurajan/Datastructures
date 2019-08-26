"""
Write a script to test if given IP address is valid or not
"""


def is_valid_ipaddress(ipaddress):
    ip_components = ipaddress.split(".")
    if len(ip_components) != 4:
        return False
    valid = True
    for each in ip_components:
        try:
            val = int(each)
            if val < 0 or val > 255:
                valid = False
        except ValueError:
            return False
    return valid


if __name__ == "__main__":
    print "Enter Ip address:"
    ipaddress = raw_input()
    print is_valid_ipaddress(ipaddress)