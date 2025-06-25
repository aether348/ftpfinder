import os 
import sys 
def main():
    ftp_server = input("FTP server: ")
    os.system(f'nmap -sn -R {ftp_server}/24 | grep "Nmap scan report for"')
    option = input("any more? [Y/N]: ")
    if option == "Y":
        main()
    if option == "N":
        sys.exit()

if __name__ == '__main__':
    main()
