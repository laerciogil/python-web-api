import time


def consulta_dados():
    print("Consultando dados...")
    time.sleep(2)
    return "dados"

def processa_dados(dados):
    print("Processando dados...")
    time.sleep(2)

def grava_log():
    print("Gravando log...")
    time.sleep(2)


def main():
    start = time.perf_counter()
    print("Início")

    dados = consulta_dados()
    processa_dados(dados)
    grava_log()
    
    print("Fim")
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")

if __name__ == "__main__":
    main()