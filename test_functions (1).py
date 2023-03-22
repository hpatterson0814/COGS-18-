def test_quiz_questions():
    assert callable(quiz_questions)
    assert isinstance(quiz_questions('a'), int)

def test_determine_age():
    assert callable(determine_age)
    assert isinstance(determine_age(19), str)
    assert determine_age(10) == "It looks like you are 10-20 years old."
    assert determine_age(10) == "It looks like you are >30 years old."

def test_are_we_correct():
    assert callable(are_we_correct)
    assert are_we_correct(yes) == 'Hooray!'
    assert are_we_correct(No) == 'Hmm. Are you sure? I am never wrong!'