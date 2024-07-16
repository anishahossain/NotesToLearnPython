#short car game to get used to python!
command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''
        start - car started
        stop - car stopped
        quit - game over 
                    ''')
    elif command == 'start':
        if started == False:  # initial set condition is False so when start commend is given python checks if variable started is false
            started = True  # if yes then it is changed to true and 'car started'is printed
            print('car started')
        else:
            print('car already started') # otherwise if it is true then else instructions are followed, same happens for stop command
    elif command == 'stop':
        if not started: # here also python checks started is false, equivalent started == False (comparison)
            print('car already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'quit':
        break
    else:
        print('I do not understand')


