import sys


class stack:

    def __init__(self, limit):
        self.lim = limit - 1
        self.list = []
        self.top = None

    def push(self, val):
        if self.top == None:
            self.list.append(val)
            self.top = len(self.list)-1
        else:
            if self.top >= self.lim:
                sys.stderr.write('Overflow!')
                sys.exit()
            else:
                self.list.append(val)
                self.top = len(self.list)-1

    def pop(self):
        if self.top != None:
            self.list.pop()
            self.top = len(self.list) - 1
            if self.top == -1:
                self.top = None
        else:
            sys.stderr.write("Underflow!")
            # print("Underflow!")
            sys.exit()

    def peek(self):
        if self.top == None:
            return(None)
        else:
            return(self.list[self.top])

    def desc(self):
        print('Data:', self.list)
        print('top: ', self.top)
        print('Limit: ', self.lim)
