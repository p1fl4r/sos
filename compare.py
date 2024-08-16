def compare(n, naloga, enaka):
    out = open(f"naloge/{naloga}/res/{n}.res", "r")
    cmp = open(f"naloge/{naloga}/out/{n}.out", "r")
    nn = '\n'
    ret = f"<details>{cmp.read().replace(nn, '<br>')}<summary>{n}.out</summary></details><details>{out.read().replace(nn, '<br>')}<summary class={'zelen' if enaka else 'rdec'}>{'Your output'}</summary></details>"
    out.close()
    cmp.close()
    return ret