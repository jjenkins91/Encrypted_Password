"""
This program will prompt a user for an username and a password
This program will verify if the username or password has any blank spaces
The password will be encrypted and stored inside of a database
If a hacker got access of the database, they would only see the encrypted password and not the real password
"""

import pyodbc as odbc
"""
Makes connection to SQL Server
"""
DRIVER_NAME = "SQL SERVER"
SERVER_NAME = "place_server_name_here"
DATABASE_NAME = "place_database_name_here"

cnxn_str = f"""
           DRIVER={{{DRIVER_NAME}}};
           SERVER={SERVER_NAME};
           DATABASE={DATABASE_NAME};
           Trust_Connection=yes;
            """
cnxn = odbc.connect(cnxn_str)
cursor = cnxn.cursor()

"""
This function validates username
Validates username for blank spaces
If username has blank spaces then user will be prompted to create another username
Once username is validated with no blank spaces then username will be encrypted
"""
def validate_username(validated_username):
    for i in range(len(validated_username)):
        if validated_username[i] == " ":
            return False
    return validated_username

# #Check to see if username is already in use
def sql_username_comparison(username):
    cursor.execute("SELECT * From Password_Encryption")
    row = cursor.fetchone()
    while row:
        my_list = row
        row = cursor.fetchone()
        while my_list[1] == username:
            print("Username already exists")
            validated_username = ask_for_username()
            return validated_username
    return username

def ask_for_username():
    print("Please enter username")
    username = input("Username: ")
    validated_username = validate_username(username)
    while validated_username == False:
        print("Please enter in username with no blank spaces")
        username = input("Username: ")
        validated_username = validate_username(username)
    compared_name = sql_username_comparison(validated_username)
    return compared_name

"""
Prompts user for username
"""
username = ask_for_username()
print(username)
validated_username = username

"""
Prompts user for password
"""
validated_password_as_list = []
password_as_list = []
re_enter_password = ""
print("Please enter password")
user_password = input("Password: ")

"""
This function will encrypted passwords
Passwords as string data types will be converted to a list separating each character or number
Each character or number will be replaced with a new set of letters and/or digits
New encrypted password will be returned
"""

