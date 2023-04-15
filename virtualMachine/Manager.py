# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

from typing import List
from diskSchedulingAlgorithms.Algo import abstractAlgorithm as Algorithm
from virtualMachine.DiskScheduler import DiskScheduler

from virtualMachine.TheDisk import TheDisk

class Manager:
    def __init__(self, disk: TheDisk, requests: List[int], queue_depth: int, algorithm: Algorithm):
        self.disk = disk
        self.scheduler = DiskScheduler(requests, queue_depth, algorithm, disk)

    def run(self) -> float:
        # Set the current head position to the start cylinder
        self.disk.current_head_position = DiskScheduler.START_CYLINDER
        
        # Continue reading requests until the queue is empty
        while self.scheduler.fill_queue():
            self.scheduler.read()

        # Return the total time spent in the queue
        return self.scheduler.get_queue_total_time()
