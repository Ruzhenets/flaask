from fastapi import FastAPI
import uvicorn
from routes.event_routes import router as event_routes
from routes.user_routes import router as user_routes
from routes.product_routes import router as product_routes
from routes.order_routes import router as order_routes

app = FastAPI()

app.include_router(event_routes)
app.include_router(user_routes)
app.include_router(product_routes)
app.include_router(order_routes)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )