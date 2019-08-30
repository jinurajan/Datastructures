

class IpAddress(object):
    def __init__(self, val):
        self.ipaddress = val

    def __str__(self):
        return "{}".format(self.ipaddress)

    def valid(self):
        octets = self.ipaddress.split(".")
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

    def getclass(self):
        if self.valid():
            octets = self.ipaddress.split(".")
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
                return "classE"
            else:
                pass
        else:
            return "Invalid Class"

    def __eq__(self, other):
        return self.ipaddress == other.ipaddress


if __name__ == "__main__":
    ip1 = IpAddress("10.20.30.40")
    print ip1
    if ip1.valid():
        print "valid"
    else:
        print "invalid"

    gc = ip1.getclass()

    ip2 = IpAddress("10.20.30.50")

    if ip1 == ip2:
        print "same"
    else:
        print "not same"
