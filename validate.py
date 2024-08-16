def validate(n, naloga):
    out = open(f"naloge/{naloga}/res/{n}.res", "r")
    cmp = open(f"naloge/{naloga}/out/{n}.out", "r")
    stat =  1 if out.read()== cmp.read() else 0
    out.close()
    cmp.close()
    return stat