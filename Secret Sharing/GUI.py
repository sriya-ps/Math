### Secret Sharing ###

# This program contains a Token Generator and Secret Finder
# Token Generator generates tokens for each person based on a secret
# Secret Finder computes the secret based on the input tokens

### Imports ###

from PyQt6.QtGui import \
    QIcon

from PyQt6.QtWidgets import \
    QApplication, \
    QMainWindow, \
    QLabel, \
    QPushButton, \
    QTextEdit, \
    QLineEdit

import random

### Global constants ###

# Maximum Length of secret

maximum_length = 10

# Maximum number of tokens that can be generated

maximum_tokens = 10

# Minimum number of tokens that need to be generated

minimum_tokens = 3

# Range of polynomial coefficients randomly selected for generating tokens

minimum_coefficient = 100000
maximum_coefficient = 999999

# Status bar message time-out

timeout = 5000

### Main application window ###

class Window_Menu(QMainWindow):
    
    # Initialise window
    
    def __init__(self):
        super().__init__()

        # Dimensions, icon, title of Main window
        
        self.setFixedWidth(270)
        self.setFixedHeight(50)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setWindowTitle("Secret Sharing")
        
        # Token Generator button
        
        self.tg_button = QPushButton(self)
        self.tg_button.setFixedSize(100, 25)
        self.tg_button.setText("Token Generator")
        self.tg_button.move(15, 12)
        
        # Secret Finder button
        
        self.sf_button = QPushButton(self)
        self.sf_button.setFixedSize(100, 25)
        self.sf_button.setText("Secret Finder")
        self.sf_button.move(150, 12)
        
        # Connectors when buttons are clicked
        
        self.tg_button.clicked.connect(self.launch_tg)
        self.sf_button.clicked.connect(self.launch_sf)
        
        # Initialisation complete, show the Main window
        
        self.show()
        
    # Launch Token Generator window
    
    def launch_tg(self, _):
        self.window_tg = Window_TG()

    # Launch Secret Finder window
    
    def launch_sf(self, _):
        self.window_sf = Window_SF()

### Token Generator Window ###
        
class Window_TG(QMainWindow):
    
    # Initialise window
        
    def __init__(self):
        super().__init__()

        # Dimensions, icon, title of Token Generator window
        
        self.setFixedWidth(390)
        self.setFixedHeight(400)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setWindowTitle("Token Generator")
        
        # User input of secret
        
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
        
        # User input of total tokens to be generated
        
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
        
        # User input of quorum tokens
        
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
        
        # Output of generated tokens
        
        self.person_token_text_edit = QTextEdit(self)
        self.person_token_text_edit.setFixedSize(360, 215)
        self.person_token_text_edit.move(15, 150)
        self.person_token_text_edit.setEnabled(False)
        
        # Status bar message
        
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("   Ready", timeout)
        
        # Connectors when buttons are clicked
        
        self.secret_button.clicked.connect(self.get_secret)
        self.total_tokens_button.clicked.connect(self.get_total_tokens)
        self.quorum_tokens_button.clicked.connect(self.get_quorum_tokens)
        
        # Initialisation completed, show the Token Generator window
        
        self.show()
        
    # User input of secret with validations
    
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
    
    # User input of total tokens to be generated with validations
    
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
    
    # User input of quorum token with validations
    # Also generate the tokens if all inputs are valid
    
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

### Functions called by the Token Generator ###
            
# Function to generate the random coefficients
# Also call function to evaluate the token and construct the output

def generate_tokens():
    global coefficients, person_token
    coefficients = [secret]
    person_token = []
    for i in range(1, quorum_tokens):
        coefficients.append(random.randint(minimum_coefficient, maximum_coefficient))
    for i in range(1, total_tokens + 1):
        person_token.append([i, evaluate_token(i)])
        
# Function to evaluate the token for each person

def evaluate_token(person):
    token = 0
    for i in range(0, len(coefficients)):
        token += coefficients[i] * (person ** i)
    return token

### Secret Finder Window ###

class Window_SF(QMainWindow):
    
    # Initialise window
    
    def __init__(self):
        super().__init__()

        # Dimensions, icon, title of Secret Finder window
        
        self.setFixedWidth(390)
        self.setFixedHeight(400)
        self.setWindowIcon(QIcon("Icon.png"))
        self.setWindowTitle("Secret Finder")
        
        # User input of person identity and token
        
        self.person_tokens_label = QLabel("Enter the identity number, token", self)
        self.person_tokens_label.setFixedWidth(200)
        self.person_tokens_label.move(15, 10)
        
        self.person_token_text_edit = QTextEdit(self)
        self.person_token_text_edit.setFixedSize(360, 215)
        self.person_token_text_edit.move(15, 50)     

        # Output to show the computed secret
        
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
        
        # Status bar message
        
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("   Ready", timeout)
        
        # Connector to get the secret
        
        self.get_secret_button.clicked.connect(self.find_secret)
        
        # Initialisation completed, show the Secret Finder window
        
        self.show()
        
    # User input of secret with validations
    # Also compute the secret and display if all validations are passed
    
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
                        lagrange_value *= (x - int(j[0])) / (int(i[0]) - int(j[0]))
                secret += lagrange_value * int(i[1])
            self.secret_line_edit.setEnabled(True)
            self.secret_line_edit.setText(str(abs(round(secret))))
            self.status_bar.showMessage("   The secret has been retrieved. If incorrect, quorum is not met", timeout)
        except:
            self.status_bar.showMessage("   Error, please re-enter", timeout)
            self.person_token_text_edit.clear()

### Main program ###

# Initialise and execute the PyQt app Main window

app = QApplication([])
window_menu = Window_Menu()
app.exec()

### End of program