from ibm_watson_nlp import NaturalLanguageUnderstanding
from ibm_watson_nlp.model import Emotion

def detectar_emociones(texto):
    emotion_model = Emotion.load()
    resultado = emotion_model.run(texto)
    emociones = resultado.get_emotion()
    return emociones
