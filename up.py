#  _______________________________________
# |   Simple Username and Login Extractor |                       
# |                                       |                 
# |   Formats: U:L:P, L:U:P, U:E:P        |            
# |                                       |              
# |_______________________________________|
#

import os, time

with open('file.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

# ----------------------------------------------------------------------#

class UP:
    def __init__(self, list: list):
        self.list = list

    def clear(self):
        with open('output.txt', 'w') as f:
            pass

    def load_list(self):
        for i in data:
            self.list.append(i)

    # ----------------------------- #

    def ulp(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[0]
                p = ln[3]

                with open('output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")

            except:
                print("[!] Line is not in User:Login:Password Format.")

    def lup(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[2]
                p = ln[3]

                with open('output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")

            except:
                print("[!] Line is not in Login:User:Password Format.")

    def uep(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[0]
                p = ln[2]

                with open('output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")

            except:
                print("[!] Line is not in Using:Email:Password Format.")

    def eup(self):
        for i in self.list:
            try:
                ln = str(i).strip().split(':')
                u = ln[1]
                p = ln[2]

                with open('output.txt', 'a') as f:
                    f.write(f"{u}:{p}\n")

            except:
                print("[!] Line is not in Email:User:Password Format.")

# ---------------------------------------------------------------------- #

def main():
    up = UP([])
    up.clear()
    up.load_list()

    os.system('cls')

    op = input("What format is your file in?\n\n[1] User:Login:Password\n[2] Login:User:Password\n[3] User:Email:Password\n[4] Email:User:Password\n[x] exit\n\n> ")
    options = ['1', '2', '3', '4', 'x']

    if op in options:
        if op == 'x':
            exit()
    else:
        print("[!] Invalid Option")
        time.sleep(1.5)
        main()

    if op == '1':
        up.ulp()
    elif op == '2':
        up.lup()
    elif op == '3':
        up.uep()
    else:
        up.eup()

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------- #

os.startfile('output.txt')
