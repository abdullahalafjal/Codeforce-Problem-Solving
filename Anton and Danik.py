def determine_winner(s):
    anton_wins = s.count("A")
    danik_wins = s.count("D")

    if anton_wins > danik_wins:
        return "Anton"
    elif danik_wins > anton_wins:
        return "Danik"
    else:
        return "Friendship"


s = input("Enter the results of the games: ")
print(determine_winner(s))
