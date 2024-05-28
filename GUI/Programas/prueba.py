import sys
from output import Ui_MainWindow
from coordenads import coordendas
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.abrir.clicked.connect(self.abrir)
        self.ui.guardar.clicked.connect(self.guardar)

    def abrir(self):
        self.archivo_entrada, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo', '.', 'Archivos de texto (*.kml);;Todos los archivos (*.*)')
        self.ui.entrada.setText(self.archivo_entrada)

    def guardar(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Archivos de Texto (*.kml);;Todos los archivos (*)", options=options)
        rotular=coordendas(self.archivo_entrada,0)
        rotular.main(fileName)
        self.ui.salida.setText(fileName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    app.exec()
