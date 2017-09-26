# tprod
Minimalistic productivity logging toolkit.

### Script 1: Adding an entry

usage: add_entry.py [-h] [-X] [-v] [-p] [-C | -W] [-D] [T1] [T2] [N]

add entry to daily log

optional arguments:

  -h, --help        show this help message and exit

  -X, --XLast       Remove last item

  T1                start time of the task

  T2                end time of the task

  N                 name of task

  -v, --verbose     print out daily log

  -p, --printout    print daily log without adding entry

  -C, --Class       Add a timestamp for a class attended

  -W, --Wasted      Add a timestamp for time wasted

  -D, --Deletelast  Delete most recent entry
  
### Script 2: Calculating productivity (also done by script 1 with -v flag)

useage: python calc_time.py filename