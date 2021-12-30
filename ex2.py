from os import path
import random
import sqlite3
import re

# ouverture/initialisation de la base de donnee 
BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, "ex2.db")
conn = sqlite3.connect(db_path)
# conn.row_factory = sqlite3.Row
c = conn.cursor()
print ("database opened successfully")

def check_special_char(str):

    char_special = "~!@#$%^&*()_+-*/<>,.[]/"

    for i in char_special:
        if i in str:
            return True

    return False


def generate_random_str(randomlength=128):

    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1

    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]

    return random_str


def insert_utilisateur(name, pw):

    if len(name) < 3 :
        print("username lenth should > 3")
        return False
    
    if len(pw) < 8 :
        print("password lenth should > 8")
        return False

    if not any(x.isupper() for x in pw) :
        print("username should contain at least one upper letter")
        return False

    if not check_special_char(pw) :
        print("username should contain at least one special letter")
        return False

    if not re.search(r'\d', pw) :
        print("username should contain at least one number")
        return False

    c.execute("SELECT * FROM utilisateurs WHERE username = ?", (name, ))
    data = c.fetchall()
    if len(data) != 0:
        print("this username has already existed")
        return False
    else:
        s_pub_key = generate_random_str()
        s_pri_key = generate_random_str()
        e_pub_key = generate_random_str()
        e_pri_key = generate_random_str()
        c.execute("insert into utilisateurs values (?, ?, ?, ?, ?, ?)", (name, pw, s_pub_key, s_pri_key, e_pub_key, e_pri_key))
        print ("utilisateur insertion successfully")

    return True
    

def logging(name, pw):

    #verifier le nom existe 
    c.execute("SELECT username FROM utilisateurs WHERE username = ?", (name,))
    data=c.fetchall()
    if len(data)==0:
        print('There is no user named %s'%name)    
        return False

    #verifier les mots de passe corresponds a le nom 
    c.execute("SELECT pass FROM utilisateurs WHERE username = ?", (name,))
    data=c.fetchone()
    if data[0] != pw:
        print('password invalid')    
        return False
    else :
        print("log in successfully")
        return True


def get_key(name, pw, keyname):

    re = logging(name, pw)

    if re :
        c.execute("SELECT ? FROM utilisateurs WHERE username = ?", (keyname, name))
        data = c.fetchall()
        return data
    else:
        print("wrong name and password")
        return False


def verification():

    cursor = c.execute("SELECT username, pass, spublickey, sprivatekey, epublickey, eprivatekey FROM utilisateurs")

    for row in cursor :
        if len(row[0]) < 3 :
            print("username lenth should > 3")
            return False
    
        if len(row[1]) < 8 :
            print("password lenth should > 8")
            return False

        if not any(x.isupper() for x in row[1]) :
            print("username should contain at least one upper letter")
            return False

        if not check_special_char(row[1]) :
            print("username should contain at least one special letter")
            return False

        if not re.search(r'\d', row[1]) :
            print("username should contain at least one number")
            return False

        if len(row[2]) != 128 or len(row[3]) != 128 or len(row[4]) != 128 or len(row[5]) != 128 :
            print("the length of each key should be 128")
            return False

    return True