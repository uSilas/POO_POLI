from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida

def teste_drive(carro):
    carro_corrida.acelera()
    carro_corrida.exibe_velocidade()
    carro_corrida.freia
    
if __name__ == "__main__":
    carro_inteligente = CarroInteligente(30)
    print("Carro Inteligente:")
    carro_inteligente.acelera()
    carro_inteligente.exibe_velocidade()

    carro_inteligente.estaciona()
    print()
    
    carro_esportivo = CarroEsportivo(50)
    print("Carro Esportivo: ")
    carro_esportivo.exibe_velocidade()
    carro_esportivo.turbo()
    carro_esportivo.exibe_velocidade()
    carro_esportivo.freia()

    carro_esportivo.exibe_velocidade()
    
    carro_corrida = CarroCorrida(100)