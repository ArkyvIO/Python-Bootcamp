# Create object for questions
class Question:
    # Initialize each question with question and answer
    def __init__(self, text, answer) -> None:
        """Initalize a question

        Args:
            question (_type_): Question text
            answer (_type_): Answer to question
        """
        # Set question to question
        self.text = text
        # Set answer to answer
        self.answer = answer
