
import time
import random
import smtplib


class Moods:
    def happy(self):
        lines = open("/Users/maimounacamara/Downloads/happy1.txt").read().splitlines()
        line = random.choice(lines)
        return line
    def sad(self):
        lines = open("/Users/miry/Downloads/sad.txt").read().splitlines()
        line = random.choice(lines)
        return line
    def anxious(self):
        lines = open("/Users/miry/Downloads/anxious.txt").read().splitlines()
        line = random.choice(lines)
        return line
    def upset(self):
        lines = open("/Users/miry/Downloads/upset.txt").read().splitlines()
        line = random.choice(lines)
        return line
    def annoyed(self):
        lines = open("/Users/miry/Downloads/annoyed.txt").read().splitlines()
        line = random.choice(lines)
        return line

def main():
        print("*************************************************")
        print("Welcome to Affirm Now")
        print(time.strftime("The Current Time is: %H:%M:%S"))
        print("How are you feeling?")
        print("Please enter an emotion based on how you are feeling, "
      "1=happy,"
          "2= sad, "
          "3=anxious, "
          "4=upset, "
          "5=annoyed")
        global mood

        while True:
            try:
                mood = float(input("Please enter your mood:"))
                if mood==1 or mood==2 or mood==3 or mood==4 or mood==5:
                    break
            except:
                print("Please enter one of the numbers")
                continue
        moodsInst = Moods()

        if mood==1:
            print(moodsInst.happy())
            affirm = int(input("Do you want to add new: Enter 1 for 'Yes', Enter 2 for 'No"))
            if affirm==1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                for i in range(0, 1):
                    name = input("Enter a new affirmation:")
                    file.write(name + "\n")
                file.close()
                # Send goodbye message w/ information
            else:
                print("Bye!")

        elif mood==2:
            print(moodsInst.sad())
            affirm = int(input("Do you want to add new: Enter 1 for 'Yes', Enter 2 for 'No"))
            if affirm == 1:
                filename = "/Users/miry/Downloads/sad.txt"
                file = open(filename, 'a')
                for i in range(0, 1):
                    name = input("Enter a new affirmation:")
                    file.write(name + "\n")
                file.close()
                # Send goodbye message w/ information
            else:
                print("Bye!")

        elif mood==3:
            print(moodsInst.anxious())
            affirm = int(input("Do you want to add new: Enter 1 for 'Yes', Enter 2 for 'No"))
            if affirm == 1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                for i in range(0, 1):
                    name = input("Enter a new affirmation:")
                    file.write(name + "\n")
                file.close()
                #Send goodbye message w/ information
            else:
                print("Bye!")

        elif mood==4:
            print(moodsInst.upset())
            affirm = int(input("Do you want to add new: Enter 1 for 'Yes', Enter 2 for 'No"))
            if affirm == 1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                for i in range(0, 1):
                    name = input("Enter a new affirmation:")
                    file.write(name + "\n")
                file.close()
                # Send goodbye message w/ information
            else:
                print("Bye!")

        elif mood==5:
            print(moodsInst.annoyed())
            affirm = int(input("Do you want to add new: Enter 1 for 'Yes', Enter 2 for 'No"))
            if affirm == 1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                for i in range(0, 1):
                    name = input("Enter a new affirmation:")
                    file.write(name + "\n")
                file.close()
                # Send goodbye message w/ information
            else:
                print("Bye!")


if __name__ == "__main__":
    main()

