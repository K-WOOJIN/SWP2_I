import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel,
    QComboBox, QTextEdit, QGridLayout, QLineEdit)

class UI (QWidget):
    def __init__(self):
        self.matA = []
        self.matB = []
        super().__init__()

    def drawUI(self):
        self.setGeometry(500, 400, 800, 700)
        self.setWindowTitle("Linear Algebra")
        grid = QGridLayout()
        self.setLayout(grid)
        empty1 = QLabel(" ")
        grid.addWidget(empty1, 4, 0)
        titleText1 = QLabel("넘기면서 봐요, 선형대수")
        font = titleText1.font()
        font.setPointSize(font.pointSize() + 11)
        titleText1.setFont(font)
        titleText1.setAlignment(Qt.AlignCenter)
        grid.addWidget(titleText1, 0, 0, 1, 6)
        explainText1 = QLabel("가우스 소거법의 forward elimination 단계,\n행렬의 곱셈, 역행렬 계산의 과정을 단계별로\n확인하며 원리를 공부할 수 있는 프로그램입니다.")
        font = explainText1.font()
        font.setPointSize(font.pointSize() + 3)
        explainText1.setFont(font)
        explainText1.setAlignment(Qt.AlignCenter)
        grid.addWidget(explainText1, 1, 0)
        makerText1 = QLabel("소프트웨어프로젝트 II")
        font = makerText1.font()
        font.setPointSize(font.pointSize() + 5)
        makerText1.setFont(font)
        makerText2 = QLabel("서기선 곽우진 안시현")
        font = makerText2.font()
        font.setPointSize(font.pointSize() + 3)
        makerText2.setFont(font)
        makerText1.setAlignment(Qt.AlignCenter)
        makerText2.setAlignment(Qt.AlignCenter)
        grid.addWidget(makerText1, 5, 0)
        grid.addWidget(makerText2, 6, 0)
        self.whichMethod = QComboBox()
        font = self.whichMethod.font()
        font.setPointSize(font.pointSize() + 6)
        self.whichMethod.setFont(font)
        self.whichMethod.setMaximumHeight(400)
        self.whichMethod.addItem(" 1 Forward Elimination")
        self.whichMethod.addItem(" 2 역행렬 구하기")
        self.whichMethod.addItem(" 3 행렬의 곱셈")
        grid.addWidget(self.whichMethod, 2, 0)
        startButton = QPushButton("시작!")
        font = startButton.font()
        font.setPointSize(font.pointSize() + 3)
        startButton .setFont(font)
        grid.addWidget(startButton, 3, 0)
        startButton.clicked.connect(self.startClicked)
        # calculating. preUI와 mainUI 합치는 거 하기
        self.expText, self.inputText, inputButton = QTextEdit("설명란"), QLineEdit(), QPushButton("입력")
        grid.addWidget(inputButton, 1, 5)
        font = self.expText.font()
        font.setPointSize(font.pointSize() + 2)
        self.expText.setFont(font)
        grid.addWidget(self.inputText, 1, 4)
        self.expText.setFixedWidth(self.expText.width() - 400)
        self.expText.setFixedHeight(self.expText.height() - 300)
        grid.addWidget(self.expText, 1, 3)
        inputButton.clicked.connect(self.inputClicked)
        self.inputText.setFixedWidth(self.inputText.width() - 500)
        self.display1, self.display2 = QTextEdit(), QTextEdit()
        grid.addWidget(self.display1, 3, 3, 3, 4)
        grid.addWidget(self.display2, 3, 4, 3, 5)
        font = self.display1.font()
        font.setPointSize(font.pointSize() + 10)
        self.display1.setFont(font)
        self.display1.setReadOnly(True)
        font2 = self.display2.font()
        font2.setPointSize(font2.pointSize() + 10)
        self.display2.setFont(font2)
        self.display2.setReadOnly(True)
        nextButton, backButton = QPushButton("▶"), QPushButton("◀")
        grid.addWidget(nextButton, 6, 4, 1, 5)
        grid.addWidget(backButton, 6, 3)
        self.show()

    def startClicked(self):
        # if self.whichMethod.currentText().startswith("1") :
        print(self.whichMethod.currentText()[1])
        if int(self.whichMethod.currentText()[1]) == 1:
            self.expText.setText("Forward Elimination")
        elif int(self.whichMethod.currentText()[1]) == 2:
                self.expText.setText("역행렬 구하기")
        else : self.expText.setText("행렬의 곱셈")

    def inputClicked(self):
        self.matA.append(list(self.inputText.text()))
        for arr in self.matA :
            text = ""
            for i in range(len(arr)) :
                text += str(arr[i])
        self.display1.append(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.drawUI()
    sys.exit(app.exec_())