from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Lab7 – Open Attestation Authority (OAA)", version="1.0.1")

# Health check aliases
@app.get("/health")
@app.get("/healthz")
def health_root():
    return JSONResponse({"status": "ok", "service": "oaa", "version": app.version})

# Keep existing health endpoint for Redis
@app.get("/oaa/health/redis")
def health_redis():
    # TODO: Add actual Redis health check logic here
    return JSONResponse({"status": "ok", "redis": "connected", "service": "oaa"})

# Echo ingest helper
class EchoPulse(BaseModel):
    source: str
    fingerprint: str
    payload: dict

@app.post("/oaa/echo/ingest")
def oaa_echo_ingest(pulse: EchoPulse):
    # TODO: validate + persist + maybe anchor depending on policy
    return {"status": "accepted", "key": pulse.fingerprint}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)