"""
"""

from heapq import *


def tasks(tasks_list):
    heapify(tasks_list)
    optimal_machines = 0
    available_machines = []
    while tasks_list:
        task_start, task_end = heappop(tasks_list)
        if available_machines and task_start >= available_machines[0][0]:
            machine_in_use_start, machine_in_use_end = heappop(available_machines)
            machine_in_use = (task_end, machine_in_use_end)
        else:
            optimal_machines += 1
            machine_in_use = (task_end, optimal_machines)
        heappush(available_machines, machine_in_use)

    
    return optimal_machines


# driver code
def main():

    # Input: A set "tasks_list" of "n" tasks, such that
    # each task has a start time and a finish time
    input_tasks_list = [[(1, 1), (5, 5), (8, 8), (4, 4),
                        (6, 6), (10, 10), (7, 7)],
                        [(1, 7), (1, 7), (1, 7),
                        (1, 7), (1, 7), (1, 7)],
                        [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)],
                        [(1, 3), (3, 5), (5, 9), (9, 12),
                        (12, 13), (13, 16), (16, 17)],
                        [(12, 13), (13, 15), (17, 20),
                        (13, 14), (19, 21), (18, 20)]]

    # loop to execute till the length of tasks
    for i in range(len(input_tasks_list)):
        print(i + 1, ".\t Tasks = ", input_tasks_list[i], sep="")

        # Output: A non-conflicting schedule of tasks in
        # "tasks_list" using the minimum number of machines
        print("\t Optimal number of machines = ",
              tasks(input_tasks_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
