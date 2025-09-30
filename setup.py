from setuptools import setup, find_packages

setup(
    name='watson-emotion-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ibm-watson-nlp',
    ],
    entry_points={
        'console_scripts': [
            'watson-emotion=app.main:detectar_emociones',
        ],
    },
    author='Tu Nombre',
    description='Aplicación para detectar emociones usando Watson NLP',
)
