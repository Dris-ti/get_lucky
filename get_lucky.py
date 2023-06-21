import random as ran

score = 0
bst = 0
cur_user = {}
run_game = True


# ------------------------------


def new_game():
    user = ""
    opt = ["N", "P"]

    while user not in opt:
        user = input("Are you a new user or previous user? [N/P] : ").upper()
        print()

    if user == "N":
        write_info()
    else:
        take_info()


# ------------------------------


def write_info():
    user_name = str(input("Enter username: "))
    user_pass = str(input("Enter password: "))
    print()

    with open("info.txt", "a") as file:
        file.write(f"{user_name}, {user_pass}, {score}\n")

    check_info(user_name, user_pass)


# ------------------------------


def take_info():
    user_name = str(input("Enter username: "))
    user_pass = str(input("Enter password: "))
    print()
    check_info(user_name, user_pass)


# ------------------------------


def check_info(n, p):
    global cur_user
    ck = False

    with open("info.txt", "r") as file:
        for line in file:
            (key, value, scr) = line.split(", ")
            cur_user[key] = [value, scr]

        for key in cur_user:
            if key == n and cur_user[key][0] == p:
                check_guess(n, p)
                ck = True
        if ck is False:
            print("This username is not registered yet.\n")
            new_game()


# ------------------------------


def check_guess(n, p):
    global cur_user
    global score
    global bst
    global run_game
    sym = ["*", "#", "$"]
    stop = 'X'
    fst = ""
    snd = ""
    trd = ""
    line_num = 0

    while snd not in sym and stop:
        print("To stop, press 'X'")
        snd = str(input("Enter symbol [*, #, $] : "))

        if snd == 'X' or snd == 'x':
            run_game = False
            display_score(n, p)
            return

        print()
        fst = ran.choice(sym)
        trd = ran.choice(sym)
        # fst = "*"
        # trd = "*"
    print("\n-----------------------------------")
    print("{:^12}{:^12}{:^12}".format("Computer", n, "Computer"))
    print("{:^12}{:^12}{:^12}".format(fst, snd, trd))
    print("-----------------------------------\n")

    if fst == snd == trd:
        score += 10
        for key in cur_user:
            if key == n:
                break
            line_num += 1

        with open("info.txt") as file:
            lines = file.readlines()

        for key in cur_user:
            if key == n:
                bst = int(cur_user[key][1])

        if int(bst) < int(score):
            lines[line_num % 3] = f"{n}, {p}, {score}\n"
            bst = int(score)
            cur_user[n] = [f"{p}", f"{bst}"]

        with open("info.txt", "w") as file:
            for line in lines:
                file.write(line)
        display_score(n, p)

    else:
        bst = int(cur_user[n][1])
        display_score(n, p)


# ------------------------------


def display_score(n, p):
    global score
    global cur_user
    global bst

    if run_game:
        check_guess(n, p)
    else:
        print("\n--------------------------------")
        print("{:^17} {:^17}".format("Current Score", "Best Score"))
        print("{:^17} {:^17}".format(score, bst))
        print("--------------------------------\n")


# ------------------------------


if __name__ == '__main__':
    new_game()
