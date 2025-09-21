from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

# GestionPersonal.py
# Aplicación PyQt5 para gestionar gastos mensuales.
# Permite al usuario ingresar su ingreso mensual y diferentes tipos de gastos,
# calcula el balance y muestra un mensaje según el resultado.

class GestorGastos(QWidget):
    """
    Ventana principal para la gestión de gastos mensuales.
    Permite ingresar ingresos y gastos, calcula el balance y muestra el estado financiero.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Gastos Mensuales")
        self.setGeometry(100, 100, 300, 250)

        # Etiqueta y campo para el ingreso mensual
        self.ingreso_label = QLabel("Ingreso mensual:")
        self.ingreso_input = QLineEdit()

        # Etiqueta y campo para el gasto en alimentación
        self.gasto1_label = QLabel("Gasto en alimentación:")
        self.gasto1_input = QLineEdit()

        # Etiqueta y campo para el gasto en transporte
        self.gasto2_label = QLabel("Gasto en transporte:")
        self.gasto2_input = QLineEdit()

        # Etiqueta y campo para otros gastos
        self.gasto3_label = QLabel("Otros gastos:")
        self.gasto3_input = QLineEdit()

        # Botón para calcular el balance
        self.calcular_btn = QPushButton("Calcular balance")
        # Etiqueta para mostrar el resultado del balance
        self.resultado_label = QLabel("Balance: ")
        # Etiqueta para mostrar el estado financiero
        self.estado_label = QLabel("")

        # Layout vertical para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.ingreso_label)
        layout.addWidget(self.ingreso_input)
        layout.addWidget(self.gasto1_label)
        layout.addWidget(self.gasto1_input)
        layout.addWidget(self.gasto2_label)
        layout.addWidget(self.gasto2_input)
        layout.addWidget(self.gasto3_label)
        layout.addWidget(self.gasto3_input)
        layout.addWidget(self.calcular_btn)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.estado_label)

        self.setLayout(layout)

        # Conexión del botón de cálculo al método correspondiente
        self.calcular_btn.clicked.connect(self.calcular_balance)

    def calcular_balance(self):
        """
        Calcula el balance mensual restando los gastos al ingreso.
        Actualiza las etiquetas con el resultado y el estado financiero.
        Si hay un error en la entrada, muestra un mensaje de advertencia.
        """
        try:
            # Obtener los valores ingresados y convertirlos a float
            ingreso = float(self.ingreso_input.text())
            gasto1 = float(self.gasto1_input.text())
            gasto2 = float(self.gasto2_input.text())
            gasto3 = float(self.gasto3_input.text())

            # Calcular el total de gastos y el balance
            total_gastos = gasto1 + gasto2 + gasto3
            balance = ingreso - total_gastos

            # Mostrar el balance en la etiqueta
            self.resultado_label.setText(f"Balance: ${balance:.2f}")

            # Mostrar el estado financiero según el balance
            if balance > 0:
                self.estado_label.setText("¡Buen trabajo! Tienes saldo positivo.")
            elif balance == 0:
                self.estado_label.setText("Has gastado todo tu ingreso.")
            else:
                self.estado_label.setText("Cuidado: estás en déficit.")
        except ValueError:
            # Si la entrada no es válida, mostrar mensaje de error
            self.estado_label.setText("Por favor, ingresa solo números válidos.")

# Ejecutar la aplicación principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    # Crear la aplicación Qt
    app = QApplication(sys.argv)
    # Instanciar la ventana principal
    ventana = GestorGastos()
    ventana.show()
    # Iniciar el bucle de eventos de la aplicación
    sys.exit(app.exec_())