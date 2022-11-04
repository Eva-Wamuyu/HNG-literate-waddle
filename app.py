import csv
import hashlib
import json

csv_file = './assets/naming-all.csv'
json_file = './assets/naming-all-teams.json'
json_array = []

def create_json():
    json_array = []
    with open(csv_file,encoding='utf-8') as f:
        f_reader = csv.DictReader(f)
        for line in f_reader:
            json_array.append(line)
        
    return json_array


def create_json_file():
    data = create_json()
    with open(json_file,'w', encoding='utf-8') as f:
        json_ = json.dumps(data,indent=10)
        f.write(json_)
    




def get_sha_256():
    with open(json_file,'rb') as f:
        bytes = f.read()
        sha_256 = hashlib.sha256(bytes).hexdigest()
    return sha_256


def append():
    sha_256 = get_sha_256()
    new_csv = []
    csv_data = open(csv_file, 'r')
    for line in csv.reader(csv_data,delimiter=','):
        line.append(sha_256)
        new_csv.append(line)
    return new_csv




def add_to_output_file():
    updated_csv_content = append()
    csv_file = open('./assets/naming-all-output.csv','w')
    writer = csv.writer(csv_file)
    for line in updated_csv_content:
        writer.writerow(line)
       
    
def handler():
    create_json_file()
    add_to_output_file()
    


if __name__ == '__main__':
    
    handler()
    














