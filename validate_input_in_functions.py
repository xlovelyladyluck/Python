def score_input(test_name, test_score=0, invalid_message="Invalid test score, Try Again."):
    """This function is meant to take the test name, score and validate that test score is in range.
    If it's not in range, it is meant to provide an invalid message

    @param test_name: This is user input test name
    @param test_score: This is user input test score. Default value is 0, but must be between 0-100
    @return: If all inputs are valid, the test name will be returned with test score. If invalid,
    an invalid message will be returned.
    @raise invalid_message: Gives an error message of invalidity
    :param invalid_message: "Invalid test score, Try again." """
    # return { test_name: test_score}

    name = input("Please provide the name of your test.")
    try:
        score = int(input("Please enter your test score."))

        if 0 <= score <= 100:
            result = name+" : "+str(score)
        else:
            result = invalid_message

    except ValueError as invalid_message:
        print(invalid_message)
    else:
        return result


if __name__ == '__main__':
    print(score_input("Please provide the name of your test.","Enter your test score.", "Invalid test score, Try Again."))

"""I had a really tough time again with this one as far as getting what I wanted, but I felt more confident when I made my tests first as it set the
idea in place for what I wanted to do first. It did feel like this went a bit better than the ones before as I happened to get the correct out come 
 through testing repeatedly until I found most of the bugs. I don't think it's perfect, but it is definitely an improvement."""
