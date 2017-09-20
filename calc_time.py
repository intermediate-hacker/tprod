def generic_time(filename, ignore_cases, accept_cases):
    total = 0

    with open(filename, 'r') as f:
        for line in f:
            proceed = True
            for case in ignore_cases:
                if case in line: proceed = False

            for case in accept_cases:
                if case not in line: proceed = False
            
            if proceed:
                tokens = line.split('|')
                time_tok = tokens[0].split('--')
                hr1 = int(time_tok[0].strip()[:2])
                min1 = int(time_tok[0].strip()[2:])
                hr2 = int(time_tok[1].strip()[:2])
                min2 = int(time_tok[1].strip()[2:])

                total += (hr2*60 + min2) - (hr1*60 + min1)

    total /= 60.0
    return total

def independent_time(filename):
    return generic_time(filename, ["WASTED", "CLASS_"], [])

def wasted_time(filename):
    return generic_time(filename, [], ["WASTED"])

def class_time(filename):
    return generic_time(filename, [], ["CLASS_"])

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print "useage: ", sys.argv[0], "<filename>"
        exit(1)
    print "Independent Work:", independent_time(sys.argv[1]), "hours"