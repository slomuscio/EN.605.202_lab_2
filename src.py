"""Source code for recursive and iterative Tower of Hanoi solutions.
"""
import time 

def tower_of_hanoi_recursive(n:int, source:str, destination:str, aux:str) -> float:
    """Recursive algorithm to solve the Towers of Hanoi problem for a tower of n disks.

    Args:
        n (int): Number of disks initially in the source tower.
        source (str): Label for source tower. 
        destination (str): Label for destination tower. 
        aux (str): Label for auxiliary tower. 

    Returns:
        float: Time taken in seconds for recursive algorithm to solve Tower of Hanoi. 
    """
    start_time = time.time()
    # Base case 
    if n == 1: 
        print(f"\tMove disk {n} from tower {source} to tower {destination}.")  # Move single disk from source to destination tower.
    # Separate out n-1 case
    else: 
        tower_of_hanoi_recursive(n-1, source, aux, destination)  # Move n-1 disks from source to aux tower.
        print(f"\tMove disk {n} from tower {source} to tower {destination}.")  # Move nth disk from source to destination tower.
        tower_of_hanoi_recursive(n-1, aux, destination, source)  # Move n-1 disks from aux to destination tower.
    end_time = time.time() 
    return end_time - start_time


def move_disk(source:list, destination:list, towers:dict) -> None:
    """Function to move one disk from source tower to destination tower. Called in iterative Tower of Hanoi solution. 

    Args:
        source (list): Tower moving the disk from. 
        destination (list): Tower moving the disk to. 
        towers (dict): Dictionary containing towers. 
    """
    if towers[source]:  # Make sure the source tower is not empty.
        disk = towers[source].pop()  # Get last disk in the source tower.
        towers[destination].append(disk)  # Add disk to destination tower. 
        print(f"\tMove disk {disk} from tower {chr(65 + source)} to tower {chr(65 + destination)}.")


def tower_of_hanoi_iterative(n:int) -> float:
    """Iterative algorithm to solve the Towers of Hanoi problem for a tower of n disks.

    Args:
        n (int): Number of disks initially in the source tower.

    Returns:
        float: Time taken in seconds for iterative algorithm to solve Tower of Hanoi. 
    """
    start_time = time.time()

    # Define the towers as lists.
    source = list(range(n, 0, -1))  # Tower A, descending order so smallest disk (0) is at end of list. 
    aux = []  # Tower B
    destination = []  # Tower C
    towers = {0: source, 1: aux, 2: destination}

    # Total number of moves required to complete Tower of Hanoi.
    total_moves = 2 ** n - 1

    # If n is even, swap destination and aux towers - following movement of disks when n is even.
    if n % 2 == 0:
        towers[1], towers[2] = towers[2], towers[1]

    # Loop through the total number of moves.
    for move in range(1, total_moves + 1):
        if move % 3 == 1:  # Move between source and destination towers.
            move_disk(0, 2, towers) if towers[0] and (not towers[2] or towers[0][-1] < towers[2][-1]) else move_disk(2, 0, towers)
        elif move % 3 == 2:  # Move between source and auxiliary towers.
            move_disk(0, 1, towers) if towers[0] and (not towers[1] or towers[0][-1] < towers[1][-1]) else move_disk(1, 0, towers)
        else:  # Move between auxiliary and destination towers.
            move_disk(2, 1, towers) if towers[1] and (not towers[1] or towers[2][-1] < towers[1][-1]) else move_disk(1, 2, towers)
    
    end_time = time.time() 
    return end_time - start_time


def tower_of_hanoi(n:int) -> None:
    """Wrapper function to run both recursive and iterative Tower of Hanoi solutions and properly format output. 

    Args:
        n (int): Number of disks initially in the source tower.

    Raises:
        Exception: \"Input is not a positive integer.\" if input is not an integer. 
        Exception: \"No disks present in tower.\" if n = 0. 
        Exception: \"N>20, too many disks.\" if n > 20.
    """
    # Check that there are disks present and that there aren't too many disks present. 
    if not n.strip().isdigit():
        raise Exception("Input is not a positive integer.")
    elif int(n) == 0:
        raise Exception("No disks present in tower.")
    elif int(n) > 20:
        raise Exception("N>20, too many disks.")
    
    print("========================================================")
    print(f"n = {n} ")
    try:
        n = int(n)
    except Exception as e:
        log_error(n, e)

    print("\t-- Recursive Output -------------------------\n")
    recursive_time = tower_of_hanoi_recursive(n, "A", "C", "B")  # Run recursive solution.

    print("\n\t-- Iterative Output -------------------------\n")
    iterative_time = tower_of_hanoi_iterative(n)  # Run iterative solution. 

    print("\n\t-- Timing Metrics ---------------------------\n")  # Print timing metrics. 
    print(f"\tRecursive Time: {recursive_time:.5g} s.")
    print(f"\tIterative Time: {iterative_time:.5g} s.")
    print(f"\tRatio (recursive / iterative): {(recursive_time / iterative_time):.5g}")

    print("========================================================\n\n")


def log_error(n:int, e:Exception) -> None:
    """Logs error to the output text file. 

    Args:
        n (int): Number of disks initially in the source tower. 
        e (Exception): Exception thrown.
    """
    print("========================================================")
    print(f"n = {n} ")

    print(f"\t-- Error ----------------------------------\n")
    print(f"\t\t{e}")
    print("===========================================================\n")