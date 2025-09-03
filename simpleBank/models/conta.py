# Class conta coloquei aqui para que eu possa manipular tudo que uma conta tem e pode fazer 
# NumeroConta
# Titular Conta
# Saldo Conta 

# DEPOSITO
# Valor

# SACAR
# Valor

# TRANSFERIR
# Valor
#



class conta:
    
    def __init__(self, numero, titular, saldo=0):
        self.numeroConta = numero
        self.titularConta = titular
        self.saldoConta = saldo
        
    
    def depositar (self, valor):
        
        if valor > 0:
            self.saldoConta += valor
            return True 
        return False 
            