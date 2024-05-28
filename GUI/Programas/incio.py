import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QLineEdit,QPushButton,QMessageBox,QCheckBox
from PyQt5.QtGui import QFont,QPixmap

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_UI()
    
    def inicializar_UI(self):
        self.setGeometry(200,200,400,250)
        self.setWindowTitle("Mi login")
        self.generaFormulario()
        self.show()

    def generaFormulario(self):
        self.is_logged=False

        user_label=QLabel(self)
        user_label.setText("Usuarios:")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,54)
        
        self.user_input=QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)

        password_label=QLabel(self)
        password_label.setText("Password:")
        password_label.setFont(QFont("Arial",10))
        password_label.move(20,86)
        
        self.password_input=QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90,82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.check_view_password=QCheckBox(self)
        self.check_view_password.setText("Ver contraseña")
        self.check_view_password.move(90,110)
        self.check_view_password.toggled.connect(self.view_password)

        login_button=QPushButton(self)
        login_button.setText("Login")
        login_button.resize(200,34)
        login_button.move(90,140)
        login_button.clicked.connect(self.view_login)

        register_button=QPushButton(self)
        register_button.setText("Register")
        register_button.resize(200,34)
        register_button.move(90,180)
        register_button.clicked.connect(self.view_register)

    def view_password(self,clicked):
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def view_login(self):
        pass

    def view_register(self):
        pass

if __name__=="__main__":
    app=QApplication(sys.argv)
    login=Login()
    sys.exit(app.exec())
