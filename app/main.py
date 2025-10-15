from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Lab7 – Open Attestation Authority (OAA)", version="1.0.1")

class EchoPulse(BaseModel):
    source: str
    fingerprint: str
    payload: dict

@app.get("/health")
@app.get("/healthz")
def health_root():
    return JSONResponse({"status": "ok", "service": "oaa", "version": app.version})

@app.get("/oaa/health/redis")
def health_redis():
    # TODO: Add actual Redis health check
    return JSONResponse({"status": "ok", "service": "redis", "connected": True})

@app.post("/oaa/echo/ingest")
def oaa_echo_ingest(pulse: EchoPulse):
    # TODO: validate + persist + maybe anchor depending on policy
    return {"status": "accepted", "key": pulse.fingerprint}

@app.get("/")
def root():
    return {"message": "Lab7 – Open Attestation Authority (OAA)", "version": app.version}
