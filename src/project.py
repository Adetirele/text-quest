
import sys
import pygame


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60

LEFT_TEXT_X = 28          # left padding for text
LEFT_TEXT_Y = 40          # top padding for text
LEFT_TEXT_MAX_WIDTH = 380 # keep text on left half (avoid right-side knight)

#piccies
INTRO_IMAGE_PATH = "TQ Intro.png"
TEACH_IMAGE_PATH = "TQ Teach.png"
END_IMAGE_PATH   = "TQ End.png"
QUEST_PATH  = "quest.ttf"

#soundz
INTRO_SOUND_PATH = "intro fanfare.mp3"
CORRECT_SOUND_PATH = "correct fanfare.mp3"
WRONG_SOUND_PATH = "incorrect sword clash.mp3"
FINAL_GOOD_SOUND_PATH = "final fanfare good.mp3"
FINAL_BAD_SOUND_PATH = "final fanfare bad.mp3"

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
            "A function is an action that the program you’re using to code already knows how to execute! Ah, I have a friend who is an executioner...\n"
            "Anyways, you can call a function by invoking it with parentheses. For example, to type text on screen, use the “print” function, which looks like this:\n"
            "print()\n"
            "To make our print function actually DO something, we put an argument inside the function’s parentheses, like this:\n"
            "print(\“Huzzah!\”)\n"
            "However, not every function is created equal. Some functions can only have certain kinds of arguments in them.\n\n"
            "What is the correct way to use a print function?\n"
            "A: Print(Huzzah!)    B: print(\“Huzzah!\”)"
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
            "name=input()\n"
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
            "Characters (char): single letters, symbols, or numbers (e.g., 'A', '?', '7')\n"
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

#make my text look goooooooood
def wrap_text(text, font, max_width):
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split(" ")
        current = ""
        for w in words:
            test = (current + " " + w) if current else w
            if font.size(test)[0] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = w
        if current:
            lines.append(current)
    return lines

def render_wrapped(surface, text, font, color, x, y, max_width, line_spacing=6):
    lines = wrap_text(text, font, max_width)
    cursor_y = y
    for line in lines:
        img = font.render(line, True, color)
        surface.blit(img, (x, cursor_y))
        cursor_y += img.get_height() + line_spacing

