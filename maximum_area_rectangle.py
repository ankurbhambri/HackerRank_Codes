from operator import add


class MHA():

    def __init__(self, arr):
        self.arr = arr

    # Nearest Smallest Elemet at Right
    def nsr(self):
        nsr = []
        for i in range(len(self.arr)):
            ele = len(self.arr)
            for k in range(i+1, len(self.arr), 1):
                if self.arr[i] > self.arr[k]:
                    ele = k
                    break
            nsr.append(ele)
        return nsr

    # Nearest Smallest Elemet at Left
    def nsl(self):
        nsl = []
        for i in range(len(self.arr)):
            prev = -1
            for k in range(i-1, -2, -1):
                if self.arr[i] > self.arr[k]:
                    prev = self.arr[k]
                    break
            if prev == -1:
                nsl.append(-1)
            else:
                nsl.append(self.arr.index(prev))
        return nsl

    def final_compute(self):
        mha = list()
        nsr = self.nsr()
        nsl = self.nsl()
        for i in range(len(self.arr)):
            mha.append(self.arr[i]*(nsr[i] - nsl[i] - 1))
        return mha


if __name__ == "__main__":

    arrs = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]

    new_arrs = []

    for i in range(len(arrs)):
        if i == 0:
            new_arrs.append(arrs[i])
        else:
            new_arrs.append(list(map(add, new_arrs[i-1], arrs[i])))

    max_sub = []
    for i in new_arrs:

        obj = MHA(i)
        max_sub.append(max(obj.final_compute()))

    print(max_sub)
