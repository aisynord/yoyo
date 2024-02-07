from model.DatabasePool import DatabasePool
import os
secretKey = os.getenv('SECRET_KEY')
import datetime
import jwt

class User: 
    #register new user
    @classmethod
    def registerUser(cls, email, name, password, role):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor()
            sql = "INSERT INTO admin (email, name, password, role) VALUES (%s,%s,%s,%s)"
            
            cursor.execute(sql, (email, name, password, role))
            dbConn.commit() 
            
            recsChanged = cursor.rowcount
            return recsChanged
        
        finally:
            dbConn.close()
            
#login 
    @classmethod
    def login(cls, email, password):
        try:
            dbConn = DatabasePool.getConnection()
            db_Info = dbConn.connection_id
            print(f"Connected to {db_Info}")

            cursor = dbConn.cursor(dictionary=True)
            sql = "select * from admin where email=%s and password=%s"

            cursor.execute(sql, (email, password))
            results = cursor.fetchone()

            print("Results from the database:", results)

            if not results:
                # Email and password do not match any records
                return {"message": "Wrong email or password", "status": "error"}

            # Set expiry
            payload = {"userid": results["userid"], "role": results["role"],
                       "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)}

            jwtToken = jwt.encode(payload, secretKey, algorithm="HS256")
            return {"jwt": jwtToken, "role": results.get("role", ""), "status": "success", "message": "Successful Login"}

        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Error occurred", "status": "error"}

        finally:
            if dbConn:
                dbConn.close()