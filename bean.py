class Bean:
    __TransId=0
    __TransType=""
    __AccountNo=""
    __CreditAmmount=0.0
    __DebitAmmount=0.0
    __TotalAmmount=0.0
    __TransDate=""
    __TransferAmmount=0.0
    __AccountNo1=""
    __name=""
    def getTransId(self):
        return self.__TransId
    def setTransId(self,id):
        self.__TransId=id
    def getTransType(self):
        return self.__TransType
    def setTransType(self,type):
        self.__TransType=type
    def getAccountNo(self):
        return self.__AccountNo
    def setAccountNo(self,accn):
       self.__AccountNo=accn
    def getCreditAmmount(self):
        return self.__CreditAmmount
    def setCreditAmmount(self,amm):
         self.__CreditAmmount=amm
    def getDebitAmmount(self):
        return self.__DebitAmmount
    def setDebitAmmount(self,amm):
        self.__DebitAmmount=amm
    def getTotalAmmount(self):
        return self.__TotalAmmount
    def setTotalAmmount(self,amm):
        self.__TotalAmmount=amm
    def getTransDate(self):
        return self.__TransDate
    def setTransDate(self,date):
        self.__TransDate=date
    def getTransferAmmount(self):
        return self.__TransferAmmount
    def setTransferAmmount(self, amm):
        self.__TransferAmmount = amm
    def getAccountNo1(self):
        return self.__AccountNo1
    def setAccountNo1(self,accn):
        self.__AccountNo1=accn
    def getname(self):
        return self.__name
    def setname(self,accn):
        self.__name=accn


