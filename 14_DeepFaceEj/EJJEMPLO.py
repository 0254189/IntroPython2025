from deepface import DeepFace

# Rutas de las imágenes a comparar
img1_path = "C:\0_IVÁN UNI\UP\8°SEM\ROBOTICA\IntroPython2025\14_DeepFaceEj\Piratita\FREDDY_FAKE.png"
img2_path = "C:\0_IVÁN UNI\UP\8°SEM\ROBOTICA\IntroPython2025\14_DeepFaceEj\Piratita\FREDDY.png"

# Verificar si son la misma persona
result = DeepFace.verify(img1_path, img2_path)

if result["verified"]:
    print("Las imágenes son de la misma persona.")
else:
    print("Las imágenes NO son de la misma persona.")