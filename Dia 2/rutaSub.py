import csv
from tqdm import tqdm



Valores = list()
x=0
y=0

def sumaY(y2):
    global y
    y+=int(y2)
def sumaX(x2):
    global x
    x+=int(x2)
def restaX(x2):
    global x
    x=x-int(x2)
def load_csv_file(csv_file):
    with open(csv_file['file'], newline='', encoding='iso-8859-1') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)
        for row in tqdm(rows, desc='Updating'):
            valor = dict()
            valor['Comando'] = row['Comando']
            valor['Cant'] = row['Cant']
            Valores.append(valor)
    for v in Valores:
        if v['Comando']=="forward":
            sumaY(v['Cant'])
        if v['Comando']=="down":
            sumaX(v['Cant'])
        if v['Comando']=="up":
            restaX(v['Cant'])
    print(x)
    print(y)
    print(x*y)


if __name__ == "__main__":
    load_csv_file({'id': 'ruta.csv',
                   'file': './ruta.csv'})
            