STYLE_LABEL = """
    QLabel {
        font-size: 22px;
        font-family: 'Trebuchet MS';
        margin: 10px;
        border: 2px solid #6c63ff;
        color: #f5f5f5;
        background: #2e2e2e;
        padding: 8px;
        border-radius: 8px;
    }
"""

STYLE_COLON = """
    QLabel {
        text-align: center;
        font-size: 24px;
        font-family: 'Verdana';
        color: black;
    }
"""

STYLE_ENTRY = """
    QLineEdit {
        height: 35px;
        padding: 5px;
        margin: 10px 0;
        font-size: 18px;
        font-family: 'Arial';
        border: 2px solid #4d4d4d;
        border-radius: 10px;
        background: #e6e6e6;
        color: #333;
    }
    
    QLineEdit:focus {
        border: 2px solid #6c63ff;
        background: #ffffff;
        color: #000000;
    }
"""

STYLE_BUTTON = """
    QPushButton {
        margin: 10px;
        color: #ffffff;
        font-size: 20px;
        background: #6c63ff;
        border: 2px solid #6c63ff;
        border-radius: 10px;
        padding: 10px;
    }
    
    QPushButton:hover {
        color: #6c63ff;
        background: #ffffff;
        border: 2px solid #6c63ff;
    }
    
    QPushButton:pressed {
        background: #4d4d4d;
        color: #ffffff;
        border: 2px solid #ffffff;
    }
"""

STYLE_MESSAGEBOX = """
    QMessageBox {
        background-color: #2e2e2e;
        color: #f5f5f5;
        font-size: 18px;
        font-family: 'Trebuchet MS';
        border: 2px solid #6c63ff;
        padding: 10px;
    }

    QMessageBox QLabel {
        color: #f5f5f5;
    }

    QMessageBox QPushButton {
        background-color: #6c63ff;
        color: #ffffff;
        font-size: 18px;
        border: 2px solid #6c63ff;
        border-radius: 10px;
        padding: 8px 16px;
    }

    QMessageBox QPushButton:hover {
        background-color: #ffffff;
        color: #6c63ff;
    }

    QMessageBox QPushButton:pressed {
        background-color: #4d4d4d;
        color: #ffffff;
    }
"""