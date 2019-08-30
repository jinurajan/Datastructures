import os
# import time
# os.system("ls -l")
# fin = os.popen("ls -l")
# records = fin.readlines()
# for record in records:
# 	print record
# 	time.sleep(1)

print "Hello"
os.execvp('ls', ['ls', '-l'])
print "Done"