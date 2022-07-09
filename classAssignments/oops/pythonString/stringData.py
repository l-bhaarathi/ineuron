import logging
logging.basicConfig(filneame="stringData.log",level=logging.INFO,format="%(levelname)s %(asctime)s %(message)s")

def data():
    logging.info("Function 'data' from the file has been accessed.")
    try:
        data=input()
        logging.info("Data input success.Data-- %s",data)
        return data
    except Exception as e:
        logging.info(e)
        return "Kindly check the following error : ",e
        
