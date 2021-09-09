from question import Question

question_prompts = [
    "What color are apples? \n(a) Red/green\n(b) purple\n(c) orange\n\n",
    "What color are bananas? \n(a) teal\n(b) magenta\n(c) yellow\n\n",
    "What color are strawberries? \n(a) yellow\n(b) red\n(c) blue\n\n",

]

#This block of code creates an array called "questions" in which each element is an
#object from the "Question" class. Remember that the class created in the "question"
#file has two attributes: prompt and answer. As you can see below, the first attribute
#is going to pass the first line above (question prompts [0]) and the second attribute,
#answer, will be passed as "a".
questions_array = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions_array:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)))

run_test(questions_array)
