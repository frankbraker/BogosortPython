from random import randint


class BogoSorter(object):

    # BogoSorter class takes an array and creates an output array that is sorted
    def __init__(self, input):
        self.array = input

    def isSorted(self):
        a = self.array.copy()

        a.sort()
        if a == self.array:
            return True
        else:
            return False

    def doSort(self):
        while not self.isSorted():

            a = self.array.copy()
            b = []

            while len(a) > 0:
                r = randint(0, len(a) - 1)
                b.append(a.pop(r))
            # print(b)
            self.array = b.copy()

        # if (self.isSorted()):
        #    print("it worked!")
        # else:
        #    print("it's still not sorted")

        return self.array
