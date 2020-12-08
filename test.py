with open('test.txt','r') as f:
    file = f.readlines()
    
    
for line in file:
    if not line.startswith('From:'):
        continue
    email = line.strip().split()
    emailorg = email[1].split('@')[1]
    print(emailorg)
    