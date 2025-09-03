# Essa sera a funcao responsavel pelos 'transferencias'.
# Transferencia Padrão (TED, DOC)
# numero de conta e agencia / verificar saldo da conta

from utils.loadingTime import loadingTime, loadingconferindoDados, loadingTransferencia
from functionConta import saldo
from doc_ted import doc, ted
from routes import routesTransferencia, routesErro


def transferenciaDOC():
    
    loadingTime()
    print('::::::::::::::::::::  Transferencia  :::::::::::::::::::: \n\n')
    
    
    
    if saldo() > 0:
        print('Escolha o tipo da transferencia')
        tipo = input('TED (T) / DOC (D) : ' + '\n' ).upper()
        
        print('SALDO: ' + saldo())
        valor = float(input('Inserir o valor: '))
        
        if tipo == 'D':
            if doc() == True and valor <= 4999.99:
                loadingconferindoDados()
                print(f'Informacoes de transferencia: \n')
                print(f'{doc()}\n')
                print('Deseja realizar essa transferencia: ')
                realizarTransferencia = input('Sim (S) \nNão (N)\nInforme: ').upper()
                
                if realizarTransferencia == 'S':
                    loadingTransferencia()
                
                elif realizarTransferencia == 'N':
                    # Mandar o usuario para a tela de transferencia novamente.
                    return routesTransferencia
                

                    
            
            
    else:
        print('Saldo insuficiente para realizar qualquer transferencia !')
        
    
    
    
    
    

    return 


