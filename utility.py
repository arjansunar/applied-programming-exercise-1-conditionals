def get_greatest(a,b,c):
    if a > b:
        if a > c:
            return a 
        else:
            return c
    elif b > c:
        return b
    else: 
        return c

def is_positive(num):
    return num >= 0 

def is_vowel(letter):
    return (letter == 'a') | (letter == 'e') | (letter == 'i') | (letter == 'o') | (letter == 'u') 

def is_alphabet(letter): 
    val= ord(letter)
    return (val >= ord('A')) & (val <= ord('z'))

def is_uppercase_or_lowercase_or_specialchar_or_digit(letter):
    val= ord(letter)
    if (val >= ord('A')) & (val <= ord('Z')):
        return "Uppercase"
    elif (val >= ord('a')) & (val <= ord('z')):
        return "Lowercase"
    elif (val >= ord('0')) & (val <= ord('9')):
        return "Digit"
    else: 
        return "Special Chars"

def is_even(num):
    return num % 2 == 0

def get_greatest_among_two_digits(a,b):
    return a if a > b else b

def is_leap_year(year):
    if (year % 400 == 0): 
        return True
    elif (year % 100 == 0): 
        return False
    elif (year % 4 == 0):
        return True
    else: return False 

# the date is assummed to have the format of yyyy-mm-dd
def is_correct_date(date):
    [year,month ,day] = map(lambda x: int(x),date.split('-'))
    return (year > 0 ) & ((month > 0) & (month <=12)) & (( day> 0) & (day <= 32))


# the date is assummed to have the format of yyyy-mm-dd
def is_eligible_for_vote(dob,current_year= 2021):
    year = int(dob.split('-')[0])
    return (current_year - year) >= 18 


def main():
    print(f'greatest: {get_greatest(7,10,9)}')
    print(f'is positive: {is_positive(0)}')
    print(f'is vowel: {is_vowel("b")}')
    print(f'is alphabet: {is_alphabet("*")}')
    print(f'is uppercase | lowercase | digit | special chars:  {is_uppercase_or_lowercase_or_specialchar_or_digit("*")}')
    print(f'is correct date: {is_correct_date("2020-13-10")}')
    print(f'is leap year: {is_leap_year(2012)}')

if __name__ == "__main__":
    main()