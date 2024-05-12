from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router # event 라우트

import uvicorn

# FastAPI() 인스턴스를 만들고 앞서 정의한 라우트 등록
app = FastAPI()

# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event") # event 라우트 등록

if __name__=="__main__":
    # uvicorn.run() 메서드를 사용해 8000번 포트에서 애플리케이션을 실행하도록 설정
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)