from Util import DbConnection
class TransactionHistory:
    def Transaction(self, obj,aa):
        try:
            z = list()
            cur=DbConnection.connection()
            cur1=cur.cursor()
            cur1.execute("select Trans_Id, Trans_type, Trans_Date, Credit_Amount, Debit_amount, Total_Amm from Transaction where Account_No = %s and Trans_Date >= %s",(obj.getAccountNo(),aa))
            a1=cur1.fetchall()
            for i in a1:
                z.append(i)
            cur.close()
            return z
        except:
            return []
class Withdrow:
    def withdrow(self, obj):
        try:
            a=obj.getTransType()
            b=obj.getAccountNo()
            c=obj.getDebitAmmount()
            d=obj.getTotalAmmount()
            cur1 = DbConnection.connection()
            cur=cur1.cursor()
            cur.execute("select now()")
            f = cur.fetchone()[0]
            if( d < c):
                return 0
            a1=cur.execute("insert into Transaction(Trans_type,Account_No,Trans_Date,Debit_amount,total_amm) values(%s,%s,%s,%s,%s)", (a, b, f, c, (d-c)))
            a2=cur.execute("update account  set Total_Amount=Total_Amount-%s where Account_No=%s",(c,b))
            if(a1>0 and a2>0):
                cur1.commit()
                cur1.close()
                return 1
            else:
                cur1.rollback()
                cur1.close()
                return 0
        except Exception as a:
            print(a)
            return 0
class Deposit:
    def deposit(self, obj):
        try:
            a = obj.getTransType()
            b = obj.getAccountNo()
            c = obj.getCreditAmmount()
            d=obj.getTotalAmmount()
            cur1 = DbConnection.connection()
            cur=cur1.cursor()
            cur.execute("select now()")
            f = cur.fetchone()[0]
            a1 = cur.execute("insert into Transaction(Trans_type,Account_No,Trans_Date,Credit_Amount,total_amm) values(%s,%s,%s,%s,%s)", (a, b, f, c,(d+c)))
            a2 = cur.execute("update account set Total_Amount= %s where Account_No=%s", ((d+c), b))
            if 0 < a1 and 0 < a2:
                cur1.commit()
                cur1.close()
                return 1
            else:
                cur1.rollback()
                cur1.close()
                return 0
        except Exception as a:
            print(a)
            return 0
class Transfer:
    def transfer(self, obj):
        try:
            a = obj.getTransType()
            b = obj.getAccountNo()
            c = obj.getTransferAmmount()
            d = obj.getAccountNo1()
            e = obj.getTotalAmmount()
            if(c>e):
                return 0
            cur1=DbConnection.connection()
            cur = cur1.cursor()
            cur.execute("select now()")
            f = cur.fetchone()[0]
            cur.execute("select Total_Amount from account where Account_No=%s", (d,))
            g = cur.fetchone()[0]
            a1 = cur.execute("insert into Transaction(Trans_type,Account_No,Trans_Date,Debit_amount,total_amm) values(%s,%s,%s,%s,%s)", (a, b, f, c,(e-c)))
            a2 = cur.execute("update Account set Total_Amount=Total_Amount-%s where Account_No=%s", (c, b))
            a3 = cur.execute("update Account set Total_Amount=Total_Amount+%s where Account_No=%s", (c, d))
            a4 = cur.execute("insert into Transaction(Trans_type,Account_No,Trans_Date,Credit_Amount,total_amm) values(%s,%s,%s,%s,%s)", (a, d, f, c, (g+c)))
            if(a1>0 and a2>0 and a3>0 and a4>0):
                cur1.commit()
                cur1.close()
                return 1
            else:
                cur1.close()
                return 0
        except Exception:
            print(Exception)
            return 0










