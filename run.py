from app.main import detectar_emociones

if __name__ == "__main__":
    texto = input("Escribe un texto para analizar emociones: ")
    emociones = detectar_emociones(texto)

    print("\n?? Emociones detectadas:")
    for emocion, puntuacion in emociones.items():
        print(f"{emocion.capitalize()}: {puntuacion:.2f}")
