
from model.DatabasePool import DatabasePool
import traceback

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
            
    @classmethod
    def updateListing(cls, new_title, new_description, new_price, new_country, new_travelperiod, new_imageURL, travelID):
        try:
            dbConn = DatabasePool.getConnection()
            db_Info = dbConn.connection_id
            print(f"Connected to {db_Info}")
            cursor = dbConn.cursor(dictionary=True)

            # update travel listing in the database
            sql = "UPDATE listing SET title=%s, description=%s, price=%s, country=%s, travel_period=%s, imageURL=%s WHERE travelID=%s"
            cursor.execute(sql, (new_title, new_description, new_price, new_country, new_travelperiod, new_imageURL, travelID))

            dbConn.commit()

            return {"message": "Information updated successfully", "status": "success"}

        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            return {"message": f"Error updating data: {str(e)}", "status": "error"}

        finally:
            dbConn.close()