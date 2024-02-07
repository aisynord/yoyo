from model.DatabasePool import DatabasePool

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