import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from datetime import datetime
from database import Database
from registration_window import RegistrationWindow

class CalendarDialog(QDialog):
    def __init__(self, parent=None):
        super(CalendarDialog, self).__init__(parent)
        self.setWindowTitle("Select Date")
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.select_date)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        self.setLayout(layout)

    def select_date(self, date):
        self.selected_date = date.toString("dd/MM/yyyy")
        self.accept()

class DateInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)

        self.txtData = QLineEdit(self)
        self.txtData.setPlaceholderText("Data (dd/mm/yyyy)")
        self.layout.addWidget(self.txtData)

        self.calendar_button = QPushButton("📅", self)
        self.calendar_button.clicked.connect(self.show_calendar)
        self.layout.addWidget(self.calendar_button)

    def show_calendar(self):
        dialog = CalendarDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.txtData.setText(dialog.selected_date)

class ApontamentoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.database = Database()

    def initUI(self):
        self.setWindowTitle('Apontamento')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.date_input_widget = DateInputWidget()
        layout.addWidget(QLabel("Data:"))
        layout.addWidget(self.date_input_widget)

        layout.addWidget(QLabel("Turno:"))
        self.optionTurnoA = QRadioButton("Turno A")
        self.optionTurnoB = QRadioButton("Turno B")
        self.optionTurnoC = QRadioButton("Turno C")
        layout.addWidget(self.optionTurnoA)
        layout.addWidget(self.optionTurnoB)
        layout.addWidget(self.optionTurnoC)

        self.listaProcesso = QComboBox(self)
        self.listaProcesso.addItems(["Selecione o processo", "Vulcanização", "Montagem", "Construção", "Banner"])
        layout.addWidget(QLabel("Processo:"))
        layout.addWidget(self.listaProcesso)

        self.listaMaquina = QComboBox(self)
        self.listaMaquina.addItems(["Selecione a máquina","NKM 1", "NKM 2", "VP1", "VP2", "VP3", "VP4", "VP5", "VP6", "VP7", "VP8", "Embalagem", "14 bar", "Crimpagem", "Prensa 01", "Prensa 02", "Leaktest"])
        layout.addWidget(QLabel("Máquina:"))
        layout.addWidget(self.listaMaquina)

        self.listaReferencia = QComboBox(self)
        self.listaReferencia.addItems(["Selecione o produto", "LTS - 6174 N", "5S 8 -16.5 CT", "5S 8 -16.5 MB", "5S 8N-13", "5S 8K-17.5 CT", "5S 8K-17.5 MB", "5S 8A-19", "5S 8E-18 CT", "5S 8E-18 MB", "5S 8M - 16 CT", "5S 8M - 16 KL", "6S 9.5-13", "6S 9.5A-13", "9 10-16", "9 10-18.5", "9 10-19", "9 10-21", "9 9.5SP -14.4 CT", "9 9.5SP -14.4 MB", "9 9S - 12 KL", "9 9LS-13.5", "9 9KS-17.5", "11 10.5E-18 KL", "11 10.5E-18 CT", "11 10.5-19 CT", "11 10.5-21 KL", "11 10.5-21 IB", "11 10.5-21 CT", "11 10.5A-16", "11 10.5C-16", "11 10.5E-16 KL", "11 10.5-25"])
        layout.addWidget(QLabel("Referência:"))
        layout.addWidget(self.listaReferencia)

        self.txtProducao = QLineEdit(self)
        self.txtProducao.setPlaceholderText("Quantidade Produzida")
        layout.addWidget(QLabel("Quantidade Produzida:"))
        layout.addWidget(self.txtProducao)

        self.txtRefugos = QLineEdit(self)
        self.txtRefugos.setPlaceholderText("Refugos")
        layout.addWidget(QLabel("Refugos:"))
        layout.addWidget(self.txtRefugos)

        layout.addWidget(QLabel("Defeitos:"))
        defect_names = [
            "Bolhas", 
            "Trincas", 
            "Marcas", 
            "Bladder furado", 
            "Falha na crimpagem", 
            "Componente incorreto", 
            "Emenda aberta", 
            "Falha no nitrogênio", 
            "Queda de energia", 
            "Problema na máquina"
        ]
        self.defect_inputs = []
        for name in defect_names:
            defect_input = QLineEdit(self)
            defect_input.setPlaceholderText(name)
            layout.addWidget(defect_input)
            self.defect_inputs.append(defect_input)

        self.btnAdd = QPushButton("Exportar", self)
        self.btnAdd.clicked.connect(self.export_data)
        layout.addWidget(self.btnAdd)

        self.btnAdd = QPushButton("Adicionar", self)
        self.btnAdd.clicked.connect(self.add_data)
        layout.addWidget(self.btnAdd)

        self.btnClear = QPushButton("Limpar", self)
        self.btnClear.clicked.connect(self.clear_form)
        layout.addWidget(self.btnClear)

        self.btnViewRegistrations = QPushButton("Ver Últimos Registros", self)
        self.btnViewRegistrations.clicked.connect(self.open_registration_window)
        layout.addWidget(self.btnViewRegistrations)

        self.setLayout(layout)

    def add_data(self):
        data = self.date_input_widget.txtData.text()
        if not data:
            QMessageBox.information(self, "Data em branco", "Indique a data referente ao apontamento.")
            return

        try:
            data = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            QMessageBox.information(self, "Data inválida", "Indique a data no seguinte formato: 01/01/2000")
            return

        selected_option = None
        if self.optionTurnoA.isChecked():
            selected_option = "A"
        elif self.optionTurnoB.isChecked():
            selected_option = "B"
        elif self.optionTurnoC.isChecked():
            selected_option = "C"
        else:
            QMessageBox.critical(self, "Turno em branco", "Indique o turno referente ao apontamento.")
            return

        processo = self.listaProcesso.currentText()
        maquina = self.listaMaquina.currentText()
        referencia = self.listaReferencia.currentText()
        producao = self.txtProducao.text()
        refugos = self.txtRefugos.text()

        if not processo or not maquina or not referencia or not producao:
            QMessageBox.critical(self, "Campo em branco", "Preencha todos os campos obrigatórios.")
            return

        try:
            producao = int(producao)
            if producao >= 500:
                QMessageBox.critical(self, "Capacidade excedida", "Valor inserido é maior que a capacidade da máquina.")
                return
        except ValueError:
            QMessageBox.critical(self, "Quantidade inválida", "Indique a quantidade produzida.")
            return

        defects = [defect_input.text() or "0" for defect_input in self.defect_inputs]
        total_defects = sum(int(defect) for defect in defects)

        if total_defects > 0.09 * producao:
            confirm = QMessageBox.question(self, "Confirmação", "Refugo acima de 10%. Confirma este valor?", QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.No:
                return

        for i, defect in enumerate(defects):
            defect_value = int(defect)
            if defect_value > 0:
                defect_type = self.defect_inputs[i].placeholderText()
                self.database.insert_data(data, selected_option, processo, maquina, referencia, refugos, producao, defect_value, defect_type)

        self.clear_form()

    def export_data(self):
        db = Database()
        timestamp = datetime.today().strftime('%Y%m%d_%H%M')
        data = db.read_data()
        df = pd.DataFrame(data, columns=['id', 'data', 'turno', 'processo', 'maquina', 'referencia', 'refugo', 'producao', 'defeitos', 'scrap_type', 'timestamp'])
        df.to_excel(f'{timestamp}_apontado.xlsx')

    def clear_form(self):
        self.date_input_widget.txtData.clear()
        self.optionTurnoA.setChecked(False)
        self.optionTurnoB.setChecked(False)
        self.optionTurnoC.setChecked(False)
        self.listaProcesso.setCurrentIndex(0)
        self.listaMaquina.setCurrentIndex(0)
        self.listaReferencia.setCurrentIndex(0)
        self.txtProducao.clear()
        self.txtRefugos.clear()
        for defect_input in self.defect_inputs:
            defect_input.clear()

    def open_registration_window(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

    def closeEvent(self, event):
        self.database.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ApontamentoApp()
    window.show()
    sys.exit(app.exec_())