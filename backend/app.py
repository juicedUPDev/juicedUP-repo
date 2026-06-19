from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(
    title="Maypo AI Consulting Platform",
    description="Enterprise-grade AI consulting powered by advanced prompt engineering",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Setup static files and templates
static_path = Path(__file__).parent / "static"
templates_path = Path(__file__).parent / "templates"

# Create directories if they don't exist
static_path.mkdir(exist_ok=True)
templates_path.mkdir(exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

# Setup templates
templates = Jinja2Templates(directory=str(templates_path))


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Serve the main dashboard with Vercel Web Analytics"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Maypo AI Consulting Platform is running",
        "version": "1.0.0",
        "analytics": "Vercel Web Analytics enabled"
    }

# Include routes (wrapped in try-except to handle missing route files gracefully)
try:
    from routes.prompts import router as prompts_router
    app.include_router(prompts_router)
except ImportError:
    pass

try:
    from routes.consulting import router as consulting_router
    app.include_router(consulting_router)
except ImportError:
    pass

try:
    from routes.analytics import router as analytics_router
    app.include_router(analytics_router)
except ImportError:
    pass
