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

        calculate_button = QPushButton(' Calculate speed')
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel('')

        self.system = QComboBox()
        self.system.addItems(['Metrical (km)', 'Imperial (miles)'])

        # Add widgets to grid

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 3, 1)
        grid.addWidget(self.output_label, 4, 0, 1, 1)
        grid.addWidget(self.system, 0, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.time_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y').date().year
        age = current_year - year_of_birth
        self.output_label.setText(f'{self.distance_line_edit.text()} is {age} years old')



app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
