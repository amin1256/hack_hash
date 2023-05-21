import hashlib
import csv

def hash_password_hack(input_file_name , output_file_name ) :
    with open(input_file_name , newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            hash_data = row[1]
            for password in range(1000 , 9999):
                password = str(password)
                h = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if h == hash_data:
                   a = (name , password)
                  
                   with open(output_file_name , 'w' ) as finally_file:
                        writer = csv.writer(finally_file)
                        writer.writerows(a)
                        
hash_password_hack('file_name' , 'outname')






#print(hash_password_hack('data.csv'))