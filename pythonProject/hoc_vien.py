# {'ten': 'rose chen', 'tuoi': '18', 'lop': 'mat dai'}
from hocVienManager import index

def go():
    hoc = index()
    for idx, m in enumerate(hoc):
        print(idx+1, m)

go()
