import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QScrollArea, QWidget, QVBoxLayout
from dict_py import VocabularyBook

class VocabApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("MyVoca.ui", self)
        self.vocab_book = VocabularyBook()
        self.pushButton.clicked.connect(self.start)
        self.show()
        
    def start(self):
        vocab_cnt = self.spinBox.value()
        revise_cnt = self.spinBox_2.value()
        nw = TestUi(vocab_cnt, revise_cnt)
        nw.exec_()

        
class TestUi(QtWidgets.QDialog):
    def __init__(self, vocab_cnt, revise_cnt):
        super().__init__()

        self.vocab_count = vocab_cnt
        self.revise_count = revise_cnt
        self.meaning_inputs = {}
        uic.loadUi("Test.ui", self)
        self.setup_ui()

    def setup_ui(self):
        scroll_layout = QVBoxLayout()
        words_list = self.vocab_book.select_word(self.vocab_count, self.revise_count)
        for i in range(len(words_list)):
            word_layout = QHBoxLayout()
            meaning_layout = QHBoxLayout()

            word_label = QtWidgets.QLabel(f"Word: {words_list[i]}")
            meaning_label = QtWidgets.QLabel("Meaning:")
            meaning_input = QtWidgets.QLineEdit()
            self.meaning_inputs[words_list[i]] = meaning_input

            word_layout.addWidget(word_label)
            meaning_layout.addWidget(meaning_label)
            meaning_layout.addWidget(meaning_input)

            scroll_layout.addLayout(word_layout)
            scroll_layout.addLayout(meaning_layout)



        scroll_widget = QWidget()
        scroll_widget.setLayout(scroll_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        check_button = QtWidgets.QPushButton("Check Answers", self)
        check_button.clicked.connect(self.check_answers)
        main_layout.addWidget(check_button)

        self.setLayout(main_layout)

    def check_answers(self):
        for word, meaning_input in self.meaning_inputs.items():
            user_answer = meaning_input.text()
            correct = self.vocab_book.check_meaning(word, user_answer)
            if correct:
                meaning_input.setStyleSheet("color: green;")
            else:
                meaning_input.setStyleSheet("color: red;")

def main():
    app = QApplication(sys.argv)
    
    ex = VocabApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()