# _*_ coding:utf-8 _*_
import os
import re


class Main():
    def __init__(self):
        self.LIST = []
        self.DIC = {}

    def get_list(self, numlist):
        for self.num in numlist:
            self.DIC[self.num] = {}
            with open("D:\\Access\\Data\\Data20171226113243416.CM") as f:
                for i in f.readlines():
                    s = re.findall('000000{}'.format(self.num), i.strip())
                    if len(s) > 0:
                        tmp_date = i.strip()[8:18]
                        if tmp_date in self.DIC[self.num].keys():
                            if len(self.DIC[self.num][tmp_date]) > 1:
                                del self.DIC[self.num][tmp_date][-1]
                            self.DIC[self.num][tmp_date].append(i.strip()[19:27])
                        else:
                            self.DIC[self.num][tmp_date] = [i.strip()[19:27]]
        sorted(self.DIC.keys())
        return self.DIC


if __name__ == '__main__':
    print(Main().get_list([69, 36]))