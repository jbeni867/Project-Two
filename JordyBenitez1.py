# Author: Jordy Benitez
# Assignment: Lab 01

def main():
    biancaScore = 0
    edwardScore = 0
    feliciaScore = 0

    userInput = vote_menu()
    while userInput != "x":
        userVote = candidate_menu()

        if userVote == 1:
            biancaScore += 1
            print("Voted Bianca")
        elif userVote == 2:
            edwardScore += 1
            print("Voted Edward")
        elif userVote == 3:
            feliciaScore += 1
            print("Voted Felicia")

        userInput = vote_menu()

    print(f'''----------------------------------
Bianca = {biancaScore}, Edward = {edwardScore}, Felicia = {feliciaScore}, Total = {biancaScore + edwardScore + feliciaScore}
----------------------------------''')
    quit()

def vote_menu():
    voteMenu = """----------------------------------
VOTE MENU
----------------------------------
v:Vote
x:Exit
Option: """

    userResponse = input(voteMenu).strip().lower()
    
    while userResponse != "x" and userResponse != "v":
        userResponse  = input("Invalid (v/x): ").strip().lower()
    
    return userResponse
    
def candidate_menu():
    candidateMenu = """----------------------------------
CANDIDATE MENU
----------------------------------
1: Bianca
2: Edward
3: Felicia 
Candidate: """

    userResponse = input(candidateMenu).strip()
    
    while not userResponse.isnumeric() or int(userResponse) not in [1,2,3]:
        if not userResponse.isnumeric():
            userResponse = input("Answer must be numeric: ").strip()
        elif int(userResponse) not in [1,2,3]:
            userResponse = input("Invalid(1/2/3): ").strip()
    
    return int(userResponse)

if __name__ == "__main__":
    main()