# DMARC_Check
Tool used to input wordlist of domains and print out DMARC records into a CSV file.

Script Usage:
- **Create wordlist of domains (can store in .txt):**
  
e.g fakedomain.com
    fakedomain1.com
  
- **Run DMARC_Check:**
- 
python3 DMARC_Check.py

- **Specify absolute path of wordlist:**
- 
Linux Example: /home/user1/Documents/Domain_wordlist.txt
Windows Example: C:\Users\Home\user1\Documents\Domain_wordlist.txt

- **Specify path to output the results:**
- 
Linux Example: /home/user1/Documents/DMARC_Output.csv
Windows Example: C:\Users\Home\user1\Documents\DMARC_Output.csv
