import qrcode

enlace_web = "https://github.com/IllyanaX"

# Creamos una instancia QRCode-objeto

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4)

"""En la línea 7 estamos creando un objeto QRCode con los siguientes parámetros: 
version: Este parámetro es un entero que indica el tamaño del código QR. Y va desde el 1 al 40
box_size: Este parámetro es un entero que indica el tamaño de cada cuadro del código QR
border: Este parámetro es un entero que indica el tamaño del borde del código QR
error_correction: Este parámetro es una constante que indica el nivel de corrección de errores que tendrá el código QR."""

# Añadimos la información al objeto QRCode

qr.add_data(enlace_web)
qr.make(fit = True)

# Creamos una imagen del código QR

img = qr.make_image(fill_color = "black", back_color = "white")

# Guardamos la imagen con extensión .png

img.save("github_qr.png")

