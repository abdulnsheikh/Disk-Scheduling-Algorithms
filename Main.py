# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

import sys
from typing import List
from enum import Enum 

from diskScheudlingAlgorithms.Cscan import Cscan
from diskScheudlingAlgorithms.Fifo import Fifo
from diskScheudlingAlgorithms.Sstf import Sstf
from virtualMachine.Manager import Manager
from virtualMachine.TheDisk import TheDisk
from unitTesting.runTest import Test

class Algorithms(Enum):
    CSCAN = 'CSCAN'
    FIFO = 'FIFO'
    SSTF = 'SSTF'

# Parses the input arguments to check if the queue size and file name are valid, otherwise prints an error message and returns False
def parse_arguments(args: List[str]) -> bool:
    if len(args) == 3:
        try:
            queue_size = int(args[1])
            if queue_size < 1:
                raise ValueError
            input_file_name = args[2]
            with open(input_file_name):
                pass
        except ValueError:
            print("Provided argument for 'queue size' is not valid.")
            return False
        except IOError:
            print("Provided argument for 'file name' is not valid. The file does not exist.")
            return False
    else: 
        print("Wrong number of arguments were given.")
        test = Test()
        return False
    return True

# Reads the disk access requests from a file and returns them as a list of integers
def get_requests_from_file(file_name: str) -> List[int]:
    with open(file_name) as f:
        return [int(line) for line in f]

# Main function that reads the input arguments, initializes the selected algorithm, reads the disk access requests and runs the simulation
def main(args: List[str]) -> None:
    if not parse_arguments(args):
        return

    try:
        # Selects the algorithm to use based on the user's input, otherwise uses FIFO as a default
        algorithm = {
            Algorithms.CSCAN: Cscan,
            Algorithms.SSTF: Sstf,
            Algorithms.FIFO: Fifo,
        }[Algorithms(args[0].upper())]()
    except KeyError:
        algorithm = Fifo()

    file_name = args[2]
    requests = get_requests_from_file(file_name)


    queue_depth = int(args[1])
    simulation = Manager(TheDisk(), requests, queue_depth, algorithm)

    total_queue_time = int(simulation.run() / len(requests))
    print(total_queue_time)

if __name__ == '__main__':
    main(sys.argv[1:])


