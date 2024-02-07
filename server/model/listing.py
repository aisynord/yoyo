import os
from model.DatabasePool import DatabasePool

class Listing:
    @classmethod 
    def insertListing(cls,title, description,price,country,travelPeriod,imageURL):
        try:
            dbConn=DatabasePool.getConnection()
            cursor=dbConn.cursor(dictionary=True)

            sql="insert into listing (title, description, price, country, travel_period, imageURL) values(%s,%s,%s,%s,%s,%s)"

            # to execute the sql
            cursor.execute(sql,(title, description,price,country,travelPeriod,imageURL))

            dbConn.commit()

            recsChanged=cursor.rowcount

            return recsChanged
        
        finally:
            dbConn.close()