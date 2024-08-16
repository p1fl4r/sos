from fastapi import FastAPI, __version__
from fastapi import Request, Form
from fastapi import Cookie
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated

import os
import subprocess
from validate import validate
from compare import compare
from naloga import naredimape, shranitestcase
from run import run

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="strani")

@app.get("/")
async def main():
    content = """<script>window.location.href = '/naloge';</script>"""
    return HTMLResponse(content=content)

@app.get('/admin')
async def admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.post('/dodajnalogo')
async def dodajnalogo(ime:str = Form(), vsebina: str = Form(...), inp: list[UploadFile] = File(...), out: list[UploadFile] = File()):
    if ime in os.listdir("./naloge"):
        return False
    naredimape(ime)
    with open(f"naloge/{ime}/naloga.txt", "w") as nal:
        nal.write(vsebina)
    with open(f"naloge/{ime}/info.py", "w") as info:
        info.write(str(await shranitestcase(inp, out, ime)))
    return "ok, naloga shranjena"

@app.get('/naloge')
async def naloge(request: Request):
    naloge = os.listdir("./naloge")
    return templates.TemplateResponse("naloge.html", {"request": request, "naloge": naloge})

@app.get('/naloge/{naloga}')
async def naloge(request: Request, naloga: str):
    if not naloga in os.listdir("./naloge"):
        return "Naloga ne obstaja."
    with open(f"naloge/{naloga}/naloga.txt") as besedilo:
        bes = besedilo.read()
    return templates.TemplateResponse("naloga.html", {"request": request, "naloga": naloga, "besedilo": bes})

@app.post("/oddaj/{naloga}")
async def oddaja(request: Request, naloga: str,  files: list[UploadFile] = File(...)):
    f = files[0]
    program = open(f"naloge/{naloga}/code/{f.filename}", "w")
    tekst = (await f.read()).decode("utf-8")
    program.write(tekst)
    program.close()
    with open(f"naloge/{naloga}/info.py", "r") as data:
        TESTCASES = int(data.read())
    resp = []
    for i in range(TESTCASES):
        run(i, f, naloga)
        enak = validate(i, naloga)
        resp.append(compare(i, naloga, enak))
    return templates.TemplateResponse("oddaja.html", {"request": request, "naloga": naloga, "files": resp})
