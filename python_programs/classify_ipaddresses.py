"""
Write a script to read n ip addresses from the keyboard and classify them into 6 classes.
"""


def classify_ip(ipaddresses):
    hash_map = {"valid_ips": [], "invalid_ips": [],
                "classA": [], "classB": [],
                "classC": [], "classD": [],
                "classE": []}

    for ipaddress in ipaddresses:
        if is_valid_ipaddress(ipaddress):
            hash_map["valid_ips"].append(ipaddress)
            ip_components = ipaddress.split(".")
            component = int(ip_components[0])
            if component >= 1 and component <= 126:
                hash_map["classA"].append(ipaddress)
            elif component >= 127 and component <= 191:
                hash_map["classB"].append(ipaddress)
            elif component >= 192 and component <= 223:
                hash_map["classC"].append(ipaddress)
            elif component >= 224 and component <= 239:
                hash_map["classD"].append(ipaddress)
            else:
                hash_map["classE"].append(ipaddress)
        else:
            hash_map["invalid_ips"].append(ipaddress)

    return hash_map


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
    print "Enter Number of Ip addresses:"
    n = int(raw_input())
    i = 0
    ip_array = []
    while i < n:
        ip = raw_input()
        ip_array.append(ip)
        i += 1
    print classify_ip(ip_array)
