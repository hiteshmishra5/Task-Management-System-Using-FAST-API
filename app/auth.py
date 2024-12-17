from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

TOKENS = {"mynewtoken": "user1"}

auth_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    if token not in TOKENS:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return TOKENS[token]
