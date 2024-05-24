from mysql.connector import connect, Error

connection = None

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="traffic_recorddb",
        port="3306"
    )
    
    cursor = connection.cursor()
    print("Connected to the database!")
    
    
    def checkUser(username, password=None):
        cmd = f"Select count(username) from user where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a
    
    def add_record(d_name, d_license, address, p_no, email, v_reg, v_model, v_no, off_name, e_agency, offense, date, time, location, description, off_code, court_no, hearing_date, outcome, fines, payment):
        try:
            query = """
                INSERT INTO record
                (d_name, d_license, address, p_no, email, v_reg, v_model, v_no, off_name, e_agency, offense, date, time, location, description, off_code, court_no, hearing_date, outcome, fines, payment) 
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (d_name, d_license, address, p_no, email, v_reg, v_model, v_no, off_name, e_agency, offense, date, time, location, description, off_code, court_no, hearing_date, outcome, fines, payment)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
        
    def get_record():
        try:
            cmd = "SELECT * FROM record;"
            cursor.execute(cmd)
            result = cursor.fetchall()
            print("data: ", result)

            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []

    def update_record(id, d_name, d_license, address, p_no, email, v_reg, v_model, v_no, off_name, e_agency, offense, date, time, location, description, off_code, court_no, hearing_date, outcome, fines, payment):
        try:
            query = """
                UPDATE record 
                SET 
                    d_name = %s,
                    d_license = %s,
                    address = %s,
                    p_no = %s,
                    email = %s,
                    v_reg = %s,
                    v_model = %s,
                    v_no = %s,
                    off_name = %s,
                    e_agency = %s,
                    offense = %s,
                    date = %s,
                    time = %s,
                    location = %s,
                    description = %s,
                    off_code = %s,
                    court_no = %s,
                    hearing_date = %s,
                    outcome = %s,
                    fines = %s,
                    payment = %s
                WHERE 
                    id = %s
            """
            values = (d_name, d_license, address, p_no, email, v_reg, v_model, v_no, off_name, e_agency, offense, date, time, location, description, off_code, court_no, hearing_date, outcome, fines, payment, id)
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()
                if cursor.rowcount == 0:
                    return False
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    
    def get_total_amount_offense():
         try:
            cmd = """SELECT COUNT(*) FROM record;"""
            cursor.execute(cmd)
            total_amount = cursor.fetchone()[0]
            
            if total_amount is None:
                total_amount = 0
            return total_amount
            
         except Exception as e:
            print(f"Error: {e}")
            return []
        
        
    def delete_record(id):
        cmd = f"delete from record where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    
except Error as e:
    print(f"Error: {e}")