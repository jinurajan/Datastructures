import os, sys

pids = []


def getmatrix(filename):
    matrix = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for line in content:
            line.strip()
            line = line.split()
            row = [int(l) for l in line]
            matrix.append(row)
    return matrix


def duplicate_entry_percentage(filename, n):
    matrix = getmatrix(filename)
    duplicate_entries = set()
    duplicate_count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in duplicate_entries:
                duplicate_count += 1
            else:
                duplicate_entries.add(matrix[i][j])

    percentage = (duplicate_count / float(n * n)) * 100

    return percentage


if len(sys.argv) != 2:
    print "I need one integer through CLI"
    sys.exit(1)

child1 = os.fork()
if child1 == 0:
    # means child process
    print "CHILD1 Started with PID:", os.getpid()
    pid = os.getpid()
    os.execvp('python', ['python', 'fillmatrix.py', sys.argv[1], str(pid)])

child2 = os.fork()
if child2 == 0:
    # means child process
    print "CHILD2 Started with PID:", os.getpid()
    pid = os.getpid()
    os.execvp('python', ['python', 'fillmatrix.py', sys.argv[1], str(pid)])


child3 = os.fork()
if child3 == 0:
    # means child process
    print "CHILD3 Started with PID:", os.getpid()
    pid = os.getpid()
    os.execvp('python', ['python', 'fillmatrix.py', sys.argv[1], str(pid)])

r = 1
while True:
    try:
        p = os.wait()
        print "process", p[0], "completed", r
        pids.append(p[0])
    except OSError:
        print "Game is Over"
        # everything is done now go and read the file
        break
    r += 1

pid_count = {}

child4 = os.fork()
if child4 == 0:
    max_duplicate_percent = 0
    max_pid = -1
    for pid in pids:
        percentage = duplicate_entry_percentage(str(pid), int(sys.argv[1]))
        if percentage not in pid_count:
            pid_count[percentage] = [pid]
        else:
            pid_count[percentage].append(pid)
        if max_duplicate_percent < percentage:
            max_duplicate_percent = percentage
            max_pid = pid
    if max_pid == -1:
        print "No Duplicates"
    else:
        print "Maximum Duplicates exists in :{}".format(
            pid_count[max_duplicate_percent])


os._exit(0)
