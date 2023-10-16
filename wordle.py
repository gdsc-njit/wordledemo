from letter_state import LetterState

class Wordle:
    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.attempts = []
