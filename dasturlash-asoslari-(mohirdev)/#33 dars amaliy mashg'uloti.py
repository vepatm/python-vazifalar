import pickle

my_birthday = '20021207'
with open('D:/Python/GitHubRepos/python-vazifalar/dasturlash-asoslari-(mohirdev)/pmd.txt', 'r') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace('  ','')
print(my_birthday in pi)

pi = float(pi)

with open('D:/Python/GitHubRepos/python-vazifalar/dasturlash-asoslari-(mohirdev)/otizuch.txt', 'wb') as file:
    pickle.dump(pi,file)

while True:
    malumot = input('\nMa\'lumot kiriting: ')
    with open('D:/Python/GitHubRepos/python-vazifalar/dasturlash-asoslari-(mohirdev)/malumot.txt', 'a') as file:
        file.write(malumot+'\n')
    sorov = input('\nYana ma\'lumot kiritishni xohlaysizmi? (yes/no): ')
    if sorov.lower() == 'no':
        print("\nDastur yakunladi!")
        break