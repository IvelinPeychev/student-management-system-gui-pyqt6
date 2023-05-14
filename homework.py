import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QDialog, \
    QAbstractSlider, QListView, QGroupBox, QListWidget, QListWidgetItem, QScrollBar, QComboBox


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average speed calculator")

        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel('Distance: ')
        self.distance_line_edit = QLineEdit()

        time_label = QLabel('Time (hours): ')
        self.time_line_edit = QLineEdit()


        self.system = QComboBox()
        self.system.addItems(['Metrical (km)', 'Imperial (miles)'])

        calculate_button = QPushButton(' Calculate speed')
        calculate_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel('')

        # Add widgets to grid

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.system, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 3, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 1)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance / time
        match self.system.currentText():
            case 'Metrical (km)':
                speed = round(speed, 2)
                point = 'km/h'
            case 'Imperial (miles)':
                speed = round(speed*0.621371, 2)
                point = 'm/h'

        self.output_label.setText(f'Average speed: {speed} {point}')



app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
