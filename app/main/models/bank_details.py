# -*- encoding: utf-8 -*-

from .. import db

class BankDetails(db.Model):
    __tablename__ = "BankDetails"

    IFSCode  = db.Column(db.String(64), primary_key = True, nullable = False) # Branch IFSC of the bank
    BankName = db.Column(db.String(255), nullable = False)                    # Bank Name
    BranchName = db.Column(db.String(255), nullable = False)                    # Branch Name

    def __repr__(self):
        # return { c.key : getattr(self, c.key) for c in self.__table__.columns }
        return f"<{self.IFSCode}(Bank Name = {self.BankName}, Branch Name = {self.BranchName}>"

    def toDict(self):
        return { c.key : getattr(self, c.key) for c in self.__table__.columns }


class AccountDetails(db.Model):
    __tablename__ = "AccountDetails"

    AccountNumber = db.Column(db.Integer, nullable = False, primary_key = True)
    AccountHolderName = db.Column(db.String(255), nullable = False)                    # Person Name
    AccountType = db.Column(db.String(255), nullable = False)
    IFSCode  = db.Column(db.String(64), nullable = False)                               # Branch IFSC of the bank
    CIF_Number = db.Column(db.String(255), nullable = False)                      
    Account_OpenDate = db.Column(db.Date, nullable = False)

    def __repr__(self):
        # return { c.key : getattr(self, c.key) for c in self.__table__.columns }
        return f"<{self.IFSCode}(Bank Name = {self.BankName}, Branch Name = {self.BranchName}>"

    def toDict(self):
        return { c.key : getattr(self, c.key) for c in self.__table__.columns }