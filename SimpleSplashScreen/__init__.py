from PyQt5.QtWidgets import QApplication, QSplashScreen, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QCoreApplication

class SplashScreen(QSplashScreen):
    def __init__(self, path_to_image):
        self.app = QApplication([])
        super().__init__(QPixmap(path_to_image), Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Create a custom progress bar background
        self.progress_bar_bg = QLabel(self)
        self.progress_bar_bg.setGeometry(0, self.pixmap().height() - 20, self.pixmap().width(), 10)
        self.progress_bar_bg.setStyleSheet("background-color: #2d20a0;")
        self.progress_bar_bg.show()

        # Create a custom progress bar foreground
        self.progress_bar_fg = QLabel(self)
        self.progress_bar_fg.setGeometry(0, self.pixmap().height() - 20, 0, 10)
        self.progress_bar_fg.setStyleSheet("background-color: #0f50f0;")
        self.progress_bar_fg.show()
        self.show()

    def update_progress(self, percentage):
        width = int((percentage / 100) * self.pixmap().width())
        self.progress_bar_fg.setGeometry(0, self.pixmap().height() - 20, width, 10)
        QCoreApplication.processEvents()
        if percentage >= 100:
            self.close()
            self.app.quit()

    def mousePressEvent(self, event):
        # Ignore mouse press events to prevent the splash screen from disappearing
        pass
