# Stopwatch GUI 

import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")
        self.setGeometry(900, 300, 400, 500)

        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False

        
        self.title_label = QLabel("Stopwatch")
        self.time_label = QLabel("00:00.00")
        
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        
        self.title_label.setStyleSheet("""
            font-size: 24px; 
            font-family: Arial; 
            color: #292929;
        """)
        self.time_label.setStyleSheet("""
            font-size: 60px; 
            font-family: Arial; 
            font-weight: bold;
            color: #292929;
        """)

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)

        main_layout.addWidget(self.title_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        main_layout.addStretch()
        main_layout.addWidget(self.time_label, alignment=Qt.AlignCenter)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)

        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    def update_time(self):
        """Called every 10ms"""
        current_elapsed = time.time() - self.start_time + self.elapsed_time
        minutes = int(current_elapsed // 60)
        seconds = int(current_elapsed % 60)
        centiseconds = int((current_elapsed % 1) * 100)
        
        self.time_label.setText(f"{minutes:02d}:{seconds:02d}.{centiseconds:02d}")

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.timer.start(10)        # Update every 10ms
            self.is_running = True

    def stop(self):
        if self.is_running:
            self.elapsed_time += time.time() - self.start_time
            self.timer.stop()
            self.is_running = False

    def reset(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.is_running = False
        self.time_label.setText("00:00.00")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
