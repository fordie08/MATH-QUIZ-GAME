import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont(None, 40)
BACKGROUND_COLOR = (189, 214, 238)  # Light blue
TEXT_COLOR = (33, 33, 33)  # Dark gray
CORRECT_COLOR = (85, 186, 118)  # Light green
INCORRECT_COLOR = (245, 108, 108)  # Light red

# Function to display text on screen
def display_text(text, x, y, color=TEXT_COLOR):
    screen_text = FONT.render(text, True, color)
    screen.blit(screen_text, [x, y])

# Function to display math question and input box
def display_question_with_input(question, x, y, text_input, input_box):
    display_text("Question: " + question, x, y)
    pygame.draw.rect(screen, TEXT_COLOR, input_box, 2)
    display_text(text_input, input_box.x + 5, input_box.y + 5)

# Function to generate a math question
def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

# Function to run the quiz
def run_quiz():
    questions_correct = 0
    answers = []
    for i in range(10):
        screen.fill(BACKGROUND_COLOR)
        question, answer = generate_question()
        input_box = pygame.Rect(300, 50, 200, 40)  # Input box position
        text_input = ''
        display_question_with_input(question, 50, 50, text_input, input_box)
        pygame.display.update()

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]
                    else:
                        text_input += event.unicode

            screen.fill(BACKGROUND_COLOR)
            display_question_with_input(question, 50, 50, text_input, input_box)
            pygame.display.update()

        # Check if answer is correct
        player_answer = int(text_input) if text_input.isdigit() else None
        if player_answer is not None and player_answer == answer:
            questions_correct += 1
            answers.append((question, answer, player_answer, True))
        else:
            answers.append((question, answer, player_answer, False))

        time.sleep(1)

    return questions_correct, answers

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quiz")

# Get player's name and section
player_name = input("Enter your name: ")
player_section = input("Enter your section: ")

# Run the quiz
score, answers = run_quiz()

# Display final score and correct answers
screen.fill(BACKGROUND_COLOR)
display_text("Quiz Over!", 300, 50)
display_text("Player: " + player_name, 50, 150)
display_text("Section: " + player_section, 50, 200)
display_text("Score: " + str(score) + "/10", 50, 250)

y_offset = 300
for i, (question, correct_answer, player_answer, is_correct) in enumerate(answers):
    y_offset += 50
    color = CORRECT_COLOR if is_correct else INCORRECT_COLOR
    display_text(f"Question {i+1}: {question}", 50, y_offset, color)
    if player_answer is not None:
        display_text(f"Your Answer: {player_answer}, Correct Answer: {correct_answer}", 50, y_offset + 25, color)
    else:
        display_text(f"You did not provide an answer. Correct Answer: {correct_answer}", 50, y_offset + 25, color)

pygame.display.update()

# Wait for player to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
