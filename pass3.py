#!/usr/bin/env python3                                                          
import time

class calc(object):
    param = [str(8)+" "+str(4),str("AABBAAABABAB"),str("BB")+" "+str(1),str("AA")+" "+str(1),str("AAAA")+" "+str(4),str("AB")+" "+str(3)]
    name = {}
    file_number = ["0"]
    flag1 = True
    flag2 = True

    def loop1(self,S_list,num):
        ret = []
        M_list = self.M_list
        count = 0
        parent = self.file_number[num]                                                                                            
        for i in range(self.K):
            self.flag1 = True
            new_list = S_list
            check_list = S_list
            while self.flag1:
                num = check_list.find(M_list[i])
                if not num == -1:
                    child = parent + str(count)
                    count += 1
                    self.file_number.append(child)
                    new_list = check_list.replace(M_list[i],"",1)
                    new_list = new_list.replace("x"*len(M_list[i]),M_list[i],1)
                    ret.append(new_list)
                    self.point(parent, child, num, M_list[i])
                    check_list = check_list.replace(M_list[i],"x"*len(M_list[i]),1)
                else:
                    self.flag1 = False
        if count == 0:
            child = parent + str(count)
            self.file_number.append(child)
        return ret

    def loop2(self):
        old_len = 0
        while self.flag2:
            _list = self._list
            current_len = len(_list)
            if current_len == old_len:
                self.flag2 = False
            else:
                for i in range(old_len,current_len):
                    self._list.extend(self.loop1(_list[i],i))
                old_len = current_len
        return self._list
    
    def point(self, old_name, name, num, m_name):                                                                                    
        self.name[name] = self.name[old_name]
        self.name[name] += str(str(num)+" "+str(m_name))
        self.name[name] += "\n"
        return

    def total(self, all_list):
        M_list = self.M_list
        max_list = []
        value_list = []
        point_list = self.point_list
        for k in all_list:
            tmp_list = all_list[k].split("\n")
            value_list.append(all_list[k])
            point = 0
            for i in range(len(tmp_list)):
                for j in range(self.K):
                    if tmp_list[i] != "" and tmp_list[i].split()[1] == M_list[j]:
                        point += int(point_list[j])
            max_list.append(point)
        #print(value_list)
        max_num = max_list.index(max(max_list))
        word = value_list[max_num]
        word += str(max(max_list))
        return word

    def start(self):
        word = ""
        self.N,self.K = map(int,self.param[0].split())
        S = "".join(self.param[1])                                                                              
        self.name["0"] = ""
        self._list = [S]
        _list = []
        _list0 = []
        _list1 = []
        for i in range(self.K):
            _list = list(map(str, self.param[2].split()))
            _list0.append(_list[0])
            _list1.append(_list[1])
        self.M_list = _list0
        self.point_list = _list1
        self.loop2()
        word = self.total(self.name)
        print(word)
        return

if __name__ == "__main__":
    cc = calc()
    cc.start()

