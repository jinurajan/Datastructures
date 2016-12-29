import sys


class ParkingLot(object):
    _instance = None
    def __init__(self, no_of_slots=6):
        self.no_of_slots = no_of_slots
        self.available_slots = {i: None for i in range(1, no_of_slots+1)}
        self.occupied_slots = {}

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
            print "Created a parking lot with {} slots".format(args[0])
        return cls._instance


    def find_nearest_available_slot(self, ticket):
        # sort the available slots dictionary
        self.available_slots = dict(sorted(self.available_slots.items()))
        slot = list(self.available_slots.items())[0][0]
        ticket.slot = slot
        del self.available_slots[slot]
        self.occupied_slots[slot] = ticket
        print "Allocated slot number: {}".format(slot)
        return ticket

    def release_slot(self, slot):
        # update the available slots and remove from occupied slot
        del self.occupied_slots[slot]
        self.available_slots[slot] = None
        print "Slot number {} is free".format(slot)

    def fetch_reg_numbers_by_color(self, color):
        reg_numbers = [ticket.reg_number for slot,ticket in self.occupied_slots.items() if ticket.color == color]
        if not reg_numbers:
            print "Not Found"
            return
        print ", ".join(reg_number for reg_number in reg_numbers) 

    def fetch_slot_by_reg_number(self, reg_number):
        # check in occupied slots if reg number exists if then return the slot number
        for slot,ticket in self.occupied_slots.items():
            if ticket.reg_number==reg_number:
                return slot

    def print_slot_by_reg_number(self, reg_number):
        slot = self.fetch_slot_by_reg_number(reg_number)
        if slot:
            print slot
        else:
            print "Not Found"

    def fetch_slots_by_color(self, color):
        slots = [slot for slot, ticket in self.occupied_slots.items() if ticket.color == color]
        if not slots:
            print "Not Found"
            return
        print ", ".join(str(slot) for slot in slots)


    def print_status(self):
        headers = ["Slot No.","Registration No","Colour"]
        print "\t".join(header for header in headers)
        for slot, ticket in self.occupied_slots.items():
            print "{}{}\t".format(slot,(len(headers[0])-len(str(slot)))*" " ),
            print "{}{}\t".format(ticket.reg_number, (len(headers[1])-len(ticket.reg_number))*" "),
            print "{}\t".format(ticket.color)



class Ticket(object):
    def __init__(self,parking_lot, reg_number, color):
        if len(parking_lot.occupied_slots) == parking_lot.no_of_slots:
            print "Sorry, parking lot is full"
            return
        else:
            slot = parking_lot.fetch_slot_by_reg_number(reg_number)
            if not slot:
                self.reg_number = reg_number
                self.color = color
                self.slot = parking_lot.find_nearest_available_slot(self)
            else:
                print "Car with Registration No:{} is already parked at slot:{}".format(reg_number, slot)


def get_parking_lot(no_of_slots=6):
    if ParkingLot._instance:
        return ParkingLot._instance
    else:
        return ParkingLot(no_of_slots)


def process_commands(command):
    action = command[0]
    command_length = len(command)
    if command_length == 1:
        if action == "status":
            parking_lot = get_parking_lot()
            parking_lot.print_status()
    elif command_length== 2:
        # can be create parking lot or leave

        if action == "create_parking_lot":
            try:
                parking_lot = get_parking_lot(int(command[1]))
            except ValueError:
                print "number of slots must be an integer"
                sys.exit()
        elif action == "leave":
            try:
                slot = command[1]
                parking_lot = get_parking_lot()
                parking_lot.release_slot(int(slot))
            except ValueError:
                print "Usage leave <slot_number>"
                sys.exit()
        elif action == "registration_numbers_for_cars_with_colour":
            parking_lot = get_parking_lot()
            try:
                parking_lot.fetch_reg_numbers_by_color(command[1])
            except ValueError:
                print "Invalid value Colour:{}".format(command[1])
        elif action == "slot_numbers_for_cars_with_colour":
            parking_lot = get_parking_lot()
            try:
                parking_lot.fetch_slots_by_color(command[1])
            except ValueError:
                print "Invalid value Colour:{}".format(command[1])
        elif action == "slot_number_for_registration_number":
            parking_lot = get_parking_lot()
            try:
                slot = parking_lot.print_slot_by_reg_number(command[1])
            except ValueError:
                print "Invalid value reg_number:{}".format(command[1])
    
    elif command_length == 3:
        # action can be park
        if action == "park":
            try:
                reg_number = command[1]
                color = command[2]
                parking_lot = get_parking_lot()
                Ticket(parking_lot, reg_number, color)
            except ValueError:
                print "Usage: park <reg_number> <color>"
                sys.exit()
    else:
        print "invalid command"
        sys.exit()

def parse_command_line_args(args):
    if len(args) == 1 and args[0] != "status":
        filename = args[0]
        with open(filename) as f:
            commands = f.readlines()
            for command in commands:
                command = command.strip().split()
                process_commands(command)
        sys.exit()
    else:
        while True:
            command = raw_input().split()
            process_commands(command)
        
if __name__ == "__main__":
    command_line_args = parse_command_line_args(sys.argv[1:])