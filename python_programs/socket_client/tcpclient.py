import socket
import os


HOST = "127.0.0.1"
PORT = 6000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    print "     MENU         \n"
    print '1: testprime'
    print '2: nextprime'
    print '3: exit\n'
    ch = raw_input("Enter your choice")
    if ch == '3':
        s.sendall(ch)
        print 'bye'
        break
    if int(ch) < 1 or int(ch) > 2:
        os.system("clear")
        print "Improper choice ... choose right service"
        continue
    n = raw_input('Enter one number : ')
    data = ch + ":" + n
    s.sendall(data)
    result = s.recv(1024)
    os.system('clear')
    print "result from server", result

s.close()
