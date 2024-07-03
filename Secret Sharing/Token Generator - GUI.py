from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QLineEdit
import random

maximum_length = 10
maximum_tokens = 9
minimum_tokens = 3
maximum_coefficient = 999999
minimum_coefficient = 100000
timeout = 5000

class Window_TG(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(390)
        self.setFixedHeight(400)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setWindowTitle("Token Generator")
        
        self.secret_label = QLabel("Enter your secret integer", self)
        self.secret_label.setFixedWidth(200)
        self.secret_label.move(15, 10)
        
        self.secret_line_edit = QLineEdit(self)
        self.secret_line_edit.setFixedWidth(100)
        self.secret_line_edit.move(225, 10)
        
        self.secret_button = QPushButton(self)
        self.secret_button.setFixedSize(25, 25)
        self.secret_button.setText("GO")
        self.secret_button.move(350, 12)
        
        self.total_tokens_label = QLabel("Enter number of tokens", self)
        self.total_tokens_label.setFixedWidth(200)
        self.total_tokens_label.move(15, 50)
        
        self.total_tokens_line_edit = QLineEdit(self)
        self.total_tokens_line_edit.setFixedWidth(100)
        self.total_tokens_line_edit.move(225, 50)
        self.total_tokens_line_edit.setEnabled(False)
        
        self.total_tokens_button = QPushButton(self)
        self.total_tokens_button.setFixedSize(25, 25)
        self.total_tokens_button.setText("GO")
        self.total_tokens_button.move(350, 52)
        self.total_tokens_button.setEnabled(False)
        
        self.quorum_tokens_label = QLabel("Enter number of quorum tokens", self)
        self.quorum_tokens_label.setFixedWidth(200)
        self.quorum_tokens_label.move(15, 90)
        
        self.quorum_tokens_line_edit = QLineEdit(self)
        self.quorum_tokens_line_edit.setFixedWidth(100)
        self.quorum_tokens_line_edit.move(225, 90)
        self.quorum_tokens_line_edit.setEnabled(False)
        
        self.quorum_tokens_button = QPushButton(self)
        self.quorum_tokens_button.setFixedSize(25, 25)
        self.quorum_tokens_button.setText("GO")
        self.quorum_tokens_button.move(350, 92)
        self.quorum_tokens_button.setEnabled(False)
        
        self.person_token_text_edit = QTextEdit(self)
        self.person_token_text_edit.setFixedSize(360, 215)
        self.person_token_text_edit.move(15, 150)
        self.person_token_text_edit.setEnabled(False)
        
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("   Ready", timeout)
        
        self.secret_button.clicked.connect(self.get_secret)
        self.total_tokens_button.clicked.connect(self.get_total_tokens)
        self.quorum_tokens_button.clicked.connect(self.get_quorum_tokens)
        
        self.show()
        
    def get_secret(self, _):
        secret_input = self.secret_line_edit.text()
        if len(secret_input) > maximum_length:
            self.status_bar.showMessage("   The secret is too long, maximum - " + str(maximum_length), timeout)
            self.secret_line_edit.clear()
        else:
            try:
                global secret
                secret = abs(int(secret_input))
                self.total_tokens_line_edit.setEnabled(True)
                self.total_tokens_button.setEnabled(True)
                self.secret_line_edit.setEnabled(False)
                self.secret_button.setEnabled(False)
            except:
                self.status_bar.showMessage("   The secret needs to be an integer", timeout)
                self.secret_line_edit.clear()
                
    def get_total_tokens(self, _):
        total_tokens_input = self.total_tokens_line_edit.text()
        try:
            global total_tokens
            total_tokens = abs(int(total_tokens_input))
            if total_tokens > maximum_tokens:
                self.status_bar.showMessage("   There are too many tokens, maximum - " + str(maximum_tokens), timeout)
                self.total_tokens_line_edit.clear()
            elif total_tokens < minimum_tokens:
                self.status_bar.showMessage("   There are too less tokens, minimum - " + str(minimum_tokens), timeout)
                self.total_tokens_line_edit.clear()
            else :
                self.quorum_tokens_line_edit.setEnabled(True)
                self.quorum_tokens_button.setEnabled(True)
                self.total_tokens_line_edit.setEnabled(False)
                self.total_tokens_button.setEnabled(False)
        except:
            self.status_bar.showMessage("   The number of tokens needs to be an integer", timeout)
            self.total_tokens_line_edit.clear()
            
    def get_quorum_tokens(self, _):
        quorum_tokens_input = self.quorum_tokens_line_edit.text()
        try:
            global quorum_tokens
            quorum_tokens = abs(int(quorum_tokens_input))
            if quorum_tokens > total_tokens:
                self.status_bar.showMessage("   There are too many quorum tokens, maximum - " + str(total_tokens), timeout)
                self.quorum_tokens_line_edit.clear()
            elif quorum_tokens < minimum_tokens:
                self.status_bar.showMessage("   There are too less quorum tokens, minimum - " + str(minimum_tokens), timeout)
                self.quorum_tokens_line_edit.clear()
            else:
                self.quorum_tokens_line_edit.setEnabled(False)
                self.quorum_tokens_button.setEnabled(False)
                self.person_token_text_edit.setEnabled(True)
                generate_tokens()
                for i in person_token:
                    self.person_token_text_edit.append(str(i[0]) + ", " + str(i[1]))
        except:
            self.status_bar.showMessage("   The number of quorum tokens needs to be an integer", timeout)
            self.quorum_tokens_line_edit.clear()
            
def generate_tokens():
    global coefficients, person_token
    coefficients = [secret]
    person_token = []
    for i in range(1, quorum_tokens):
        coefficients.append(random.randint(minimum_coefficient, maximum_coefficient))
    for i in range(1, total_tokens + 1):
        person_token.append([i, evaluate_token(i)])
        
def evaluate_token(person):
    token = 0
    for i in range(0, len(coefficients)):
        token += coefficients[i] * (person**i)
    return token
      
app = QApplication([])
window_tg = Window_TG()
app.exec()