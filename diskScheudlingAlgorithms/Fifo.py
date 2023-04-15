# Name: Abdulnaser Sheikh
# Date: April 15th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

from typing import List 
from diskScheudlingAlgorithms.Algo import abstractAlgorithm as Algorithm
from virtualMachine.DiskRequest import DiskRequest

class Fifo(Algorithm):
  def __init__(self):
    self.name = "FIFO"
 
  def sort(self, queue: List[DiskRequest], currentHeadPosition: int) -> List[DiskRequest]:
    return queue
