# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems
 
from diskSchedulingAlgorithms.Algo import abstractAlgorithm as Algorithm
import collections


class Cscan(Algorithm):
    # This class inherits from the Algorithm class and implements the CSCAN algorithm.

    def __init__(self):
        # Constructor for the class
        super().__init__("CSCAN")  # Initialize the parent class Algorithm with the name of the algorithm.

    def sort(self, queue: collections.deque, current_head_position: int) -> collections.deque:
        # This method sorts the requests in the given deque object according to the CSCAN algorithm.

        temp_queue = collections.deque()  # Create a temporary deque object.

        # Traverse the deque and split the requests into two separate queues.
        for _ in range(len(queue)):
            req = queue.popleft()  # Remove the request from the front of the deque.
            if req.getNumber() < current_head_position:
                temp_queue.append(req)  # Add the request to the temporary queue if it is less than the current head position.
            else:
                queue.append(req)  # Add the request to the original queue if it is greater than or equal to the current head position.

        # Sort both the queues using the request number as the key.
        queue = collections.deque(sorted(queue, key=lambda x: x.getNumber()))
        temp_queue = collections.deque(sorted(temp_queue, key=lambda x: x.getNumber()))

        # Append the temporary queue to the original queue and return it.
        queue += temp_queue
        return queue
