import csv
import hashlib


csv_file = open('./assets/naming-all-teams.csv','r')
json_file = open('./assets/naming-all-teams.json','rb')

def get_sha_256():
    
    bytes = json_file.read()
    sha_256 = hashlib.sha256(bytes).hexdigest()
    
    return sha_256

def create_json_file():
    for line in csv_file:
        print(line)
        try:
            format = line['format']
            name = line['name']
            description = line['description']
            series_number = line['series_number']
            series_total = line['series_total']
            attributes = line['attributes']

            for attribute in attributes:
                trait_type = attribute[0]['trait_type']
                value = attribute[0]['value']
                trait_type= attribute[1]['trait_type']
                value2 = attribute[1]['value']
                trait_type2 = attribute[2]['trait_type']
                value3 = attribute[2]['value']
                min_value = attribute[3]['min_value']
                max_value = attribute[3]['max_value']

        
        except KeyError:

            obj = {}



def append():
    sha_256 = get_sha_256()
    new_csv = []
    csv_file_reader = csv.reader(csv_file,delimiter=',')
    for line in csv_file_reader:
            line.append(sha_256)
            new_csv.append(line)
    
    return new_csv


def add_to_output_file():
    updated_csv_content = append()
    csv_file = open('./assets/naming-all-teams-output.csv','w')
    writer = csv.writer(csv_file)
    for line in updated_csv_content:
        writer.writerow(line)
    csv_file.close()



if __name__ == '__main__':
    
    add_to_output_file()
    json_file.close()
    csv_file.close()














