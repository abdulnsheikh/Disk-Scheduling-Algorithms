import os
import sys
from diskSchedulingAlgorithms.Algo import abstractAlgorithm as Algorithm

from diskSchedulingAlgorithms.Cscan import Cscan
from diskSchedulingAlgorithms.Fifo import Fifo
from diskSchedulingAlgorithms.Sstf import Sstf 
from typing import List
from virtualMachine.Manager import Manager

from virtualMachine.TheDisk import TheDisk

class Test:
    def __init__(self) -> None: 

        self.run_fifo_test()
        self.run_sstf_test()
        self.run_cscan_test()

    def run_cscan_test(self) -> None:
        requests = self.get_requests_from_file(self)
        algorithm = Cscan()

        print("CSCAN Test****")
        expected_output = [184,241,266,308,333] 

        counter = 0
        for index in range(10, 60, 10):
            time = self.run(requests, algorithm, index) 
            print("{} {}".format(time, expected_output[counter]))
            # the test 
            assert time == expected_output[counter] 
            counter += 1
        print("passed! ")

    def run_fifo_test(self) -> None:
        requests = self.get_requests_from_file(self)
        algorithm = Fifo() 
 
        print("FIFO Test****")
        expected_output = [574,1093,1542,1925,2245] 

        counter = 0
        for index in range(10, 60, 10):
            time = self.run(requests, algorithm, index)
            print("{} {}".format(time, expected_output[counter]))

            # the test
            assert time == expected_output[counter]
            counter += 1
        print("passed! ")

    def run_sstf_test(self) -> None:
        requests = self.get_requests_from_file(self)
        algorithm = Sstf()

        print("SSTF Test****")
        expected_output = [158,198,248,288,323]

        counter = 0
        for index in range(10, 60, 10):
            time = self.run(requests, algorithm, index)
            print("{} {}".format(time, expected_output[counter]))

            # the test
            assert time == expected_output[counter]
            counter += 1
        print("passed! ")

    def run(self, requests: List[int], algorithm: Algorithm, queue_depth: int) -> int:
        simulation = Manager(TheDisk(), requests, queue_depth, algorithm)
        total_queue_time = int(simulation.run() / len(requests))
        return total_queue_time

    # Reads the disk access requests from a file and returns them as a list of integers
    def get_requests_from_file(self, file_name: str) -> List[int]:
        return [243,72,675,217,949,127,278,275,388,183,36,402,83,948,103,
                319,640,232,323,719,1015,638,35,571,465,485,439,976,612,116,
                402,591,609,187,839,742,420,988,366,704,839,608,256,710,456,
                490,542,51,230,32,593,223,620,1008,514,977,689,688,202,624,691,
                826,74,830,81,483,208,51,151,806,383,583,576,19,852,241,526,
                916,946,21,661,801,115,875,757,579,322,202,192,90,299,866,316,
                712,173,478,967,418,173,1003]
