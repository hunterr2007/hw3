from pathlib import Path
print(f'Количество символов в тексте :' +str(len(set(Path(r'referat.txt').read_text(encoding='utf-8').split()))))
with open("referat.txt", "r", encoding="utf-8") as f:
    a=''
    for line in f:
        line=line.replace(".","!")
        a+=line
    with open("referat2.txt", "w", encoding="utf-8") as g:
        g.write(a)
print(f'Количество символов в тексте : {len(a)}')
