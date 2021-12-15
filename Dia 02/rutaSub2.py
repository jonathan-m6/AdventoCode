import csv
from tqdm import tqdm
def load_csv_file(csv_file):
    x,y,punt=0,0,0
    with open(csv_file['file'], newline='', encoding='iso-8859-1') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)
        for row in tqdm(rows, desc='Updating'):
            if row['Comando']=="forward":
                y+=int(row["Cant"])
                punt=punt+int(row["Cant"])*x
            if row['Comando']=="down":
                x+=int(row["Cant"])
            if row['Comando']=="up":
                x=x-int(row["Cant"])
    print(y)
    print(punt)
    print(y*punt)
if __name__ == "__main__":
    load_csv_file({'id': 'ruta.csv','file': './ruta.csv'})