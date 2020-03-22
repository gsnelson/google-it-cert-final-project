#!/usr/bin/env python3

# import required libraries
import os
import datetime
import sys
import reports
import emails

# instantiate variables

root = os.getcwd()
# desc_path = root + "/supplier-data/descriptions"
desc_path = "C:/Users/gscot/Documents/python/google-it-cert-final-project/supplier-data/descriptions"
# pdf_save_path = "/tmp/processed.pdf"
pdf_save_path = "C:/Users/gscot/Documents/python/google-it-cert-final-project/tmp/processed.pdf"

def main(argv):
    rpt_contents = ""
    os.chdir(desc_path)
    file_list = os.listdir()
    for file in file_list:
        with open(file, "r") as f:
            fname = f.readline()
            fweight = f.readline()
            rpt_contents += ("<br/>" + "name: " + fname + "<br/>" + fweight + "<br/>")
            f.close
    print(rpt_contents)
        
    # create fruit processed PDF report
    # calls the reports.generate function from reports.py
    
    todays_date = datetime.datetime.today()
    rpt_title = "Processed Update on " + todays_date.strftime("%B %d, %Y")
    reports.generate_report(pdf_save_path, rpt_title, rpt_contents)  
    print(rpt_title)
    # send the PDF report as an email attachment
    # call emails.generate & emails.send functions from emails.py
  
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is \nattached to this email."

    message = emails.generate(sender, receiver, subject, body, pdf_save_path)
    emails.send(message)



if __name__ == "__main__":
  main(sys.argv)
