# tprod
Minimalistic productivity logging toolkit.

### Script 1: Adding an entry

usage: python add_entry.py [-h] [-v] [-p] [-C] [-W] T1 T2 N

add entry to daily log

positional arguments:
  T1              start time of the task
  T2              end time of the task
  N               name of task

optional arguments:
  -h, --help      show this help message and exit
  -v, --verbose   print out daily log
  -p, --printout  print daily log without adding entry
  -C, --Class     Add a timestamp for a class attended
  -W, --Wasted    Add a timestamp for time wasted

### Script 2: Calculating productivity (also done by script 1 with -v flag)

useage: python calc_time.py <filename>