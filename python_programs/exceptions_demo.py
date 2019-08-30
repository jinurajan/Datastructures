print 'hello'
L = [10, 20, 30]
try:
    import Jinu
    x = int(raw_input("Enter first number: "))
    y = int(raw_input("Enter second number: "))
    z = x / y
    print z
    print L[10]
except ValueError:
    print 'I got ValueError'
except IndexError:
    print "I got IndexError"
except ZeroDivisionError:
    print "I got ZeroDivisionError"
except Exception:
    print "I got some other Exception"
else:
    print "No exception"
finally:
    print "I do this anyways"
