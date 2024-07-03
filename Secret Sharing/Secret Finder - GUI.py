from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QLineEdit

timeout = 5000

class Window_SF(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(390)
        self.setFixedHeight(400)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setWindowTitle("Secret Finder")
        
        self.person_tokens_label = QLabel("Enter the identity number, token", self)
        self.person_tokens_label.setFixedWidth(200)
        self.person_tokens_label.move(15, 10)
        
        self.person_token_text_edit = QTextEdit(self)
        self.person_token_text_edit.setFixedSize(360, 215)
        self.person_token_text_edit.move(15, 50)
        
        self.get_secret_button = QPushButton(self)
        self.get_secret_button.setFixedSize(100, 25)
        self.get_secret_button.setText("Get Secret")
        self.get_secret_button.move(140, 280)
        
        self.secret_label = QLabel("The secret is", self)
        self.secret_label.setFixedWidth(200)
        self.secret_label.move(95, 330)
        
        self.secret_line_edit = QLineEdit(self)
        self.secret_line_edit.setFixedWidth(100)
        self.secret_line_edit.move(180, 330)
        self.secret_line_edit.setEnabled(False)
        
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("   Ready", timeout)
        
        self.get_secret_button.clicked.connect(self.find_secret)
        
        self.show()
        
    def find_secret(self, _):
        global person_token
        person_token = []
        try:
            person_token_input = self.person_token_text_edit.toPlainText()
            person_token_temp = person_token_input.split("\n")
            for i in person_token_temp:
                if i :
                    person_token.append(i.split(", "))
            global secret
            secret = 0
            for i in person_token:
                lagrange_value = 1
                x = 0
                for j in person_token:
                    if int(j[0]) != int(i[0]):
                        lagrange_value *= (x-int(j[0]))/(int(i[0])-int(j[0]))
                secret += lagrange_value * int(i[1])
            self.secret_line_edit.setEnabled(True)
            self.secret_line_edit.setText(str(abs(round(secret))))
            self.status_bar.showMessage("   The secret has been retrieved. If incorrect, quorum is not met", timeout)
        except:
            self.status_bar.showMessage("   Error, please re-enter", timeout)
            self.person_token_text_edit.clear()
            
app = QApplication([])
window_sf = Window_SF()
app.exec()