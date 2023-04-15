# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

from typing import List 
from collections import deque
from diskSchedulingAlgorithms.Algo import abstractAlgorithm as Algorithm
from virtualMachine.DiskRequest import DiskRequest
from virtualMachine.TheDisk import TheDisk

class DiskScheduler:
    # This class represents a disk scheduler.

    START_CYLINDER = 0  # The starting cylinder of the disk.

    def __init__(self, requests: List[int], queue_depth: int, algorithm: Algorithm, disk: TheDisk):
        # Constructor for the class.
        self.requests = deque([DiskRequest(i) for i in requests])  # Initialize the requests as a deque of DiskRequests.
        self.queue_total_time = 0.0  # Initialize the total time to 0.
        self.queue_depth = queue_depth  # Set the queue depth.
        self.queue = deque()  # Initialize the queue as a deque.
        self.algorithm_class = algorithm  # Set the scheduling algorithm.
        self.disk = disk  # Set the disk.

    def get_queue_total_time(self) -> float:
        # This method returns the total time spent in the queue.
        return self.queue_total_time

    def get_requests(self) -> List[DiskRequest]:
        # This method returns a list of the requests.
        return list(self.requests)

    def get_queue(self) -> List[DiskRequest]:
        # This method returns a list of the requests in the queue.
        return list(self.queue)

    def fill_queue(self) -> List[DiskRequest]:
        # This method fills the queue with requests from the request queue.
        if self.requests:
            current_queue_size = len(self.queue)
            available_spaces_in_queue = self.queue_depth - current_queue_size

            for i in range(available_spaces_in_queue):
                self.queue.append(self.requests.popleft())

        return list(self.queue)

    def read(self) -> DiskRequest:
        # This method reads the next request from the queue and returns it.
        self.queue = self.algorithm_class.sort(self.queue, self.disk.current_head_position)

        request_to_retrieve = self.queue.popleft()
        seek_time = self.disk.getSeekTime(self.disk.current_head_position, request_to_retrieve.number)
 
        request_to_retrieve.time += seek_time
 
        self.queue_total_time += request_to_retrieve.time
 
        for r in self.queue:
            r.time += seek_time
 
        self.disk.current_head_position = request_to_retrieve.number

        return request_to_retrieve 