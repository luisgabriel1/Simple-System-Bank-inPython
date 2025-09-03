import time
import tqdm

def loadingTime():
    for _ in tqdm(range(100), desc="Processando"):
        time.sleep(0.05)
        

def loadingconferindoDados():
    for _ in tqdm(range(100), desc="Conferindo Dados"):
        time.sleep(0.05)
        print('Dados conferidos com sucesso !')
        

def loadingTransferencia():
    for _ in tqdm(range(100), desc="Processando Transferencia"):
        time.sleep(0.05)
        print('Transferencia feita com Sucesso !')
        
        
def loadingPagar():
    for _ in tqdm(range(100), desc="Processando Pagamento"):
        time.sleep(0.05)
        print('Pagamento feito com Sucesso !')
        
        
def loadingDeposito():
    for _ in tqdm(range(100), desc="Processando Deposito"):
        time.sleep(0.05)
        print('Deposito feito com Sucesso !')


def loadingPix():
    for _ in tqdm(range(100), desc="Processando Pix"):
        time.sleep(0.05)
        print('Pix feito com Sucesso !')
        