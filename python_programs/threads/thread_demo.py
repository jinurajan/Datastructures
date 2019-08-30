from threading import Thread, Lock


class Account:
    def __init__(self):
        self.count = 0

    def deposit(self):
        self.count += 1

    def balance(self):
        return self.count


class Player(Thread):
    def __init__(self, lock, account):
        Thread.__init__(self)
        self.lock = lock
        self.account = account

    def run(self):
        lock = self.lock
        account = self.account
        i = 0
        while i < 1000:
            lock.acquire()
            account.balance()
            account.deposit()
            lock.release()
            i += 1


acc = Account()
lock = Lock()

p1 = Player(lock, acc)
p2 = Player(lock, acc)
p3 = Player(lock, acc)


p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

print "Final value:", acc.balance()
