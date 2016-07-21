import sys
import time


# for x in range(0, 100):
#     sys.stdout.write("%s\r" % (str(x) + "%"))
#     time.sleep(0.1)
def print_progress(msg, current,max):
    progress = 100.0*float(current)/float(max)
    msgwith = min(40,len(msg))
    sys.stdout.write('%-48s%3.2f%%\r' % (msg[0:msgwith], progress))
    sys.stdout.flush()
    if progress == 100.0:
        sys.stdout.write('\n')

if __name__ == '__main__':
    max = 1000
    for i in range(max + 1):
        print_progress('ABCDEFGHIJKLMNOPQRSTUVWXYZ.csv (%d)' % i, i,1000)
        time.sleep(0.01)