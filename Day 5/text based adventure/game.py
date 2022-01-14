name = input("Enter the name of your Charachter::")
print(f"Once there lived a young boy named {name} at homtownPallet Town. He was a very good magician. His magic wawords.He used to help everyone in his village but wasn’t unawarofthe outside world which was full of evil monsters. One dahedecided to move out and make the world evil-free.\n")


class Battle:
    def Arena1(Answer1):
        var = 2
        while var != 1:
            print("Welcome to city of Jeden ravaged by Devil1\n")
            print("Answer the Question to kill the devil or face hisWrath")
            print("How many wonders do we have in the world?")
            UserAnswer = int(input("Enter Your Answer::"))
            if (Answer1 == UserAnswer):
                print("Correct Answer! You sucessfully defeated thedevil")
                var -= 1
            else:
                print("Wrong Answer! You lost to the devil")

    def Arena2(Answer2):
        var = 2
        while var != 1:
            print("Welcome to city of Pedwar ravaged by Devil2\n")
            print("Answer the Question to kill the devil or face his Wrath")
            print("Which bird is the universal symbol of Peace?")
            UserAnswer = input("Enter Your Answer::")
            if (Answer2 == UserAnswer):
                print("Correct Answer! You sucessfully defeated the devil")
                var -= 1
            else:
                print("Wrong Answer! You lost to the devil")

    def Arena3(Answer3):
        var = 2
        while var != 1:

            print("Welcome to city of Hamza ravaged by Devil3\n")
            print("Answer the Question to kill the devil or face his Wrath")
            print("What causes Anemia? ")
            UserAnswer = input("Enter Your Answer::")
            if (Answer3 == UserAnswer):
                print("Correct Answer! You sucessfully defeated thedevil")
                var -= 1
            else:
                print("Wrong Answer! You lost to the devil")

    def Arena4(Answer4):
        var = 2
        while var != 1:
            print("Welcome to city of Strand ravaged by Devil4\n")
            print("Answer the Question to kill the devil or face his Wrath")
            print("Tsunamis are not caused by?")
            UserAnswer = input("Enter Your Answer::")
            if (Answer4 == UserAnswer):
                print("Correct Answer! You sucessfully defeated the devil")
                var -= 1
            else:
                print("Wrong Answer! You lost to the devil")

    def Arena5(Answer5):
        var = 2
        while var != 1:
            print("BOSS FIGHT!")
            print("Answer the Question to kill the devil or face his Wrath")
            print("Which one of the following ports is the oldest port in India?")
            UserAnswer = input("Enter Your Answer::")
            if (Answer5 == UserAnswer):
                print("Correct Answer! You sucessfully defeated thedevil")
                var -= 1
            else:
                print("Wrong Answer! You lost to the devil")
                break


def main():
    Battle.Arena1(Answer1=7)
    Battle.Arena2(Answer2="Dove")
    Battle.Arena3(Answer3="By Deficiency of Iodine")
    Battle.Arena4(Answer4="Hurricanes")
    Battle.Arena5(Answer5="Chennai")


main()
