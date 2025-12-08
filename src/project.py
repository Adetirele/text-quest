
import sys
import pygame


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60

LEFT_TEXT_X = 28          # left padding for text
LEFT_TEXT_Y = 40          # top padding for text
LEFT_TEXT_MAX_WIDTH = 380 # keep text on left half (avoid right-side art)

INTRO_IMAGE_PATH = "src/assets/TQ_intro.png"
TEACH_IMAGE_PATH = "src/assets/TQ_teach.png"
END_IMAGE_PATH   = "src/assets/TQ_end.png"
QUEST_FONT_PATH  = "src/assets/quest_font.ttf"

TEXT_COLOR = (0, 0, 0)      # black text
FEEDBACK_GOOD = (40, 150, 60)
FEEDBACK_BAD = (180, 40, 40)

# ------------------ lesson content startz here ------------------
LESSONS = [
    {
        "title": "Programming basics",
        "body": (
            "Hello there, fair squire! My name is Pythonious the Knight, and I am here to teach you all about coding!\n"
            "Also called programming, coding is how humans can talk to computers. Computer programs are a set of instructions written "
            "by humans to tell computers what to do.\n"
            "Unfortunately, we cannot speak to computers in plain English! We must communicate with them with something called a “programming language.”\n"
            "There are many different kinds of programming languages, but the one we are going to be using today is called Python. Hmm…\n"
            "Pythons remind me of dragons. Have you ever slain one before? Back to the point. With Python, you can give computers commands and "
            "make them do all sorts of silly things!\n\n"
            "Can we speak to computers in plain English?\n"
            "A: No    B: Yes"
        ),
        "correct": "A",
        "right_msg": "Excelsior! Answer A is correct. Onwards, to the next lesson!",
        "wrong_msg": "Blast! That’s not right—but that’s ok! Re-read the lesson and try again!"
    },
    {
        "title": "Functions",
        "body": (
            "A function is an action that the program you’re using to code already knows how to execute! Ah, I have a friend who is an executioner…\n"
            "Anyways, you can call a function by invoking it with parentheses. For example, to type text on screen, use the “print” function, which looks like this:\n"
            "print()\n"
            "To make our print function actually DO something, we put an argument inside the function’s parentheses, like this:\n"
            "print(\"Huzzah!\")\n"
            "However, not every function is created equal. Some functions can only have certain kinds of arguments in them.\n\n"
            "What is the correct way to use a print function?\n"
            "A: Print(Huzzah!)    B: print(\"Huzzah!\")"
        ),
        "correct": "B",
        "right_msg": "Protinus! Answer B is correct. Onwards! Press the spacebar to continue to the next lesson!",
        "wrong_msg": "Argh! That’s not right—but that’s ok! Re-read the lesson and try again!"
    },
    {
        "title": "Variables",
        "body": (
            "Variables are similar to containers that hold a program’s data. To give a variable something to hold on to, you must follow it with an assignment operator. "
            "I will be succeeded by my daughter, Pythonia the 4th. She is unyielding in battle!\n"
            "Ahem. Back to the lesson.\n"
            "An assignment operator gives value to variables. Here’s how to use one:\n"
            "name = input()\n"
            "“name” is the name of the variable and the equals sign is the assignment operator.\n\n"
            "What do variables do in programming languages?\n"
            "A: Hold a program’s data    B: Constantly change"
        ),
        "correct": "A",
        "right_msg": "Glory! Answer A is correct. Onwards! Press the spacebar to continue to the next lesson!",
        "wrong_msg": "Confound it! That’s not right—but that’s ok! Re-read the lesson and try again!"
    },
    {
        "title": "Data types",
        "body": (
            "Data types specify what kind of values a variable can hold, among other things. We will go over primitive data types, "
            "which are building blocks already given to you by the programming language you’re using. These include:\n"
            "Integers (int): whole numbers without decimal points (ex: 5, -100)\n"
            "Floating-point numbers (float): numbers with decimal points (ex: 3.14, -0.5)\n"
            "Characters (char): single letters, symbols, or numbers (e.g., 'A', '$', '7')\n"
            "Booleans (bool): true or false values.\n"
            "These data types are in their simplest form, and they help the computer understand what you mean when you code.\n\n"
            "What is an example of a data type?\n"
            "A: Primitive data type    B: Boolean"
        ),
        "correct": "B",
        "right_msg": "Excellent! Answer B is correct. Squire, you are well on your way to becoming a great knight! Press spacebar to continue.",
        "wrong_msg": "Hexes! That’s not right—but that’s ok! Re-read the lesson and try again!"
    }
]

def main():
    game = TextQuestGame()
    game.run()

if __name__ == "__main__":
    main()