def count_upper_lower_case_characters():
    string = input('Enter the string :')
    upper_characters=0
    lower_characters=0
    for i in string:
        if i.isupper():
            upper_characters+=1
        if i.islower():
            lower_characters+=1
    print(f"No of upper characters in the given string : '{string} ' is {upper_characters}")
    print(f"No of lower characters in the given string : '{string} ' is {lower_characters}")
count_upper_lower_case_characters()

