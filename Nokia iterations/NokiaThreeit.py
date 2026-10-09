home_code = 99


def power_up():
    print("_-_-POWERING UP-_-_")
    print("Welcome user to Nokia 5510 ")
    print("Powering ON your Ancient of days-----")


def show_main_menu():
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
    print("99. Home")


def show_home_option():
    print("99. Home")


def go_home():
    print("-> HOME")
    return True


def phonebook_options_menu():
    phonebooktwoopt = 1

    while phonebooktwoopt != 0:
        print("\n========PHONE BOOK OPTIONS========")
        print("1. Memory in use")
        print("2. Type of view")
        print("3. Memory status")
        show_home_option()

        phonebooktwoopt = int(input(":  "))

        if phonebooktwoopt == home_code:
            return go_home()

        match phonebooktwoopt:
            case 1:
                print("-> Save in SIM...Save to phone")

            case 2:
                print("-> Type of view selected.")

            case 3:
                print("-> Names saved----.... Space remaining----")

            case 0:
                print("-> i wanna LEAVE")

            case _:
                print("Invalid input.")

    return False


def phonebook_menu():
    phonebookopt = 1

    while phonebookopt != 0:
        print("\n===== PHONE BOOK ==========")
        print("Choose option (1-11): ")
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
        print("0.  Back to menu")
        show_home_option()

        phonebookopt = int(input(":  "))

        if phonebookopt == home_code:
            return go_home()

        match phonebookopt:
            case 1:
                print("-> Search...")

            case 2:
                print("-> Service Nos...")

            case 3:
                print("-> Add name...")

            case 4:
                print("-> Erase...")

            case 5:
                print("-> Edit...")

            case 6:
                print("-> Copy...")

            case 7:
                print("-> Assign tone...")

            case 8:
                print("-> Send b'card...")

            case 9:
                print("-> Options")
                if phonebook_options_menu():
                    return True

            case 10:
                print("-> Speed dials...")

            case 11:
                print("-> Voice tags...")

            case 0:
                print("-> Back to MAIN MENU")

            case _:
                print("Guy Follow Instruction na!")
                print("Invalid Input sha.")

    return False


def message_set_one_menu():
    messagetwoopt = 1

    while messagetwoopt != 0:
        print("\n--- Set 1 ---")
        print("1. Message centre number")
        print("2. Messages sent as")
        print("3. Message validity")
        print("0. Back")
        show_home_option()

        messagetwoopt = int(input(":  "))

        if messagetwoopt == home_code:
            return go_home()

        match messagetwoopt:
            case 1:
                print("-> Message centre number")

            case 2:
                print("-> Messages sent as")

            case 3:
                print("-> Message validity")

            case 0:
                print("-> Back")

            case _:
                print("Invalid input.")

    return False


def message_common_menu():
    messagethreeopt = 1

    while messagethreeopt != 0:
        print("\n--- Common ---")
        print("1. Delivery reports")
        print("2. Reply via same centre")
        print("3. Character support")
        print("0. Back")
        show_home_option()

        messagethreeopt = int(input(":  "))

        if messagethreeopt == home_code:
            return go_home()

        match messagethreeopt:
            case 1:
                print("-> Delivery reports")

            case 2:
                print("-> Reply via same centre")

            case 3:
                print("-> Character support")

            case 0:
                print("-> Back")

            case _:
                print("Invalid input.")

    return False


def message_settings_menu():
    settingsopt = 1

    while settingsopt != 0:
        print("\n======= MESSAGE SETTINGS =======")
        print("1. Set 1")
        print("2. Common")
        show_home_option()

        settingsopt = int(input(":  "))

        if settingsopt == home_code:
            return go_home()

        match settingsopt:
            case 1:
                if message_set_one_menu():
                    return True

            case 2:
                if message_common_menu():
                    return True

            case 0:
                print("-> Back to MESSAGES")

            case _:
                print("Invalid input.")

    return False


def messages_menu():
    messageopt = 1

    while messageopt != 0:
        print("\n========== MESSAGES ==========")
        print("Choose option (1-7): ")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        show_home_option()

        messageopt = int(input(":  "))

        if messageopt == home_code:
            return go_home()

        match messageopt:
            case 1:
                print("-> Write messages...")

            case 2:
                print("-> Inbox...")

            case 3:
                print("-> Outbox...")

            case 4:
                print("-> Picture messages...")

            case 5:
                print("-> Templates...")

            case 6:
                print("-> Smileys...")

            case 7:
                if message_settings_menu():
                    return True

            case 0:
                print("-> Back to MAIN MENU")

            case _:
                print("Invalid input.")

    return False


def call_duration_menu():
    durationchoice = 1

    while durationchoice != 0:
        print("\n--- Show call duration ---")
        print("1. Last call duration")
        print("2. All calls' duration")
        print("3. Received calls' duration")
        print("4. Dialled calls' duration")
        print("5. Clear timers")
        show_home_option()

        durationchoice = int(input(":  "))

        if durationchoice == home_code:
            return go_home()

        if durationchoice == 0:
            print("-> Back to CALL REGISTER")

    return False


