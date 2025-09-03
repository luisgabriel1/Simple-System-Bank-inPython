from fastapi import FastAPI


router = FastAPI(title='API Transferencia main')

@router.get('/transferencia')
def apiTransferencia():
    return ('API TRANSFERENCIA ')