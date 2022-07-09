import logging
logging.basicConfig(filename="string.log",level=logging.INFO,format="%(levelname)s %(asctime)s %(message)s")
logging.info("String File has been opened.")
class String:
    logging.info("Class String has been accessed")
    def __init__(self):
        try:
            import stringData
            self.data=stringData.data()
            logging.info("Data import success.")
            logging.info("Raw Data : %s",self.data)
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : \n",e)
    def string_extract(self):
        logging.info("Function string_extract has been accessed")
        try:
            ext=self.data[1:300:3]
            logging.info("string_extract success")
            logging.info("Data : %s",ext)
            return ext
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : \n",e)
    def string_reverse(self):
        logging.info("Function string_reverse has been accessed")
        try:
            rev=self.data[::-1]
            logging.info("string_reverse success")
            logging.info("Data : %s",rev)
            return rev
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : \n",e)
    def string_upper(self):
        logging.info("Function string_upper has been accessed")
        try:
            upper=self.data.upper()
            upper=upper.split()
            logging.info("string_upper success")
            logging.info("Data : %s",upper)
            return upper
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : ",e)
    def string_lower(self):
        logging.info("Function string_lower has been accessed")
        try:
            lower=self.data.lower()
            logging.info("string_lower success")
            logging.info("Data : %s",lower)
            return lower
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : ",e)
    def string_caps(self):
        logging.info("Function string_caps has been accessed")
        try:
            caps=self.data.capitalize()
            logging.info("string_caps success")
            logging.info("Data : %s",caps)
            return caps
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : ",e)
    def string_upper(self):
        logging.info("Function string_upper has been accessed")
        try:
            upper=self.data.upper()
            upper=upper.split()
            logging.info("string_upper success")
            logging.info("Data : %s",upper)
            return upper
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : ",e)
    def string_strip(self):
        logging.info("Function string_strip has been accessed")
        data=input("Enter data to strip : ")
        try:
            strip=data.strip()
            logging.info("string_strip success")
            logging.info("Data : %s",strip)
            return strip
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : ",e)
    def string_lstrip(self):
        logging.info("Function string_lstrip has been accessed")
        data=input("Enter data to  left-strip : ")
        try:
            lstrip=data.lstrip()
            logging.info("string_lstrip success")
            logging.info("Data : %s",lstrip)
            return lstrip
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : ",e)            
    def string_rstrip(self):
        logging.info("Function string_rstrip has been accessed")
        data=input("Enter data to right-strip : ")
        try:
            rstrip=data.rstrip()
            logging.info("string_rstrip success")
            logging.info("Data : %s",rstrip)
            return rstrip
        except Exception as e:
            logging.error(e)
            print("Kindly check the following error : ",e)            
            
    
    
    
    
    
    