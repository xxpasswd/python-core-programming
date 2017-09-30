#coding=utf-8

from datetime import datetime,timedelta

db ={}

def newuser():
    while True:
        name = raw_input("Input your name: ").lower()
        if name =='':
            print "invalid name! Will back to home"
            break
        if name in db:
            print "Already exist,choose another"
            continue
        else:
            password = raw_input("Input password:  ")
            if password == '':
                print "invalid password!"
            else:
                db[name] = {}.fromkeys(('password', 'last_login'))
                db[name]['password']=password
                print "creat successful"
                break

def olduser():
    while True:
        name = raw_input("Input your name:  ").lower()
        if name == '':
            break

        if name not in db:
            print name,"is not exited!"
            print "Are you want to creat an acount?"
            choice = raw_input("1.ok   2.no   ")
            if choice == '1':
                newuser()
        else:
            password = raw_input("Input passwd:  ")
            if password == db.get(name).get('password'):
                if (db[name]['last_login'] == None ) or ((datetime.today()-db[name]['last_login']) > \
                                                                timedelta(0,120,0)):
                    print "Welcome back,", name
                    db[name]['last_login'] = datetime.today()
                    break
                else:
                    print "You are already logining!", name
                    print "last logged time: ",db[name]['last_login']
                    db[name]['last_login'] = datetime.today()
                    break
            else:
                print "password error!"

def delete_user():
    if db:
        name = raw_input("Input name  ").lower()
        if name in db:
            del db[name]
            print "delete",name
        else:
            print "name error"
    else:
        print "no user regist"

def all_user():
    if db:
        for i in db:
            print "name:%s password:%s" % (i,db[i]['password'])
    else:
        print "no user"

def menu():
    command = [all_user, delete_user]

    while True:
        prompt = int(raw_input("1.show all user   2.delete user  3.quit   "))
        if prompt > 3:
            print "input error!"
        elif prompt == 3:
            break
        else:
            command[prompt-1]()

def showmenu():
    while True:
        prompt = raw_input("1.login  2.menu  3.quit  ")
        if prompt == '1':
            olduser()
        elif prompt == '2':
            admin = raw_input("Enter admin password   ")
            if admin == 'admin':
                menu()
            else:
                print "password error"
        elif prompt == '3':
            break

        else:
            print "input error "

if __name__ == '__main__':
    showmenu()