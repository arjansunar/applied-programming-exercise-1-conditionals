import utility as ut

def user_input():
    while True:
        print(''' 
            1. Find the greates among three numbers 
            2. Is positive
            3. Is vowel 
            4. Is alphabet
            5. Is uppercase | lowercase | digit | special chars
            6. Is correct date
            7. Is leap year
            8. Is eligible for vote
            9. Is even
                ''')
        id = int(input("Enter the Id of the chosen question: "))
        
        if (id == 1):
            a= int(input("Enter 1st number: "))
            b= int(input("Enter 2nd number: "))
            c= int(input("Enter 3rd number: "))
            print(f'greatest: {ut.get_greatest(a,b,c)}')
        elif (id == 2): 
            num = int(input("Enter a number: "))
            print(f'is positive: {ut.is_positive(num)}')
        elif (id == 3): 
            char = input("Enter a character: ")
            print(f'is vowel: {ut.is_vowel(char)}')
        elif (id == 4): 
            char = input("Enter a character: ")
            print(f'is an alphabet: {ut.is_alphabet(char)}')
        elif (id == 5): 
            char = input("Enter a character: ")
            print(f'is uppercase | lowercase | digit | special chars:  {ut.is_uppercase_or_lowercase_or_specialchar_or_digit(char)}')
        elif (id == 6): 
            date = input("Enter a date in yyyy-mm-dd format: ")
            print(f'is correct date: {ut.is_correct_date(date)}')
        elif (id == 7): 
            year = int(input("Enter a year: "))
            print(f'is leap year: {ut.is_leap_year(year)}')
        elif (id == 8):
            year = input("Enter your DOB in yyyy-mm-dd format: ")
            print(f'is eligible to vote: {ut.is_eligible_for_vote(year)}')
        else: 
            num = int(input("Enter a number to check if it is even: "))
            print(f'is even: {ut.is_even(num)}')


        usr_in = input("Do you want to continue?\nIf yes press y: ") 
        if (usr_in.lower() != 'y'):
            break

if __name__ == "__main__":
    user_input()
