import sys
from PyQt5 import QtWidgets
from database import Database

class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Últimos 10 Registros")
        self.setGeometry(100, 100, 600, 400)

        # Create layout
        layout = QtWidgets.QVBoxLayout()

        # Create a table to display registrations
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(8)  # Adjust based on the number of fields
        self.table.setHorizontalHeaderLabels(["Data", "Turno", "Processo", "Máquina", "Referência", "Refugos", "Produção", "Defeitos"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        # Fetch the last 10 registrations from the database
        db = Database()
        registrations = db.get_last_registrations(10)

        self.table.setRowCount(len(registrations))
        for row_index, row_data in enumerate(registrations):
            for column_index, item in enumerate(row_data):
                self.table.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(item)))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec_())