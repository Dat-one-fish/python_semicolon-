print("_-_-POWERING UP-_-_")
print("Welcome user to Nokia 5510 ")
print("Powering ON your Ancient of days-----")

while True:  
    print("\n MAIN MENU ")
    print("Choose option (0-13): ")
    print("1. Phone book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call divert")
    print("8. Games")
    print("9. Calculator")
    print("10. Reminders")
    print("11. Clock")
    print("12. Profiles")
    print("13. SIM services")
    print("0. Exit phone")
   
    choice = int(input(":  "))

    match choice:  
        case 0:
            print("Omo finally")
            print("_-_-POWERING DOWN-_-_")
            break

        case 1:
            phonebookopt = -1
            while phonebookopt != 0:  
                print("\n===== PHONE BOOK ==========")
                print("Choose option (0-11 or 0 to go back): ")
                print("1. Search")
                print("2. Service Nos.")
                print("3. Add name")
                print("4. Erase")
                print("5. Edit")
                print("6. Copy")
                print("7. Assign tone")
                print("8. Send b'card")
                print("9. Options")
                print("10. Speed dials")
                print("11. Voice tags")
                print("0. Back")

                phonebookopt = int(input(":  "))

                match phonebookopt:  
                    case 1: print("-> Search...")
                    case 2: print("-> Service Nos...")
                    case 3: print("-> Add name...")
                    case 4: print("-> Erase...")
                    case 5: print("-> Edit...")
                    case 6: print("-> Copy...")
                    case 7: print("-> Assign tone...")
                    case 8: print("-> Send b'card...")
                    case 9: 
                        phonebooktwoopt = -1
                        while phonebooktwoopt != 0:  
                            print("\n========PHONE BOOK OPTIONS========")
                            print("1. Memory in use")
                            print("2. Type of view")
                            print("3. Memory status")
                            print("0. Back")

                            phonebooktwoopt = int(input(":  "))

                            match phonebooktwoopt:  
                                case 1: print("-> Save in SIM...Save to phone")
                                case 2: print("-> Type of view selected.")
                                case 3: print("-> Names saved----.... Space remaining----")
                                case 0: print("-> Returning to Phone Book Menu...")
                                case _: print("Invalid input.")
                    case 10: print("-> Speed dials...")
                    case 11: print("-> Voice tags...")
                    case 0: print("-> Returning to Main Menu...")

        case 2:
            messageopt = -1
            while messageopt != 0:  
                print("\n========== MESSAGES ==========")
                print("Choose option (0-7): ")
                print("1. Write messages")
                print("2. Inbox")
                print("3. Outbox")
                print("4. Picture messages")
                print("5. Templates")
                print("6. Smileys")
                print("7. Message settings")
                print("0. Back")

                messageopt = int(input(":  "))

                match messageopt:  
                    case 1: print("-> Write messages...")
                    case 2: print("-> Inbox...")
                    case 3: print("-> Outbox...")
                    case 4: print("-> Picture messages...")
                    case 5: print("-> Templates...")
                    case 6: print("-> Smileys...")
                    case 7:
                        messagesettingsopt = -1
                        while messagesettingsopt != 0:  
                            print("\n======= MESSAGE SETTINGS =======")
                            print("1. Set 1")
                            print("2. Common")
                            print("0. Back")

                            messagesettingsopt = int(input(":  "))

                            match messagesettingsopt:
                                case 1:
                                    messagetwoopt = -1
                                    while messagetwoopt != 0:  
                                        print("\n--- Set 1 ---")
                                        print("1. Message centre number")
                                        print("2. Messages sent as")
                                        print("3. Message validity")
                                        print("0. Back")
                                        messagetwoopt = int(input(":  "))
                                case 2:
                                    messagethreeopt = -1
                                    while messagethreeopt != 0:  
                                        print("\n--- Common ---")
                                        print("1. Delivery reports")
                                        print("2. Reply via same centre")
                                        print("3. Character support")
                                        print("0. Back")
                                        messagethreeopt = int(input(":  "))

        case 3: 
            print("-> Chat...")

        case 4:
            callregister = -1
            while callregister != 0:  
                print("\n========== CALL REGISTER ==========")
                print("1. Missed calls")
                print("2. Received calls")
                print("3. Dialled numbers")
                print("4. Erase recent call lists")
                print("5. Show call duration")
                print("6. Show call costs")
                print("7. Call cost settings")
                print("8. Prepaid credit")
                print("0. Back")

                callregister = int(input(":  "))

                match callregister:  
                    case 5:
                        durationchoice = -1
                        while durationchoice != 0:  
                            print("\n--- Show call duration ---")
                            print("1. Last call duration")
                            print("2. All calls' duration")
                            print("3. Received calls' duration")
                            print("4. Dialled calls' duration")
                            print("5. Clear timers")
                            print("0. Back")
                            durationchoice = int(input(":  "))
                    case 6:
                        costchoice = -1
                        while costchoice != 0:  
                            print("\n--- Show call costs ---")
                            print("1. Last call cost")
                            print("2. All calls' cost")
                            print("3. Clear counters")
                            print("0. Back")
                            costchoice = int(input(":  "))
                    case 7:
                        costsettingschoice = -1
                        while costsettingschoice != 0:  
                            print("\n--- Call cost settings ---")
                            print("1. Call cost limit")
                            print("2. Show costs in")
                            print("0. Back")
                            costsettingschoice = int(input(":  "))

        case 5:
            toneschoice = -1
            while toneschoice != 0:  
                print("\n========== TONES ==========")
                print("1. Ringing tone")
                print("2. Ringing volume")
                print("3. Incoming call alert")
                print("4. Composer")
                print("5. Message alert tone")
                print("6. Keypad tones")
                print("7. Warning and game tones")
                print("8. Vibrating alert")
                print("9. Screen saver")
                print("0. Back")
                toneschoice = int(input(":  "))

        case 6:
            settingschoice = -1
            while settingschoice != 0:  
                print("\n========== SETTINGS ==========")
                print("1. Call settings")
                print("2. Phone settings")
                print("3. Security settings")
                print("4. Restore factory settings")
                print("0. Back")

                settingschoice = int(input(":  "))

                match settingschoice:  
                    case 1:
                        callsettingschoice = -1
                        while callsettingschoice != 0:  
                            print("\n--- Call settings ---")
                            print("1. Automatic redesign")
                            print("2. Speed dialing")
                            print("3. Call waiting options")
                            print("4. Own number sending")
                            print("5. Phone line in use")
                            print("6. Automatic answer")
                            print("0. Back")
                            callsettingschoice = int(input(":  "))
                    case 2:
                        phonesettingschoice = -1
                        while phonesettingschoice != 0:  
                            print("\n--- Phone settings ---")
                            print("1. Language")
                            print("2. Cell info display")
                            print("3. Welcome note")
                            print("4. Network selection")
                            print("5. Lights")
                            print("6. Confirm SIM service actions")
                            print("0. Back")
