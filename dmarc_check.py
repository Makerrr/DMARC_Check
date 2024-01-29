#!/usr/bin/python3
import csv
import dns.resolver
import os
print ("______ ___  ___  ___  ______  _____   ")
print ("|  _  \|  \/  | / _ \ | ___ \/  __ \  ")
print ("| | | || .  . |/ /_\ \| |_/ /| /  \/  ")
print ("| | | || |\/| ||  _  ||    / | |      ")
print ("| |/ / | |  | || | | || |\ \ | \__/\  ")
print ("|___/  \_|  |_/\_| |_/\_| \_| \____/  ")
print ("                                        ")
print ("    James Korexenos @ Security in Depth")
print("\n")

def main():
    print("Welcome to the bootleg DMARC checker!")

    
    print("Note: For Windows File Paths - Please exclude quotes")
    input_path = input("Please enter the path to the document that contains the list of domains: ")

    if not os.path.exists(input_path):
        print("Error: File not found.")
        print("Please relaunch and specify the correct path!")
        return

    # Get the path to the output file
    output_path = input("Please enter the path for the output CSV file: ")

    with open(input_path, 'r') as input_file, open(output_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(['Domain', 'DMARC Record'])

        for line in input_file:
            domain = line.strip()
            dmarc_record = query_dmarc_records(domain)
            if dmarc_record:
                csv_writer.writerow([domain, dmarc_record])
            else:
                csv_writer.writerow([domain, 'No DMARC record found'])

    print(f"DMARC check completed. Results saved to {output_path}")

def query_dmarc_records(domain):
    dmarc_records = []
    try:
        # Perform a DNS TXT record query to get DMARC record
        answers = dns.resolver.query(f'_dmarc.{domain}', 'TXT')

        for rdata in answers:
            txt_record = rdata.strings[0].decode('utf-8')  # Decode bytes to string
            if 'v=DMARC1' in txt_record:
                dmarc_records.append(txt_record)

    except dns.resolver.NXDOMAIN:
        pass  

    return '\n'.join(dmarc_records) if dmarc_records else 'No DMARC record found'

if __name__ == "__main__":
    main()
