import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QScrollArea, QWidget, QVBoxLayout
from dict_py import VocabularyBook

class VocabApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.vocab_book = VocabularyBook()
        self.ui = uic.loadUi("MyVoca.ui", self)
        self.pushButton.clicked.connect(self.start)
        self.show()
        
    def start(self):
        vocab_cnt = self.spinBox.value()
        revise_cnt = self.spinBox.value()
        nw = TestUi(vocab_cnt, revise_cnt)
        nw.exec_()
        
class TestUi(QtWidgets.QDialog):
    def __init__(self, vocab_cnt, revise_cnt):
        super().__init__()
        self.vocab_count = vocab_cnt
        self.revise_count = revise_cnt
        uic.loadUi("Test.ui", self)
        self.setup_ui()

    def setup_ui(self):
        scroll_layout = QVBoxLayout()

        for _ in range(self.vocab_count + self.revise_count):
            word_layout = QHBoxLayout()
            meaning_layout = QHBoxLayout()

            word_label = QtWidgets.QLabel("Word:")
            word_input = QtWidgets.QLineEdit()
            meaning_label = QtWidgets.QLabel("Meaning:")
            meaning_input = QtWidgets.QLineEdit()

            word_layout.addWidget(word_label)
            word_layout.addWidget(word_input)
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
        self.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    ex = VocabApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()