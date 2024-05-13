import sys
import asyncio
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class FullScreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Создание виджета для отображения веб-страницы
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)
        
        # Загрузка HTML страницы
        self.web_view.load(QUrl.fromLocalFile("C:/slipeos/applications/com.systemui/res/drawable/index.html"))
        
        # Установка размеров окна равными размерам экрана
        self.setGeometry(0, 0, 1680, 1050)  # Установите здесь размеры экрана вашего клиента
        
        # Развертывание окна на весь экран
        self.showFullScreen()

        # Добавление сокращения клавиатуры для кнопки Escape
        shortcut = QShortcut(Qt.Key_Escape, self)
        shortcut.activated.connect(self.return_to_previous_page)

    def return_to_previous_page(self):
        if self.web_view.history().canGoBack():
            self.web_view.back()

async def start_server():
    # Запуск сервера асинхронно
    subprocess.Popen(["python", "C:/slipeos/applications/com.systemui/server.py"])

async def main():
    # Запуск сервера
    server_process = subprocess.Popen(["python", "C:/slipeos/applications/com.systemui/server.py"])
    
    # Подождать, пока сервер не запустится
    await asyncio.sleep(2)  # Подставьте здесь необходимое вам время ожидания
    
    # Запуск приложения
    app = QApplication(sys.argv)
    window = FullScreenWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    asyncio.run(main())
