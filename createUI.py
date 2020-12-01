import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QStackedLayout, QGroupBox)

class UI (QWidget):
    def __init__(self):
        self.matA = []
        self.matB = []
        super().__init__()

    def draw_preUI(self):
        self.setGeometry(500, 400, 300, 200)
        self.setWindowTitle("선형대수")
        hbox1, vbox2, self.hbox3, self.vbox4, self.hbox5, self.vbox = QHBoxLayout(), QVBoxLayout(), QHBoxLayout(), QVBoxLayout(), QHBoxLayout(), QVBoxLayout()
        titleText1 = QLabel("프로그램 이름")
        titleText1.setAlignment(Qt.AlignCenter)
        explainText1 = QLabel("가우스 소거법의 forward elimination 단계,\n행렬의 곱셈, 역행렬 계산의 과정을 단계별로\n확인하며 원리를 공부할 수 있는 프로그램입니다.")
        explainText1.setAlignment(Qt.AlignCenter)
        self.vbox4.addWidget(titleText1)
        self.vbox4.addWidget(explainText1)
        makerText1 = QLabel("소프트웨어프로젝트 II")
        makerText2 = QLabel("서기선 곽우진 안시현")
        vbox2.addWidget(makerText1)
        vbox2.addWidget(makerText2)
        self.whichMethod = QComboBox()
        self.whichMethod.addItem("1 Forward Elimination")
        self.whichMethod.addItem("2 역행렬 구하기")
        self.whichMethod.addItem("3 행렬의 곱셈")
        self.hbox3.addWidget(self.whichMethod)
        startButton = QPushButton("시작!")
        startButton.clicked.connect(self.startClicked)
        hbox1.addStretch(1)
        hbox1.addWidget(startButton)
        self.hbox5.addLayout(vbox2)
        self.hbox5.addLayout(hbox1)

        self.vbox.addLayout(self.vbox4)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox5)
        self.setLayout(self.vbox)
        self.show()

    def startClicked(self):
        # if self.whichMethod.currentText().startswith("1") :
        self.draw_mainUI()
        print(self.whichMethod.currentText()[0])
        return self.whichMethod.currentText()[0]

    def inputClicked(self):
        self.matA.append(list(self.inputText.text()))
        for arr in self.matA :
            text = ""
            for i in range(len(arr)) :
                text += str(arr[i])
        self.display1.append(text)

    def draw_mainUI(self):
        self.setGeometry(500, 400, 460, 550)
        self.setWindowTitle("선형대수 풀이")
        expText, self.inputText, inputButton = QTextEdit(), QLineEdit(), QPushButton("입력")
        inputButton.clicked.connect(self.inputClicked)
        self.inputText.setFixedWidth(self.inputText.width() - 500)
        self.display1, self.display2 = QTextEdit(), QTextEdit()
        font = self.display1.font()
        font.setPointSize(font.pointSize() + 7)
        self.display1.setFont(font)
        self.display1.setAlignment(Qt.AlignCenter)
        self.display1.setReadOnly(True)
        font2 = self.display2.font()
        font2.setPointSize(font2.pointSize() + 7)
        self.display2.setFont(font2)
        self.display2.setAlignment(Qt.AlignCenter)
        self.display2.setReadOnly(True)
        nextButton, backButton = QPushButton("▶"), QPushButton("◀")
        display_box, text_box, button_box, box = QHBoxLayout(), QHBoxLayout(), QHBoxLayout(), QVBoxLayout()
        text_box.addStretch(1)
        text_box.addWidget(expText)
        text_box.addWidget(self.inputText)
        text_box.addStretch(1)
        text_box.addWidget(inputButton)
        display_box.addWidget(self.display1)
        display_box.addWidget(self.display2)
        button_box.addStretch(3)
        button_box.addWidget(backButton)
        button_box.addStretch(1)
        button_box.addWidget(nextButton)
        button_box.addStretch(3)
        box.addLayout(text_box)
        box.addLayout(display_box)
        box.addLayout(button_box)
        self.setLayout(box)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.draw_mainUI()
    sys.exit(app.exec_())
    if ui.buttonClicked() in ["1", "2", "3", 1, 2, 3] :
        ui.hide()
        del ui
        x = UI()
        x.draw_mainUI()