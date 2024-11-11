
#101 ReadFile_with_csv=============================================================================

import csv

 
file_location = 'C:/Users/ARUNKUMAR/OneDrive/Desktop/Person.csv'

try:
    with open(file_location, 'r') as read_all:
        all_content = csv.reader(read_all)
        print("This is print reference")
        print(all_content)  

        for row in all_content:
            print(row)  
            
except FileNotFoundError:
    print("The file is not there")
except PermissionError:
    print("You don't have access this file")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 



# 101 Readfile_Without_csv=============================================================================

fileLocation = 'C:/Users/ARUNKUMAR/OneDrive/Desktop/Person.csv'

try:
    with open(fileLocation,'r') as file:
        allContend = file.read()
        print(allContend)
    
except FileNotFoundError:
    print("No file")
except PermissionError:
    print("No permission")
finally:
    print("Successfully executed")

#102 Howto_load_database=============================================================================

import psycopg2
import csv
from psycopg2 import OperationalError, DatabaseError, Error

def connect_database():
    try:
        
        connection = psycopg2.connect(
            host="localhost",
            database="PythonCSV",
            user="postgres",
            password=" ",
            port="5432",
        )
        print("Successfully connected to the database.")
        return connection
    except OperationalError as e:
        print(f"Error connecting to the database: {e}")
        

def data_insert():
    
    connectObj = connect_database()
    if connectObj is None:
        print("Database connection failed. Exiting...")
        
    
    try:
       
        with open('C:/Users/ARUNKUMAR/OneDrive/Desktop/Person.csv', 'r') as file:
            dataReadObj = csv.reader(file)
            
            
            next(dataReadObj) 
            
          
          
            with connectObj.cursor() as cur_connect_obj:
               
                for row in dataReadObj:
                    try:
                        cur_connect_obj.execute(
                            "INSERT INTO staff (id, name, age, city) VALUES (%s, %s, %s, %s)",
                            row
                        )
                    except (DatabaseError, Error) as e:
                        print(f"Error inserting row {row}: {e}")
                        
                    else:
                        connectObj.commit()  

    except FileNotFoundError as e:
        print(f"File not found => {e}")
    except IOError as e:
        print(f"Reading file => {e}")
    except Error as e:
        print(f"Database error => {e}")
    finally:
        
        if connectObj:
            connectObj.close()
            print("Database connection closed.")

data_insert()

# 103 Compare_ 2_csvfiles===================================================================================

import csv


def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print("Don't have file ")
    except Exception as e:
        print("Error occur while reading : " +e)   

def compare_file1_file2(file1_data, file2_data):
    mismatches = []
    try:
        for index, (row1, row2) in enumerate(zip(file1_data, file2_data)):
            for key in row1:
            
                if row1[key] != row2[key]: 
                    mismatches.append({
                        'row': index + 1,  
                        'column': key,
                        'file1_value': row1[key],
                        'file2_value': row2[key]
                        })
    except KeyError as e:
        print("Column mismatch :" +e)  
    except Exception as e:
        print(f"Error during comparison: {e}")             
    return mismatches


def generate_mismatch_report(mismatches,Mismatch_report):
    try:
        with open(Mismatch_report, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["row", "column", "file1_value", "file2_value"])
            writer.writeheader()
            writer.writerows(mismatches)
    except Exception as e:
        print(f"Error writing mismatch report: {e}")


file1_path ='C:/Users/ARUNKUMAR/OneDrive/Desktop/TataCars.csv'
file2_path ='C:/Users/ARUNKUMAR/OneDrive/Desktop/AudiCars.csv'


Tatabrand_data = read_csv(file1_path)

Audibrand_data = read_csv(file2_path)
Mismatch_report = 'C:/Users/ARUNKUMAR/OneDrive/Desktop/mismatch_repost.csv'

Mismatches = compare_file1_file2(Tatabrand_data, Audibrand_data)


if Mismatches:
    generate_mismatch_report(Mismatches, Mismatch_report)
    print("Mismatch report generated: 'mismatch_report.csv'")
else:
    print("No mismatches found.")



# 104Deviation_report_sendtomail=============================================================================

import smtplib


def read_csv(filename):
    try:    
        with open(filename, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')
            data = [line.strip().split(',') for line in lines[1:]]
            return headers, data
    except FileNotFoundError:
        print("Don't have file ")
    except Exception as e:
        print("Error occur while reading : " +e)


def write_csv(filename, headers, data):
    try:
        with open(filename, 'w') as file:
            file.write(','.join(headers) + '\n')
            for row in data:
                file.write(','.join(map(str, row)) + '\n')
    except Exception as e:
        print("Error writing to "+filename+" "+e)

yesterday = ('C:/Users/ARUNKUMAR/OneDrive/Desktop/Yesterday.csv')
today = ('C:/Users/ARUNKUMAR/OneDrive/Desktop/Today.csv')
deviation = ('C:/Users/ARUNKUMAR/OneDrive/Desktop/deviation_report.csv')

yesterday_headers, yesterday_data = read_csv(yesterday)
today_headers, today_data = read_csv(today)


deviation_report = []
for y_row in yesterday_data:
    
    for t_row in today_data:
        
        if y_row[0] == t_row[0]:  
            try:
                price_yesterday = float(y_row[2]) #200.75
                price_today = float(t_row[2])  #180.7
            
                deviation_percentage = ((price_today - price_yesterday) / price_yesterday) * 100

                if deviation_percentage > 10:
                    deviation_report.append([y_row[0], y_row[1], price_yesterday, price_today, deviation_percentage])
            except ValueError:
                print("Non Numeric error")
            except IndexError:
                print("Missing data in row")

deviation_headers = ['ProductID', 'ProductName', 'Price_Yesterday', 'Price_Today', 'Deviation_Percentage']
write_csv(deviation, deviation_headers, deviation_report)
print("Deviation report saved as 'deviation_report.csv'")





sender_email = "100arunkumar.p@gmail.com"
receiver_email = "indiraperumal78@gmail.com"
password = " "


subject = "Alert: Price Deviation Report"
body = """\
Hello,

Attached is the report for products with price deviations greater than 10% between yesterday and today.

Best regards,
Arun Kumar P
"""

email_message = f"From: {sender_email}\n"
email_message += f"To: {receiver_email}\n"
email_message += f"Subject: {subject}\n\n"
email_message += body


try:
        with open("deviation_report.csv", "r") as file:
            attachment_content = file.read()

        email_message += "\n-- ATTACHMENT START WITH MORE THAN 10% --\n"
        email_message += attachment_content
        email_message += "\n--ATTACHMENT END--\n"
except FileNotFoundError:
        print("Deviation report file not found. Email will be sent without attachment.")
except Exception as e:
        print(f"Error reading attachment file: {e}")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_message)

    print("Email sent successfully with deviation report.")
except smtplib.SMTPAuthenticationError:
        print("Error: Unable to authenticate with email server. Check credentials.")
except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

# =============================================================================
