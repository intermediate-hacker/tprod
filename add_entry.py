import datetime
import sys
import subprocess
import argparse

import calc_time

months = ["Unknown",
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

def get_file_name():
    now = datetime.datetime.now()
    return "{0}_{1}_{2}.log".format(months[now.month], now.day, now.year)

def add_entry(start, end, label, verbose):
    filename = get_file_name()

    with open(filename, "a") as fp:
        fp.write(str(start) + " -- " + str(end) + " | " + label + "\n")

    if verbose: show_log()

def add_class(start, end, label, verbose):
  add_entry(start, end, "CLASS_" + label, verbose)

def add_independent(start, end, label, verbose):
  add_entry(start, end, label, verbose)

def add_wasted(start, end, verbose):
  add_entry(start, end, "WASTED", verbose)

def show_log():
  filename = get_file_name()
  with open(filename, "r") as fp:
        print fp.read()
        print "=" * 10
  print "Independent Work", round(calc_time.independent_time(filename), 2), "hours."


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'add entry to daily log')
    parser.add_argument('start_time', metavar = 'T1', type=int, help = 'start time of the task')
    parser.add_argument('end_time', metavar = 'T2', type=int, help = 'end time of the task')
    parser.add_argument('label', metavar = 'N', type=str, help = 'name of task')
    parser.add_argument('-v', '--verbose', action='store_true', help='print out daily log')
    parser.add_argument('-p', '--printout', action='store_true', help='print daily log without adding entry')
    parser.add_argument('-C', '--Class', action='store_true', help='Add a timestamp for a class attended')
    parser.add_argument('-W', '--Wasted', action='store_true', help='Add a timestamp for time wasted')

    args = parser.parse_args()

    if args.Class:
      add_class(args.start_time, args.end_time, args.label, args.verbose)
    elif args.Wasted:
      add_wasted(args.start_time, args.end_time, args.verbose)
    else:
      add_independent(args.start_time, args.end_time, args.label, args.verbose)