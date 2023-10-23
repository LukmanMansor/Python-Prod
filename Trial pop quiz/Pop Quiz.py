from question import Question

question_prompt = [
    "1. What country has the highest life expectancy?\n(a) Hong Kong\n(b) New York\n(c) Las vegas\n ",
    "2. Who was the Ancient Greek God of the Sun?\n(a) Freya\n(b) Apollo\n(c) Zeus\n ",
    "3. What car manufacturer had the highest revenue in 2020?\n(a) Toyota\n(b) Mercedes\n(c) Volkswagen\n ",
    "4. How many elements are in the periodic table?\n(a) 118\n(b) 123\n(c) 110\n ",
    "5. How many ghosts chase Pac-Man at the start of each game?\n(a) 4\n(b) 5\n(c) 3\n ",
    "6. Which planet has the most moons?\n(a) Earth\n(b) Pluto\n(c) Saturn\n ",
    "7. What country has won the most World Cups?\n(a) Argentina\n(b) Brazil\n(c) England\n ",
    "8. How many bones do we have in an ear?\n(a) 3\n(b) None\n(c) 2\n ",
    "9. What Netflix show had the most streaming views in 2021?\n(a) Your Name\n(b) Squid Game\n(c) Cafe Minamdang\n ",
    "10. What is Arie favourite colour?\n(a) Brown\n(b) Purple\n(c) Pink\n "
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c"),
    Question(question_prompt[3], "a"),
    Question(question_prompt[4], "a"),
    Question(question_prompt[5], "c"),
    Question(question_prompt[6], "b"),
    Question(question_prompt[7], "a"),
    Question(question_prompt[8], "b"),
    Question(question_prompt[9], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Hey, you got " + str(score) + " out of " + str(len(questions)) + " question correct!")


run_test(questions)
