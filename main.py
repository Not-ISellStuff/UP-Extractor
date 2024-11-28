import os

#  _______________________________________
# |   Simple Username and Login Extractor |                       
# |                                       |                 
# |   Format: Username:Login:Password     |                      
# |                                       |              
# |_______________________________________|
#

with open('output.txt', 'w') as f:
    pass

with open('ulp_list.txt', 'r', encoding='utf-8') as f:
    list = f.readlines()

for i in list:
    try:
        ln = i.strip().split(':')

        user = ln[0]
        password = ln[3]
        acc = f"{user}:{password}"

        print(acc)
        with open('output.txt', 'a') as f:
            f.write(f"{acc}\n")
        
    except:
        print("[!] Invalid Format")

os.startfile('output.txt')
