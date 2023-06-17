"""
In this challenge, you have to implement a Snapshot Array with the following properties:

- Constructor (length): This is the constructor and it initializes the data structure to hold the specified number of indexes
- Set Value (idx, val): This property sets the value at a given index idx to value val.
- Snapshot(): This method takes no parameters and returns the Snap ID. Snap ID is the number of times that the snapshot function was called, less 
1, as we start the count at 0.mThe first time this function is called, it saves a snapshot and returns 0. The nth time it is called, after saving the snapshot, it returns 
n−1
.
- Get Value (idx, Snap ID) method returns the value at the index in the snapshot with the given Snap ID

Suppose that we have three nodes whose values we wish to track in the snapshot array. Initially, the value of all the nodes will be 0. After calling the Set Value (1, 4) function, the value of node 1 will change to 4. If we take a snapshot at this point, the current values of all the nodes will be saved with Snap ID 0
. Now, if we call Set Value (1, 7), the current value for node 1 will change to 7 . Now, if we call the Get Value (1, 0) function, we will get the value of node 1 from snapshot 0, that is, 
4

"""


from collections import defaultdict
from copy import deepcopy
class SnapshotArray:
  # Constructor
  def __init__(self, length):
    # Write your code here
    self.snap_id = 0
    self.node_value = defaultdict(dict)
    self.count = length

  # Function set_value sets the value at a given index idx to val. 
  def set_value(self, idx, val):
    if idx < self.count:
      self.node_value[self.snap_id][idx] = val
  
  # This function takes no parameters and returns the snapid.
  # snapid is the number of times that the snapshot() function was called minus 1. 
  def snapshot(self):
    self.node_value[self.snap_id+1] = deepcopy(self.node_value[self.snap_id])
    self.snap_id += 1
    return self.snap_id - 1
  
  def __str__(self):
    return str(self.node_value)
  
  # Function get_value returns the value at the index idx with the given snapid.
  def get_value(self, idx, snap_id):
    if snap_id < self.snap_id and snap_id >=0 and idx < self.count:
      if idx in self.node_value[snap_id]:
        return self.node_value[snap_id][idx]
      return 0


def main():
    num_nodes = [3, 5, 5, 3, 2]
    node_values = [
        [[0, 5], [0, 1], [2, 3], [1, 10]],
        [[4, 1],  [2, 21]],
        [[4, 12], [2, 61]],
        [[0, 15], [0, 5], [2, 13], [1, 100]],
        [[0, 32], [0, 6], [1, 2]]
    ]
    values_to_get = [
        [[0, 0], [0, 1], [1, 0]],
        [[4, 1], [2, 1], [3, 1]],
        [[4, 1], [2, 1], [3, 1]],
        [[0, 1], [1, 1]],
        [[0, 0]]
    ]

    for i in range(len(num_nodes)):
        print(i + 1, ".\tInitializing a data structure with ", num_nodes[i], " nodes", sep = "")
        snapshot_arr = SnapshotArray(num_nodes[i])
        for j in node_values[i]:
            print("\t\tSetting the value of node ", j[0], " to ", j[1], sep = "")
            snapshot_arr.set_value(j[0], j[1])
            print("\t\tSnap id:", snapshot_arr.snapshot(), "\n", sep = "")
        for x in values_to_get[i]:
            print("\t\tNode value at index ", x[0], " with snapID: ", x[1], \
                    " is: ", snapshot_arr.get_value(x[0], x[1]), sep = "")
        print("\n", "-"*100, sep = "")


if __name__ == '__main__':
    main()