#the "game" part of the game
class TextQuestGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Text Quest")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Load assets (scaled to window if nned be)
        self.intro_img = self.safe_load_image(INTRO_IMAGE_PATH)
        self.teach_img = self.safe_load_image(TEACH_IMAGE_PATH)
        self.end_img = self.safe_load_image(END_IMAGE_PATH)

        # Load font (yummy quest font)
        # Size 24 for body; 30 for headings, perhaps change later
        self.body_font = pygame.font.Font(QUEST_PATH, 15)
        self.title_font = pygame.font.Font(QUEST_PATH, 24)
        self.feedback_font = pygame.font.Font(QUEST_PATH, 15)

        # Game state
        self.state = "intro"          # intro, 4 lessons, end screenn
        self.lesson_index = 0
        self.correct_answered = False # spacebar only works after correct answer!!!!!!
        self.feedback_text = ""       # shows right/wrong feedback
        self.feedback_color = TEXT_COLOR

        # Score tracking (if i feel like it, might delete)__________________________________________________________
        self.score = 0

    def safe_load_image(self, path):
        try:
            img = pygame.image.load(path).convert_alpha()
            # If my image is the wrong size itll scale to the popup window
            if img.get_size() != (WINDOW_WIDTH, WINDOW_HEIGHT):
                img = pygame.transform.smoothscale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
            return img
        except Exception:
            # If ucant find the image, fill the background later
            return None
        
    def run(self):
        """Main loop."""
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            if not self.handle_events():
                pygame.quit()
                sys.exit()
            self.update(dt)
            self.render()

    def handle_events(self):
        """Event loop: quit, Esc, and key input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                self.handle_key(event.key)
        return True        
        
    def handle_key(self, key):
        """Keyboard rules per state."""
        if self.state == "intro":
            # Any key starts the lessons
            self.state = "lesson"
            self.correct_answered = False
            self.feedback_text = ""
            self.feedback_color = TEXT_COLOR
            return  
          
        if self.state == "lesson":
            lesson = LESSONS[self.lesson_index]
            # Only A/B keys count for answers
            if key == pygame.K_a:
                self.process_answer("A", lesson)
            elif key == pygame.K_b:
                self.process_answer("B", lesson)
            # Spacebar advances only if correct answer was given
            elif key == pygame.K_SPACE and self.correct_answered:
                self.advance_lesson()
        elif self.state == "end":
            pass

    def process_answer(self, choice, lesson):
        """Check answer and set feedback; lhlat progression until answer is right!!"""
        if choice == lesson["correct"]:
            self.correct_answered = True
            self.feedback_text = lesson["right_msg"]
            self.feedback_color = FEEDBACK_GOOD
            self.score += 1
        else:
            self.correct_answered = False
            self.feedback_text = lesson["wrong_msg"]
            self.feedback_color = FEEDBACK_BAD

    def advance_lesson(self):
        """Move to next lesson or end if finished."""
        self.lesson_index += 1
        self.correct_answered = False
        self.feedback_text = ""
        self.feedback_color = TEXT_COLOR
        if self.lesson_index >= len(LESSONS):
            self.state = "end"

    def update(self, dt):
        pass
    def render(self):
        """Draw current state."""
        if self.state == "intro":
            self.render_intro()
        elif self.state == "lesson":
            self.render_lesson()
        elif self.state == "end":
            self.render_end()
        pygame.display.flip()

    def render_intro(self):
        # Background
        if self.intro_img:
            self.screen.blit(self.intro_img, (0, 0))
        else:
            self.screen.fill((240, 240, 240))

    def render_lesson(self):
        # Background with teaching pyhtonious
        if self.teach_img:
            self.screen.blit(self.teach_img, (0, 0))
        else:
            self.screen.fill((255, 255, 255))

        # Lesson title
        lesson = LESSONS[self.lesson_index]
        title_text = f"Lesson {self.lesson_index + 1}: {lesson['title']}"
        title_img = self.title_font.render(title_text, True, TEXT_COLOR)
        self.screen.blit(title_img, (LEFT_TEXT_X, LEFT_TEXT_Y))

        # Body text wrapped to left area to avoid overlapping my knight
        render_wrapped(self.screen, lesson["body"], self.body_font, TEXT_COLOR,
                       LEFT_TEXT_X, LEFT_TEXT_Y + 50, LEFT_TEXT_MAX_WIDTH)    
        
        # Feedback text (shows right/wrong messages)
        if self.feedback_text:
            render_wrapped(self.screen, self.feedback_text, self.feedback_font, self.feedback_color,
                           LEFT_TEXT_X, WINDOW_HEIGHT - 120, LEFT_TEXT_MAX_WIDTH)

        # Bottom hint: spacebar rule (only if correct)
        hint = "Press SPACE to continue" if self.correct_answered else "Answer with A or B"
        hint_img = self.body_font.render(hint, True, TEXT_COLOR)
        self.screen.blit(hint_img, (LEFT_TEXT_X, WINDOW_HEIGHT - 60))

        # Optional score display
        score_msg = f"Score: {self.score}/{len(LESSONS)}"
        score_img = self.body_font.render(score_msg, True, TEXT_COLOR)
        self.screen.blit(score_img, (WINDOW_WIDTH - 180, 20))

    def render_end(self):
        # Background
        if self.end_img:
            self.screen.blit(self.end_img, (0, 0))
        else:
            self.screen.fill((230, 230, 240))

        # Farewell text!!!! sad to see u go
        combined_text = f"Quest Complete!   Final score: {self.score}/{len(LESSONS)}"
        combined_img = self.title_font.render(combined_text, True, TEXT_COLOR)
        combined_rect = combined_img.get_rect()
        combined_rect.centerx = WINDOW_WIDTH // 2
        combined_rect.y = LEFT_TEXT_Y  
        self.screen.blit(combined_img, combined_rect)


#main function
def main():
    game = TextQuestGame()
    game.run()

if __name__ == "__main__":
    main()