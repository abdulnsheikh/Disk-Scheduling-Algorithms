<p align="center">
  <img src="https://raw.githubusercontent.com/abdulnsheikh/Disk-Scheduling-Algorithms/main/images/image.png" alt="Logo">
</p>


## Operating System Disk Scheduling Simulation
This is a Python program that simulates disk scheduling algorithms used by operating systems to manage and schedule disk input/output (I/O) requests. The simulation reads a list of disk access requests from a file and then runs the selected algorithm to schedule the requests in a queue. The program outputs the total queue time.

## Disk Scheduling Algorithms
The following disk scheduling algorithms are implemented in this program:

`CSCAN (Circular SCAN)`\
`FIFO (First-In, First-Out)`\
`SSTF (Shortest Seek Time First)`

## Usage 

```bash
  python Main.py <algorithm> <queue_size> <file_name>
```


## Where:

<`algorithm>`: The disk scheduling algorithm to use. Possible values are CSCAN, FIFO, and SSTF. If not provided, the program defaults to FIFO.

<`queue_size`>: The maximum size of the disk I/O request queue.

<`file_name`>: The name of the file that contains the list of disk access requests.

## Examples
### Run the FIFO algorithm with a queue size of 10 on the requests.txt file:

`python3 Main.py FIFO 10 requests.txt`

### Run the SSTF algorithm with a queue size of 5 on the requests.txt file:

`python3 Main.py SSTF 5 requests.txt`

## Testing
Unit tests for the disk scheduling algorithms are provided in the unitTesting directory. To run the tests, use the following command:

`python3 Main.py`

Authors
- [Abdulnaser Sheikh](https://github.com/abdulnsheikh/)

Acknowledgements
This project is developed as an assignment for the Operating Systems course at the 

`University of Nebraska Omaha`\
`College of Information Science and Technology`.

## License 

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

