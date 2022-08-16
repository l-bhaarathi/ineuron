import logging as log
log.basicConfig(filename='assignment3.log',level=log.INFO,format='%(levelname)s: %(asctime)s %(message)s')
log.info('logged into assignment3')
class pattern:
    def name_triangle(self,name,n):
        try:
            for i in range(n):
                for j in range(i):
                    print(name,end=(len(name)//2)*' ')
                print('')
        except Exception as e:
            log.info('pattern.name_triangle')
            log.error(e)

    def name_diamond(self,name,n):
        try:
            k=n-1
            for i in range(n):
                for j in range(k):
                    print(end=(len(name)//2)*' ')
                k-=1
                for j in range(i+1):
                    print(name,end=(len(name)//2)*' ')
                print('')
            k=1
            for i in range(n-2,-1,-1):
                for j in range(k):
                    print(end=(len(name)//2)*' ')
                k+=1
                for j in range(i+1):
                    print(name,end=(len(name)//2)*' ')
                print('')
        except Exception as e:
            log.info('pattern.name_diamond')
            log.error(e)
        
from assignment3_data import data

class operations(data):
    def __listLoop(self,l,var):
        try:
            for i in l:
                if type(i)==list:
                    for j in i:
                        var.append(j)
                elif type(i)==set or type(i)==tuple:
                    self.__listLoop(i,var)
                elif type(i)==dict:
                    self.__listLoop(i.keys(),var)
                    self.__listLoop(i.values(),var)
            return var
        except Exception as e:
            log.info('operations.__listLoop')
            log.error(e)
        
    def get_list(self):
        # to get all the list entities from the data
        try:
            var=list()
            l=self.l
            res=self.__listLoop(l,var)
            return sorted(res)
        except Exception as e:
            log.info('operations.get_list')
            log.error(e)

    
    def __tupleLoop(self,l,var):
        try:
            for i in l:
                if type(i)==tuple:
                    for j in i:
                        var.append(j)
                elif (type(i)==list) or (type(i)==set):
                    self.__tupleLoop(i,var)
                elif type(i)==dict:
                    self.__tupleLoop(i.keys(),var)
                    self.__tupleLoop(i.values(),var)
            return var
        except Exception as e:
            log.info('operations.__tupleLoop')
            log.error(e)
    
    def get_tuple(self):
        # to get all the tuples from the data
        try:
            var=[]
            l=self.l
            res=self.__tupleLoop(l,var)
            return sorted(res)
        except Exception as e:
            log.info('operations.get_tuple')
            log.error(e)
            
    
    def __dictLoop(self,l,var):
        try:
            for i in l:
                if type(i)==dict:
                    var.append(i)
                elif (type(i)==tuple) or (type(i)==list) or (type(i)==set):
                    self.__dictLoop(i,var)
            return var
        except Exception as e:
            log.info("operations.__dictLoop")
            log.error(e)
    
    def get_dict(self):
        # to get all the dictinary entities from data
        try:
            var=list()
            l=self.l
            res=self.__dictLoop(l,var)
            return res
        except Exeception as e:
            log.info('operations.get_dict')
            log.error(e)
    
    def keyNum(self):
        # to get number of keys in the dictionary from data
        try:
            var=self.get_dict()
            var1=[]
            for i in var:
                var1.append(len(i.keys()))
            return var1
        except Exception as e:
            log.info('operations.keyNum')
            log.error(e)
    
    def __numLoop(self,l,var):
        try:
            for i in l:
                if type(i)==int:
                    var.append(i)
                elif (type(i)==list) or (type(i)==tuple) or (type(i)==set):
                    self.__numLoop(i,var)
                elif type(i)==dict:
                    self.__numLoop(list(i.keys()),var)
                    self.__numLoop(list(i.values()),var)
                else:
                    try:
                        if int(i)==int:
                            var.append(i)
                    except:
                        continue
            return var
        except Exception as e:
            log.info('operations.__numLoop')
            log.error(e)
    
    def get_num(self):
        # to get all the numbers from data
        try:
            l=self.l
            var=list()
            res=self.__numLoop(l,var)
            return sorted(res)
        except Exception as e:
            log.info('operations.get_num')
            log.error(e)
    
    def add_num(self):
        # to add all the numbers from data
        try:
            total=self.get_num()
            return sum(total)
        except Exception as e:
            log.info('operations.add_num')
            log.error(e)
    
    def odd_num(self):
        # to get all the odd numbers from data
        try:
            odd=list()
            var=self.get_num()
            for i in var:
                if i%2==0:
                    continue
                else:
                    odd.append(i)
            return odd
        except Exception as e:
            log.info('operations.odd_num')
            log.error(e)
    
    def __valLoop(self,val,l,var):
        try:
            for i in l:
                if type(i)==type(val):
                    if i==val:
                        var.append(val)
                elif (type(i)==list) or (type(i)==set) or (type(i)==tuple):
                    self.__valLoop(val,i,var)
                elif type(i)==dict:
                    self.__valLoop(val,i.keys(),var)
                    self.__valLoop(val,i.values(),var)
                else:
                    try:
                        if type(val)(i)==type(val):
                            if val==i:
                                var.append(i)
                    except:
                        continue
            return var
        except Exception as e:
            log.info('operations.__valLoop')
            log.error(e)
    
    def get_val(self,val):
        # to get a desired value from data
        try:
            var=list()
            l=self.l
            res=self.__valLoop(val,l,var)
            if res:
                return var
            else:
                return 'The given value not present'
        except Exception as e:
            log.info('operations.get_val')
            log.error(e)

    def __countLoop(self,l,var):
        try:
            for i in l:
                if (type(i)==int) or (type(i)==str):
                    var.append(i)
                elif (type(i)==list) or (type(i)==tuple) or (type(i)==set):
                    self.__countLoop(i,var)
                elif type(i)==dict:
                    self.__countLoop(i.keys(),var)
                    self.__countLoop(i.values(),var)
            var1=set(var)
            var_count=dict()
            for i in var1:
                var_count[i]=var.count(i)
            return var_count
        except Exception as e:
            log.info('operations.__countLoop')
            log.error(e)
    
    def val_count(self):
        # to get the frequency of elements in data
        try:
            l=self.l
            var=list()
            res=self.__countLoop(l,var)
            return res
        except Exception as e:
            log.info('operations.val_count')
            log.error(e)

    def __strLoop(self,l,var):
        try:
            for i in l:
                if type(i)==str:
                    var.append(i)
                elif (type(i)==list) or (type(i)==tuple) or (type(i)==set):
                    self.__strLoop(i,var)
                elif type(i)==dict:
                    self.__strLoop(i.keys(),var)
                    self.__strLoop(i.values(),var)
            return var
        except Exception as e:
            log.info('operations.__strLoop')
            log.error(e)
    def get_string(self):
        # to get all the string out of data
        try:
            l=self.l
            var=list()
            res=self.__strLoop(l,var)
            return res
        except Exception as e:
            log.info('operations.get_string')
            log.error(e)
    def alphanum(self):
        # to get all the alphanumeric out of data
        try:
            var1=self.get_string()
            var2=list()
            for i in var1:
                if i.isalnum()==True and i.isalpha()==False:
                    var2.append(i)
                else:
                    var1.remove(i)

            if var2:
                return var2
            else:
                return 'no alphanum'
        except Exception as e:
            log.info('operations.alphanum')
            log.error(e)
    def __listLoop1(self,l1,var2):
        try:
            var1=list()
            for i in l1:
                if type(i)==int:
                    var1.append(i)
        except Exception as e:
            log.info('operations.__listLoop1')
            log.error(e)
        try:
            var2.append(reduce(lambda a,b:a*b,var1))
        except:
            pass
    def multiplyLoop(self):
        # to get multiplication of all the elements in individual arrays from data
        try:
            var2=list()
            l=self.l
            self.__listLoop1(l,var2)
            for i in l:
                if (type(i)==tuple) or (type(i)==list) or (type(i)==set):
                    self.__listLoop1(i,var2)
            return var2
        except Exception as e:
            log.info('operations.multiplyLoop')
            log.error(e)
    def __listLoop3(self,l1,var):
        try:
            for i in l1:
                if type(i)==int or type(i)==str:
                    var.append(i)
                elif type(i)==list or type(i)==tuple or type(i)==set:
                    self.__listLoop3(i,var)
                elif type(i)==dict:
                    self.__listLoop3(i.keys(),var)
                    self.__listLoop3(i.values(),var)
        except Exception as e:
            log.info('operations.__listLoop3')
            log.error(e)
    def flatList(self):
        # to wrap out the data into a flat list
        try:
            var=list()
            l=self.l
            self.__listLoop3(l,var)
            return var
        except Exception as e:
            log.info('operations.flatlist')
            log.error(e)
