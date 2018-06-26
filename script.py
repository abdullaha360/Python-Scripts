import os
import paramiko

def welcome():
    print("\t\tCOMMAND MENU")
    print('-'*30)
    print('1.Show IP Info')
    print('2.Run Updates')
    print('3.Device Info')
    print('4.SSH')
    print('5.Locate App')
    print('6.Kill an App')

    print('-' * 30)
welcome()


def ssh():
    ip = input("Enter ip: ")
    usr = input("Enter user: ")
    passw = input("Enter Password: ")
    ssh = paramiko.SSHClient()
    try:
        ssh.connect(ip, port = 22, username = usr, password = passw)
    except:
        return False

def find(app):
	return os.system('whereis -b ' + app)

def sys(num):
    if num == '1':
        return os.system('hostname -i')
    if num == '2':
        print("RUNNING UPDATE")
        try:
            return os.system('sudo -S apt-get update && sudo -S apt-get upgrade')
        finally:
            return os.system('sudo -S yum update')
    if num == '3':
        print("\nDEVICE NAME: ")
        return os.system('uname -a')
    if num == '4':
        ssh()
    if num == '5':
    	appin = input("Find an app: ")
    	find(appin)
    if num == '6':
    	kill = input("Enter name of process to kill: ")
    	return os.system('pkill ' + kill)



inp = input("Pick a number: ")

sys(inp)


