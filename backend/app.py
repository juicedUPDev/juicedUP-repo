from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Backend!"}

# Include routes
from routes.prompts import router as prompts_router
from routes.consulting import router as consulting_router
from routes.analytics import router as analytics_router

app.include_router(prompts_router)
app.include_router(consulting_router)
app.include_router(analytics_router)