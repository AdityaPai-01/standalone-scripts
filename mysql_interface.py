# SIMPLE MYSQL-PYTHON MENU DRIVEN CLI INTERFACE PROGRAM
# MAIN FUNCTIONS INCLUDE:
#   - Adding records
#   - Deleting records
#   - Updating records
#   - Showing all records
#   - Searching one specific record

# DATABASE: test, TABLENAME: 'users'
import mysql.connector, os, time

con = mysql.connector.connect(
    host="your host name",
    user="your username",
    password="your password",
    database="test"
)
cursor = con.cursor()

# CLEARS COMMAND LINE INTERFACE AFTER EXECUTION OF THE FUNCTION
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# SHOWS ALL THE USERS PRESENT IN THE DATABASE
def show_all():
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    print(f"{'USER_ID':<15} {'USER_NAME':<25} {'USER_EMAIL':<30} {'USER_BALANCE':<15}")
    for record in records:
        print(f"{record[0]:<15} {record[1]:<25} {record[2]:<30} {record[3]:<15,.2f}")

# ADDS THE USER RECORDS IN THE SPECIFIED TABLE OF THE DATABASE
def add_user(values):
    try:
        query = "INSERT INTO users (user_id, user_name, user_email, user_balance) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, values)
        con.commit()
        return "executed successfully".upper()
    except Exception as e:
        return f"Error: {e}"

# DELETES THE USER RECORDS IN THE SPECIFIED TABLE OF THE DATABASE
def delete_user(user_id):
    try:
        cursor.execute("SELECT user_id FROM users")
        all_uid = cursor.fetchall()
        for uid in all_uid:
            if user_id == uid[0]:
                cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
                con.commit()
                return "executed successfully".upper()
        return "user not found in database".upper()
    except Exception as e:
        return f"Error: {e}"

# UPDATES THE USER RECORDS AS PER GIVEN PARAMETERS
def update_user(user_id, parameter, new_value):
    try:
        cursor.execute("SELECT * FROM users")
        all_records = cursor.fetchall()
        for record in all_records:
            if user_id == record[0]:
                if parameter == "N":
                    cursor.execute(
                        "UPDATE users SET user_name = %s WHERE user_id = %s",
                        (new_value, user_id),
                    )
                    con.commit()
                    return "executed successfully"
                elif parameter == "E":
                    cursor.execute(
                        "UPDATE users SET user_email = %s WHERE user_id = %s",
                        (new_value, user_id),
                    )
                    con.commit()
                    return "executed successfully".upper()
                else:
                    return "invalid parameter".upper()
        return "USER NOT IN DATABASE"
    except Exception as e:
        return f"Error: {e}"

# SEARCHES FOR SPECIFIC USER RECORD BASED ON ITS UNIQUE ID, DISPLAYS THE ENITRE RECORD IF IT EXISTS
def search_user(user_id):
    try:
        cursor.execute("SELECT * FROM users")
        all_records = cursor.fetchall()
        for record in all_records:
            if user_id == record[0]:
                return f"{'USER_ID':<15} {'USER_NAME':<25} {'USER_EMAIL':<30} {'USER_BALANCE':<15}\n{record[0]:<15} {record[1]:<25} {record[2]:<30} {record[3]:<15,.2f}"
        return "USER NOT IN DATABASE"
    except Exception as e:
        return f"Error: {e}"

# USED TO ASSIGN THE LATEST USER ID TO NEWEST RECORD
def latest_userid():
    cursor.execute('SELECT user_id FROM users')
    all_uid = cursor.fetchall()
    return len(all_uid) + 1

# MAIN PROGRAM
while True:
    print(f"{"WELCOME TO PySQL INTERFACE":=^20}")
    print("YOU CAN PERFORM FOLLOWING FUNCTIONS: ")
    print("1: ADD USER")
    print("2: DELETE USER")
    print("3: UPDATE USER")
    print("4: SEARCH USER")
    print("5: SHOW ALL USER")
    option = input("enter your option: ")
    clear()
    match option:
        case '1':
            print(add_user((f"USER-{latest_userid():04}",input('enter user name: '), input('enter user email:'), 10000)))
        case '2':
            print(delete_user(input('enter users id to delete record: ').upper()))
        case '3':
            print(update_user(input('enter users id to update record: ').upper(), input('enter parameter(N-Name/E-Email): ').upper(),input('enter new value: ')))
        case '4':
            print(search_user(input('enter users id to search recrod: ').upper()))
            input('enter anything to exit: ')
        case '5':
            show_all()
            input('enter anything to exit: ')
        case _:
            print("INVALID INPUT")
    time.sleep(3)
    clear()