def call_costs_menu():
    costchoice = 1

    while costchoice != 0:
        print("\n--- Show call costs ---")
        print("1. Last call cost")
        print("2. All calls' cost")
        print("3. Clear counters")
        show_home_option()

        costchoice = int(input(":  "))

        if costchoice == home_code:
            return go_home()

        if costchoice == 0:
            print("-> Back to CALL REGISTER")

    return False


def call_cost_settings_menu():
    costsettingschoice = 1

    while costsettingschoice != 0:
        print("\n--- Call cost settings ---")
        print("1. Call cost limit")
        print("2. Show costs in")
        show_home_option()

        costsettingschoice = int(input(":  "))

        if costsettingschoice == home_code:
            return go_home()

        if costsettingschoice == 0:
            print("-> Back to CALL REGISTER")

    return False


def call_register_menu():
    callregister = 1

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
        show_home_option()

        callregister = int(input(":  "))

        if callregister == home_code:
            return go_home()

        match callregister:
            case 5:
                if call_duration_menu():
                    return True

            case 6:
                if call_costs_menu():
                    return True

            case 7:
                if call_cost_settings_menu():
                    return True

            case 0:
                print("-> Back to MAIN MENU")

            case _:
                print("Invalid input.")

    return False


def tones_menu():
    toneschoice = 1

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
        show_home_option()

        toneschoice = int(input(":  "))

        if toneschoice == home_code:
            return go_home()

        if toneschoice == 0:
            print("-> Back to MAIN MENU")

    return False


def call_settings_menu():
    callsettingschoice = -1

    while callsettingschoice != 0:
        print("\n--- Call settings ---")
        print("1. Automatic redesign")
        print("2. Speed dialing")
        print("3. Call waiting options")
        print("4. Own number sending")
        print("5. Phone line in use")
        print("6. Automatic answer")
        show_home_option()

        callsettingschoice = int(input(":  "))

        if callsettingschoice == home_code:
            return go_home()

        if callsettingschoice == 0:
            print("-> Back to SETTINGS")

    return False


def phone_settings_menu():
    phonesettingschoice = 1

    while phonesettingschoice != 0:
        print("\n--- Phone settings ---")
        print("1. Language")
        print("2. Cell info display")
        print("3. Welcome note")
        print("4. Network selection")
        print("5. Lights")
        print("6. Confirm SIM service actions")
        show_home_option()

        phonesettingschoice = int(input(":  "))

        if phonesettingschoice == home_code:
            return go_home()

        if phonesettingschoice == 0:
            print("-> Back to SETTINGS")

    return False


def security_settings_menu():
    securitychoice = 1

    while securitychoice != 0:
        print("\n--- Security settings ---")
        print("1. PIN code request")
        print("2. Call barring service")
        print("3. Fixed dialing")
        print("4. Closed user group")
        print("5. Phone security")
        print("6. Change access codes")
        show_home_option()

        securitychoice = int(input(":  "))

        if securitychoice == home_code:
            return go_home()

        if securitychoice == 0:
            print("-> Back to SETTINGS")

    return False


def settings_menu():
    settingschoice = 1

    while settingschoice != 0:
        print("\n========== SETTINGS ==========")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")
        show_home_option()

        settingschoice = int(input(":  "))

        if settingschoice == home_code:
            return go_home()

        match settingschoice:
            case 1:
                if call_settings_menu():
                    return True

            case 2:
                if phone_settings_menu():
                    return True

            case 3:
                if security_settings_menu():
                    return True

            case 0:
                print("-> Back to MAIN MENU")

            case _:
                print("Invalid input.")

    return False


def clock_menu():
    clockchoice = 1

    while clockchoice != 0:
        print("\n========== CLOCK ==========")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date setting")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")
        show_home_option()

        clockchoice = int(input(":  "))

        if clockchoice == home_code:
            return go_home()

        if clockchoice == 0:
            print("-> Back to MAIN MENU")

    return False


def power_down():
    print("Omo finally")
    print("_-_-POWERING DOWN-_-_")


def main():
    power_up()

    while True:
        show_main_menu()

        choice = input(":  ")

        match choice:
            case "0":
                power_down()
                break

            case "1":
                phonebook_menu()

            case "2":
                messages_menu()

            case "3":
                print("-> Chat...")

            case "4":
                call_register_menu()

            case "5":
                tones_menu()

            case "6":
                settings_menu()

            case "7":
                print("-> Call divert...")

            case "8":
                print("-> Games...")

            case "9":
                print("-> Calculator...")

            case "10":
                print("-> Reminders...")

            case "11":
                clock_menu()

            case "12":
                print("-> Profiles...")

            case "13":
                print("-> SIM services...")

            case "99":
                go_home()

            case _:
                print("Invalid selection.")


main()
