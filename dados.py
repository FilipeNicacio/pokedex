import os
import sys


def get_resource_path(relative_path):
    try:
        # Para executáveis criados com PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


pokemon = {
    'PIKACHU': {
        'status': ['HP: 300', 'Ataque: 600', 'Defesa: 500', 'Velocidade: 300', 'Total: 1.700'],
        'habilidades': ['Choque do Trovão', 'Cabeçada'],
        'categoria': ['#025', 'elétrico', get_resource_path('images/pikachu.png'), '#FCC719'],
    },

    'BULBASAUR': {
        'status': ['HP: 320', 'Ataque: 510', 'Defesa: 400', 'Velocidade: 200', 'Total: 1.430'],
        'habilidades': ['Folhas Navalha', 'Raio Solar'],
        'categoria': ['#001', 'grama', get_resource_path('images/bulbasaur.png'), '#49D0B0'],
    },

    'CHARMANDER': {
        'status': ['HP: 200', 'Ataque: 300', 'Defesa: 400', 'Velocidade: 320', 'Total: 1.220'],
        'habilidades': ['Lança-Chamas', 'Ataque Rápido'],
        'categoria': ['#004', 'fogo', get_resource_path('images/charmander.png'), '#ED8A8B'],
    },

    'GYARADOS': {
        'status': ['HP: 300', 'Ataque: 600', 'Defesa: 500', 'Velocidade: 300', 'Total: 1.700'],
        'habilidades': ['Jato dÁgua', 'Hidro Bomba'],
        'categoria': ['#130', 'água', get_resource_path('images/gyarados.png'), '#76BEFE'],
    },

    'GENGAR': {
        'status': ['HP: 100', 'Ataque: 200', 'Defesa: 300', 'Velocidade: 400', 'Total: 1.000'],
        'habilidades': ['Bola Sombria', 'Lambida'],
        'categoria': ['#094', 'trevas', get_resource_path('images/gengar.png'), '#BA68C8'],
    },

    'DRAGONITE': {
        'status': ['HP: 500', 'Ataque: 600', 'Defesa: 400', 'Velocidade: 400', 'Total: 1.900'],
        'habilidades': ['Dança do Dragão', 'Velocidade Extrema'],
        'categoria': ['#149', 'dragão', get_resource_path('images/dragonite.png'), '#C29791'],
    },
}
