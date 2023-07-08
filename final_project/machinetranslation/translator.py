"""Module providingFunction translating text"""
from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    """Translating English to French"""
    frenchText = MyMemoryTranslator(source='en-US', target='fr-FR').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    """Translating French to English"""
    englishText = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchText)
    return englishText
