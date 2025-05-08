#!/usr/bin/env sh
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
