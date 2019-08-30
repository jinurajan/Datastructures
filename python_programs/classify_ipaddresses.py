"""
Write a script to read n ip addresses from the keyboard and classify them into 6 classes.
"""


def classify_ip(*ipaddresses):
    hash_map = {"valid_ips": [], "invalid_ips": [],
                "classA": [], "classB": [],
                "classC": [], "classD": [],
                "classE": []}

    for ipaddress in ipaddresses:
        if is_valid_ipaddress(ipaddress):
            hash_map["valid_ips"].append(ipaddress)
            octets = ipaddress.split(".")
            class_val = get_ip_class(octets)
            if class_val is not None:
                hash_map[class_val].append(ipaddress)
        else:
            hash_map["invalid_ips"].append(ipaddress)

    return hash_map


def get_ip_class(octets):
    component = int(octets[0])
    if component >= 1 and component <= 126:
        return "classA"
    elif component >= 127 and component <= 191:
        return "classB"
    elif component >= 192 and component <= 223:
        return "classC"
    elif component >= 224 and component <= 239:
        return "classD"
    elif component >= 240 and component <= 254:
        return "class E"
    else:
        pass


def is_valid_ipaddress(ipaddress):
    octets = ipaddress.split(".")
    if len(octets) != 4:
        return False
    for each in octets:
        if each.isdigit():
            val = int(each)
            if val < 0 or val > 255:
                return False
        else:
            return False
    return True


if __name__ == "__main__":
    print "Enter Number of Ip addresses:"
    n = int(raw_input())
    i = 0
    ip_array = []
    while i < n:
        ip = raw_input()
        ip_array.append(ip)
        i += 1
    print classify_ip(*ip_array)
