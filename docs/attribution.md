The stackoverflow answer below was the inspiration for the  clocker class

http://stackoverflow.com/a/18101605/540028

Backup of answer in case the link 404s
--------------

User:  user2631403 | answered Aug 7 '13 at 10:57
As a learning exercise for myself, I created a class to be able to create several stopwatch timer instances that you might find useful (I'm sure there are better/simpler versions around in the time modules or similar)

import time as tm
class Watch:
    count = 0
    description = "Stopwatch class object (default description)"
    author = "Author not yet set"
    name = "not defined"
    instances = []
    def __init__(self,name="not defined"):
        self.name = name
        self.elapsed = 0.
        self.mode = 'init'
        self.starttime = 0.
        self.created = tm.strftime("%Y-%m-%d %H:%M:%S", tm.gmtime())
        Watch.count += 1

    def __call__(self):
        if self.mode == 'running':
            return tm.time() - self.starttime
        elif self.mode == 'stopped':
            return self.elapsed
        else:
            return 0.

    def display(self):
        if self.mode == 'running':
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.elapsed = 0.
        elif self.mode == 'stopped':
            pass
        else:
            pass
        print "Name:       ", self.name
        print "Address:    ", self
        print "Created:    ", self.created
        print "Start-time: ", self.starttime
        print "Mode:       ", self.mode
        print "Elapsed:    ", self.elapsed
        print "Description:", self.description
        print "Author:     ", self.author

    def start(self):
        if self.mode == 'running':
            self.starttime = tm.time()
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.starttime = tm.time()
            self.mode = 'running'
            self.elapsed = 0.
        elif self.mode == 'stopped':
            self.mode = 'running'
            #self.elapsed = self.elapsed + tm.time() - self.starttime
            self.starttime = tm.time() - self.elapsed
        else:
            pass
        return

    def stop(self):
        if self.mode == 'running':
            self.mode = 'stopped'
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.mode = 'stopped'
            self.elapsed = 0.
        elif self.mode == 'stopped':
            pass
        else:
            pass
        return self.elapsed

    def lap(self):
        if self.mode == 'running':
            self.elapsed = tm.time() - self.starttime
        elif self.mode == 'init':
            self.elapsed = 0.
        elif self.mode == 'stopped':
            pass
        else:
            pass
        return self.elapsed

    def reset(self):
        self.starttime=0.
        self.elapsed=0.
        self.mode='init'
        return self.elapsed

def WatchList():
    return [i for i,j in zip(globals().keys(),globals().values()) if '__main__.Watch instance' in str(j)]



round_two_decimals() util implementation sourced from this answer
http://stackoverflow.com/a/4519044/540028

Backup of answer in case the link 404s
--------------
User martineau answered Dec 23 '10 at 13:13

8.833333333339or8.833333333333334properly rounded to two decimal places is8.83. Mathematically it sounds like what you want is a ceiling function. The one in Python'smathmodule is namedceil:

import math

v = 8.8333333333333339
print(math.ceil(v*100)/100)  # -> 8.84
Respectively, the floor and ceiling functions generally map a real number to the largest previous or smallest following integer which has zero decimal places—so to use them for 2 decimal places the number is first multiplied by 102 (or 100) to shift the decimal point and is then divided by it afterwards to compensate.

If you don't want to use themathmodule for some reason, you can use this (minimally tested) implementation:

def ceiling(x):
    n = int(x)
    return n if n-1 < x <= n else n+1
How this applies to the linked loan and payment calculator problem

From the sample output it appears that they rounded up the monthly payment, which is what some call the effect of the ceiling function. This means that each month a little more than 1⁄12 of the total amount is being paid. That made the final payment a little smaller than usual—so the remaining unpaid balance was only8.76.

It would be equally valid to use normal rounding producing a monthly payment of8.83and a slightly higher final payment of8.87. However, in the real world people generally don't like to have their payments go up, so rounding up each payment is the common practice—it also returns the money to the lender more quickly.
