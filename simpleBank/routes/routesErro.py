from fastapi import FastAPI


router = FastAPI(title='API Error')

@router.get('/')