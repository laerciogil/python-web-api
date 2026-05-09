import time
import asyncio


async def consulta_dados():
    print("Consultando dados...")
    await asyncio.sleep(2)
    return "dados"

async def processa_dados(dados):
    print("Processando dados...")
    await asyncio.sleep(2)

async def grava_log():
    print("Gravando log...")
    await asyncio.sleep(2)


async def main():
    # dados = await consulta_dados()  # Furure/Promise
    # await processa_dados(dados)
    # await grava_log()

    # Executar tasks em paralelo
    dados = await asyncio.create_task(consulta_dados())
    asyncio.create_task(processa_dados(dados))
    asyncio.create_task(grava_log())
    asyncio.create_task(grava_log())
    asyncio.create_task(grava_log())
    asyncio.create_task(grava_log())
    asyncio.create_task(grava_log())
    
    

if __name__ == "__main__":
    start = time.perf_counter()
    print("Início")
    
    asyncio.run(main()) # eventloop

    print("Fim")
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")