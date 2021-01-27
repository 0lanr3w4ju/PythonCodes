# this is a car stimulation

start = False

print("""
this is a car stimulation \n
help menu:
start - starts car
stop - stops car
help - for this help menu
quit - to exit program
""")

while True:
    command = input("> ").lower()

    if command == "start":
        if not start:
            start = True
            print("car started..")
        else:
            print("car started already..")

    elif command == "stop":
        if start:
            start = False
            print("car stopped..")
        else:
            print("car stopped already..")


    elif command == "help":
        print("""
        start - starts car
        stop - stops car
        help - for this help menu
        quit - to exit program
        """)

    elif command == "quit":
        print("exiting program..")
        break
    else:
        print("wrong command!")
