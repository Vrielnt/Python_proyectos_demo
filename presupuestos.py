# Importamos la clase FPDF del módulo fpdf, que permite crear archivos PDF
from fpdf import FPDF

# Solicitamos al usuario los datos necesarios para el presupuesto
proyecto = input("Ingrese la descripción del proyecto: ")
horas_estimadas = input("Ingrese el total de horas estimadas: ")
valor_hora = input("Introduzca el valor de la hora trabajada: ")
termino = input("Introduzca el tiempo estimado de finalización: ")

# Calculamos el valor total multiplicando las horas por el valor por hora
valor_total = int(horas_estimadas) * int(valor_hora)

# Creamos un nuevo objeto PDF
pdf = FPDF()
pdf.add_page()  # Añadimos una página al documento
pdf.set_font("Arial")  # Definimos la fuente del texto

# Insertamos una imagen de fondo (plantilla del presupuesto)
pdf.image("template.png", x=0, y=0)

# Escribimos los datos ingresados por el usuario en posiciones específicas del PDF
pdf.text(115, 145, proyecto)          # Descripción del proyecto
pdf.text(115, 160, horas_estimadas)   # Horas estimadas
pdf.text(115, 175, valor_hora)        # Valor por hora
pdf.text(115, 190, termino)           # Tiempo estimado de entrega
pdf.text(115, 205, str(valor_total))  # Total calculado

# Guardamos el archivo PDF con el nombre "Presupuesto.pdf"
pdf.output("Presupuesto.pdf")

# Mensaje final para confirmar que el PDF se generó correctamente
print("¡Presupuesto generado exitosamente!")
