import psycopg2
from psycopg2 import Error
from uuid import uuid1
from datetime import datetime

def get_user_profile(connection, token):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE userid = %s", (token,))
        user = cursor.fetchone()
        # print("User", token)
        if user:
            user = list(user)
            del user[2]
            del user[0]
            return {"success":True, "user":user}
        else:
            return {"success":False, "message":"No User Found."}
    except Error as e:
        return {"success":False, "message":"Failed to fetch data, Error: " + str(e)}

def register_user(connection, user):
    try:
        cursor = connection.cursor()
        current = datetime.now()
        cursor.execute("INSERT INTO users (userid, email, password, name, registrated_on) VALUES (%s, %s, %s, %s, %s)", (str(uuid1()), user["email"], user["password"], user["name"], current))
        connection.commit()
        return {"success":True, "message":"User created successfully"}
    except Error as e:
        print(f"The error '{e}' occurred")
        return {"success":False, "message":"User cannot be created., Error: " + str(e)}

def login_user(connection, user_creds):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (user_creds["email"], user_creds["password"]))
        user = cursor.fetchone()
        if user:
            return {"success":True, "token":user[0]}
        else:
            print("Invalid username or password")
            return {"success":False, "message":"Invalid username or password."}
    except Error as e:
        return {"success":False, "message":"User cannot login., Error: " + str(e)}
    
def update_profile(connection, user_creds):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET name = %s, gender = %s, contact = %s, location = %s, dob = %s WHERE email = %s", 
                       (user_creds.get("name"), user_creds.get("gender"), user_creds.get("contact"), 
                        user_creds.get("location"), user_creds.get("dob"), user_creds.get("email")))
        connection.commit()
        return {"success": True, "message": "Profile updated successfully."}
    except Error as e:
        return {"success": False, "message": "User cannot be updated., Error: " + str(e)}
