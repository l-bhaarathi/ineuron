import logging as dataLog
dataLog.basicConfig(filename="listData.log",level=dataLog.INFO,format="%(levelname)s: %(asctime)s - %(message)s")
dataLog.info("logged into 'listData'")
class data:
    def __init__(self):
        dataLog.info("class 'data' has been accessed")
        try:
            self.list_data=[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , "key1" :"sudh",234:[23,45,656]}]
        
        except Exception as e:
            dataLog.error(e)
            print('Kindly check the following error :',e)

        
                
        
