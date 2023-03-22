def introduction():
    """Introduction statement
    
    Parameters
    ----------
    None
    
    Returns
    -------
    string
    """
    
    print (f"""Welcome! After answering the questions below the Magic Psychic 
will be able to guess your age range.🔮 Try to answer each question intuitively 
and quickly to avoid over-thinking. Answer by typing the letter of the option 
you wish to choose and then pressing 'Enter' on your keyboard.\n""")
    
introduction()


def quiz_questions():
    """Carries out the quiz questions 1-5
    
    Parameters
    ----------
    input(str): 'a', 'b', 'c', 'd'
    
    Returns
    -------
    score
    """
    
    global score
    score = 0

    print("Time for Breakfast. What are you eating?")
    Question_1 = input(f"A. French Toast\nB. Eggs and Bacon\nC. Cereal\nD. Oatmeal\n")
    Question_1 = Question_1.lower()
    if Question_1 == 'a':
        score = score + 2
    elif Question_1 == 'b':
        score = score + 4
    elif Question_1 == 'c':
        score = score + 1
    elif Question_1 == 'd':
        score = score + 3
        
    print ("Time for Lunch. What are you eating?")
    Question_2 = input(f"A. Club Sandwich\nB. Mac n' Cheese\nC. Salad\nD. Burrito\n")
    Question_2 = Question_2.lower()
    if Question_2 == 'a':
         score += 3
    elif Question_2 == 'b':
        score += 1
    elif Question_2 == 'c':
        score += 4
    elif Question_2 == 'd':
        score += 2

    print ("Time for a Snack. What are you eating?")
    Question_3 = input(f"A. Granola Bar\nB. Carrots\nC. Fruit Roll Up\nD. Muffin\n")
    Question_3 = Question_3.lower()
    if Question_3 == 'a':
         score += 3
    elif Question_3 == 'b':
        score += 4
    elif Question_3 == 'c':
        score += 1
    elif Question_3 == 'd':
        score += 2

    print("Time for Dinner. What are you eating?")
    Question_4 = input(f"A. Steak and Potatoes\nB. Dino Nuggets\nC. Grilled Cheese and Soup\nD. Chicken and Rice\n")
    Question_4 = Question_4.lower()
    if Question_4 == 'a':
         score += 4
    elif Question_4 == 'b':
        score += 1
    elif Question_4 == 'c':
        score += 2
    elif Question_4 == 'd':
        score += 3

    print("Time for Dessert. What are you eating?")
    Question_5 = input(f"A. Ice Cream\nB. Cookies and Milk\nC. Tiramisu\nD. Fruit Tart\n")
    Question_5 = Question_5.lower()
    if Question_5 == 'a':
         score += 2
    elif Question_5 == 'b':
        score += 1
    elif Question_5 == 'c':
        score += 4
    elif Question_5 == 'd':
        score += 3
    
quiz_questions()


def determine_age(score):
    """Produces result of quiz given inputs from quiz_questions
    
    Parameters
    ----------
    score: 5-20
    
    Returns
    -------
    str(result)
    """
    
    if score >= 16:
        print(f"It looks like you are >30 years old.🧓\n")
    elif score >= 11:
        print(f"It looks like you are 21-30 years old.🥳\n")
    elif score >= 6:
        print(f"It looks like you are 10-20 years old.🤓\n")
    else:
        print(f"It looks like you are <10 years old.👼\n")

determine_age(score)


def are_we_correct():
    """Asks the user if the guess was correct and produces
    a response statement
    
    Parameters
    ----------
    input(str): 'yes', 'no'
    
    Returns
    -------
    str
    """
    Question_6 = input(f'Was the age that the Magic Psychic guessed correct? Yes or No?\n')
    Question_6 = Question_6.lower()
    if Question_6 == 'yes':
        print ('Hooray!🎉')
    elif Question_6 == 'no':
        print ('Hmm. Are you sure? I am never wrong!🤨')
    else:
        print ("i couldn't understand that")
        
are_we_correct()



