import csv

def read_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def compare_and_remove_duplicates(file1, file2, target_file):
    data1 = read_csv(file1)
    data2 = read_csv(file2)

    # Menghapus baris yang memiliki nilai kolom "review" yang sama dengan file kedua
    reviews1 = set(row['Review'] for row in data1)
    reviews2 = set(row['Review'] for row in data2)
    
    if target_file == file1:
        data1_filtered = [row for row in data1 if row['Review'] not in reviews2]
        write_csv(file1, data1_filtered)
    elif target_file == file2:
        data2_filtered = [row for row in data2 if row['Review'] not in reviews1]
        write_csv(file2, data2_filtered)
    else:
        print("Nama file target tidak sesuai.")

# Mengganti 'file1.csv' dan 'file2.csv' dengan nama file yang sesuai
# Mengganti 'target_file' dengan nama file yang ingin dihapus barisnya yang sama dengan file kedua
compare_and_remove_duplicates('scraping_avoskin.csv', 'dataset-150 - sebelum preprocess.csv', 'dataset-150 - sebelum preprocess.csv')
