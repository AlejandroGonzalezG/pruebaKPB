import requests
import csv
import json
import os

def call_api_gutendex(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            count_page_one = count_data(data['results'])
            save_results_to_csv(data['results'])
            page_two = data['next']
            response_page_two = requests.get(page_two)
            data_page_two = response_page_two.json()
            count_page_two = count_data(data_page_two['results'])
            save_results_to_csv(data_page_two['results'])
            total_count = count_page_one + count_page_two
            print(f'El total de libros en las primeras 2 páginas es de:{total_count}')
        else:
            print(f"Ha fallado la respuesta con el siguiente código: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ha ocurrido un error: {e}")

def count_data(books):
    count = 0
    for data in books:
        count += 1
    return count

def save_results_to_csv(data):
    try:
        existing_fieldnames = set()
        if os.path.exists('books.csv'):
            with open('books.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                existing_fieldnames = set(reader.fieldnames)

        new_fieldnames = set()
        for result in data:
            new_fieldnames.update(result.keys())
        
        fieldnames = sorted(existing_fieldnames.union(new_fieldnames))

        with open('books.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            for result in data:
                row = {}
                for key in fieldnames:
                    value = result.get(key, '')
                    if isinstance(value, list):
                        value = json.dumps(value)
                    row[key] = value
                writer.writerow(row)
        print('Se ha creado o actualizado correctamente el archivo books.csv')
    
    except Exception as e:
        print(f'Ocurrió el siguiente error: {e}')


url = 'https://gutendex.com/books/'
call_api_gutendex(url)
