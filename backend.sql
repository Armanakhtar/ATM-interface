Create database ATM;
Use ATM;
Create table Account(
ID varchar(20) Primary key,
Pin Integer(10) Unique,
Account_No varchar(20) Unique check(Length(Account_No)>=10),
Name varchar(20) not null,
Total_Amount Double(20,3) check(Total_Amount>=0)
);

Create table Transaction(
Trans_Id Integer(15) Unique auto_increment,
Trans_type varchar(10),
Account_No varchar(20),
Trans_Date Datetime not null,
Credit_Amount double(20,3),
Debit_amount double(20,3),
Total_Amm double(20,3) not null,
CONSTRAINT FOREIGN KEY(Account_No) REFERENCES Account(Account_No)
);

Insert into Account values(
'imran@2003',1234,'1234567890','Imran',10000),(
'arman@2003',5678,'0987654321','Arman',10000);






