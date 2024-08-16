import os
def naredimape(ime):
    os.makedirs(f"naloge/{ime}")
    for subdir in ["code", "err", "in", "out", "res"]:
        os.makedirs(f"naloge/{ime}/{subdir}")

async def shranitestcase(inp, out, ime):
    for (x, file) in enumerate(inp):
        program = open(f"naloge/{ime}/in/{x}.in", "w")
        program.write((await file.read()).decode("utf-8"))
    for (x, file) in enumerate(out):
        program = open(f"naloge/{ime}/out/{x}.out", "w")
        program.write((await file.read()).decode("utf-8"))
    return len(inp)
