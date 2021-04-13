inp = input('Enter the word You want to generate combination from :- ')

hlst2 = []
hlst  = []
lst   = []

for j in inp:
    for i in inp:
        hlst.append(str(j)+i)

for k in range(len(inp)-2):
    for j in inp:
        for i in hlst:
            hlst2.append(str(j)+str(i))
    for i in hlst:
        lst.append(i)
    for i in hlst:
        hlst.pop()
    for i in hlst2:
        hlst.append(i)
    for i in hlst2:
        hlst2.pop()
    if k+1==int(len(inp)-2):
        for i in hlst:
            lst.append(i)


try:
    print('''                           \n
                                Press ctrl + c to stop the Program.\n
                                        Commands :-\n
                            1 ) Check if number is in list or not :-
                                Command :- check <number You wanna check whether is in list or not>
                                Example :- "check 4312" | Output :- "4312 is in list"
                            2 ) Write every combination in a file :-
                                Command :- write <file name>.<extention>
                                Note : - Extention is required
                                Example :- "write pass_list.txt" | Output :- "pass_list.txt created."
    ''')
    while True:
        cn = input('Execute commands from here > ')
        cmd = cn.split(' ')
        if cmd[0]=='check':
            if len(cmd[1])>len(inp):
                print(f'Maximum length of a word to check is in list or not is {len(inp)}, Try again...')
            elif cmd[1] in lst:
                print(f'{cmd[1]} is in list')
        elif cmd[0]=='write':
            fle = cmd[1].split('.')
            if len(fle)==0:
                print('Please, give a name to file name..')
            else:
                with open(str(cmd[1]), 'w') as f:
                    for item in lst:
                        f.write("%s\n" % item)
                    print(f'{cmd[1]} created..')
except KeyboardInterrupt:
    print('\nStopping program...')
    pass