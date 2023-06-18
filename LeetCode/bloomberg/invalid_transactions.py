"""
Invalid Transactions

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashmap = {}
        result = set()
        for i, t in enumerate(transactions):
            name, time, amount, city =  t.split(",")
            if name not in hashmap:
                hashmap[name] = []
                if int(amount) > 1000:
                    result.add(i)
            else:
                prevTrans = hashmap[name]
                for j in range(len(prevTrans)):
                    prevName, prevTime, prevAmount, prevCity = transactions[prevTrans[j]].split(",")
                    if int(amount) > 1000:
                        result.add(i)
                    if abs(int(time) - int(prevTime)) <= 60 and city != prevCity:
                        result.add(i)
                        result.add(prevTrans[j])
            hashmap[name].append(i)
        return [transactions[t] for t in result]
            
