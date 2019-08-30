class Person:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return "Person {0},{1},{2}".format(
            self.fname,
            self.lname,
            self.email)

    def fullname(self):
        return self.fname + self.lname

    def getemail(self):
        return self.email


class Employee(Person):
    def __init__(self, fname, lname, email, eid, salary):
        Person.__init__(self, fname, lname, email)
        self.eid = eid
        self.salary = salary

    def __str__(self):
        return "Person {0}, {1}, {2}, {3}, {4}".format(
            self.fname,
            self.lname,
            self.email,
            self.eid,
            self.salary)

    def getsalary(self):
        return self.salary


p = Person("abc", "xyz", "abc@xyz.com")
print p
fn = p.fullname()
print "my name is", fn

emp = Employee("abc", "xyz", "abc@xyz.com", 1234, 10000)
print emp

fn = emp.fullname()
print fn

sal = emp.getsalary()
print sal
