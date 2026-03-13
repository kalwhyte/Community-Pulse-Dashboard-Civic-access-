import logging
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .routers import ingest, dashboard, analysis

# ------------------------------------------------
# LOGGING SETUP (Mechanical / Hacker Style)
# ------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("community-pulse")

# ------------------------------------------------
# APP INIT
# ------------------------------------------------
app = FastAPI(
    title="Community Pulse API",
    version="1.0.0",
    description="Signal ingestion and community analytics engine"
)

# ------------------------------------------------
# CORS
# ------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------
# REQUEST LOGGER MIDDLEWARE
# ------------------------------------------------
@app.middleware("http")
async def request_logger(request: Request, call_next):

    start = time.time()

    logger.info(
        f"REQ  -> {request.method} {request.url.path} | IP:{request.client.host}"
    )

    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(f"ERROR -> {str(e)}")
        raise e

    process_time = round((time.time() - start) * 1000, 2)

    logger.info(
        f"RES  <- {request.method} {request.url.path} | "
        f"STATUS:{response.status_code} | {process_time}ms"
    )

    return response


# ------------------------------------------------
# ROUTERS
# ------------------------------------------------
app.include_router(ingest.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")
app.include_router(analysis.router, prefix="/api/v1")


# ------------------------------------------------
# ROOT ENDPOINT
# ------------------------------------------------
@app.get("/")
def root():
    logger.info("SYSTEM STATUS CHECK")
    return {
        "system": "community-pulse",
        "status": "online",
        "mode": "analysis-engine"
    }


# ------------------------------------------------
# STARTUP LOG
# ------------------------------------------------
@app.on_event("startup")
def startup_event():
    logger.info("===================================")
    logger.info("COMMUNITY PULSE BACKEND INITIALIZED")
    logger.info("Signal ingestion module loaded")
    logger.info("Dashboard analytics module loaded")
    logger.info("Analysis engine ready")
    logger.info("Listening for requests...")
    logger.info("===================================")