def encrypt_password(encrypted_password):
    for i in range(len(user_password)):
        password_as_list.append(user_password[i])
    for i in range(len(password_as_list)):
        if password_as_list[i] == 'A':
            password_as_list[i] = "4h5"
        elif password_as_list[i] == 'B':
            password_as_list[i] = "#4r"
        elif password_as_list[i] == 'C':
            password_as_list[i] = "9DD"
        elif password_as_list[i] == 'D':
            password_as_list[i] = "0Pq"
        elif password_as_list[i] == 'E':
            password_as_list[i] = "t!m"
        elif password_as_list[i] == 'F':
            password_as_list[i] = "sxz"
        elif password_as_list[i] == 'G':
            password_as_list[i] = "99o"
        elif password_as_list[i] == 'H':
            password_as_list[i] = "fdd"
        elif password_as_list[i] == 'I':
            password_as_list[i] = "dff"
        elif password_as_list[i] == 'J':
            password_as_list[i] = "1s3"
        elif password_as_list[i] == 'K':
            password_as_list[i] = "f0p"
        elif password_as_list[i] == 'L':
             password_as_list[i] = "?as"
        elif password_as_list[i] == 'M':
            password_as_list[i] = "dds"
        elif password_as_list[i] == 'N':
            password_as_list[i] = "?l?"
        elif password_as_list[i] == 'O':
            password_as_list[i] = "D*i"
        elif password_as_list[i] == 'P':
            password_as_list[i] = "DDp"
        elif password_as_list[i] == 'Q':
            password_as_list[i] = "P3s"
        elif password_as_list[i] == 'R':
            password_as_list[i] = "POP"
        elif password_as_list[i] == 'S':
            password_as_list[i] = "!@#"
        elif password_as_list[i] == 'T':
            password_as_list[i] = "Dfg"
        elif password_as_list[i] == 'U':
            password_as_list[i] = "fc4"
        elif password_as_list[i] == 'V':
            password_as_list[i] = "7jf"
        elif password_as_list[i] == 'W':
            password_as_list[i] = "09k"
        elif password_as_list[i] == 'X':
            password_as_list[i] = "4ft"
        elif password_as_list[i] == 'Y':
            password_as_list[i] = "567"
        elif password_as_list[i] == 'Z':
            password_as_list[i] = "Y2k"
        elif password_as_list[i] == 'a':
            password_as_list[i] = "f67"
        elif password_as_list[i] == 'b':
            password_as_list[i] = "#88"
        elif password_as_list[i] == 'c':
            password_as_list[i] = "ihg"
        elif password_as_list[i] == 'd':
            password_as_list[i] = "80o"
        elif password_as_list[i] == 'e':
            password_as_list[i] = "k!m"
        elif password_as_list[i] == 'f':
            password_as_list[i] = "9pa"
        elif password_as_list[i] == 'g':
            password_as_list[i] = "4ft"
        elif password_as_list[i] == 'h':
            password_as_list[i] = "#$g"
        elif password_as_list[i] == 'i':
            password_as_list[i] = "liX"
        elif password_as_list[i] == 'j':
            password_as_list[i] = "SED"
        elif password_as_list[i] == 'k':
            password_as_list[i] = "8ij"
        elif password_as_list[i] == 'l':
            password_as_list[i] = "?FF"
        elif password_as_list[i] == 'm':
            password_as_list[i] = "7y6"
        elif password_as_list[i] == 'n':
            password_as_list[i] = "?f?"
        elif password_as_list[i] == 'o':
            password_as_list[i] = "f*g"
        elif password_as_list[i] == 'p':
            password_as_list[i] = "2e4"
        elif password_as_list[i] == 'q':
            password_as_list[i] = "6Ty"
        elif password_as_list[i] == 'r':
            password_as_list[i] = "iji"
        elif password_as_list[i] == 's':
            password_as_list[i] = "fcd"
        elif password_as_list[i] == 't':
            password_as_list[i] = "SS4"
        elif password_as_list[i] == 'u':
            password_as_list[i] = "p0p"
        elif password_as_list[i] == 'v':
            password_as_list[i] = "fh6"
        elif password_as_list[i] == 'w':
            password_as_list[i] = "!we"
        elif password_as_list[i] == 'x':
            password_as_list[i] = "123"
        elif password_as_list[i] == 'y':
            password_as_list[i] = "fg6"
        elif password_as_list[i] == 'z':
            password_as_list[i] = "6t5"
        elif password_as_list[i] == '1':
            password_as_list[i] = "i*i"
        elif password_as_list[i] == '2':
            password_as_list[i] = "yhu"
        elif password_as_list[i] == '3':
            password_as_list[i] = "7yg"
        elif password_as_list[i] == '4':
            password_as_list[i] = "4es"
        elif password_as_list[i] == '5':
            password_as_list[i] = "vgz"
        elif password_as_list[i] == '6':
            password_as_list[i] = "plh"
        elif password_as_list[i] == '7':
            password_as_list[i] = "7uy"
        elif password_as_list[i] == '8':
            password_as_list[i] = "4f6"
        elif password_as_list[i] == '9':
            password_as_list[i] = "!tg"
        elif password_as_list[i] == '0':
            password_as_list[i] = "sdf"
    encrypted_password = "".join(password_as_list)
    return encrypted_password

"""
This function validates the password
Validates password for blank spaces
If password has blank spaces then user will be prompted to create another password
Once password is validated with no blank spaces then password will be encrypted
"""
def validate_password(validated_password):
    for i in range(len(validated_password)):
        if validated_password[i] == " ":
            return False
validated_password = validate_password(user_password)
while validated_password == False:
    print("Please enter in password with no blank spaces")
    user_password = input("Password: ")
    validated_password = validate_password(user_password)
encrypted_password = encrypt_password(validated_password)

"""
Username and Encrypted password are passed to database
Shows the user the encrypted password and congrats message
If necessary user will have to retype password
Changes to database will be commited
"""

cursor.execute(f"INSERT INTO Password_Encryption (login_name, user_password) VALUES ('{validated_username}','{encrypted_password}')")
print("Please enter your password again")
password_retyped = input("Password: ")
while password_retyped != user_password:
    print("Please enter your password again")
    password_retyped = input("Password: ")
print("Congrats, you created a password")
print(f"Your encrypted password: {encrypted_password}")
cnxn.commit()