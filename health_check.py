#!/usr/bin/env python3

# import required libraries
import shutil
import psutil
import sys
import socket
import emails

# instantiate variables
gb = 10 ** 9  # GB == gigabyte
THRESHOLD = 500 * 1024 * 1024  # 500MB

def main(argv):

    # monitor cpu usage, alert if > 80%
    cpu_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    c_metric = cpu_load[1] > 80
    print(cpu_load)
    print(c_metric)
    
    # monitor available disk space, alert if < 20%
    total_b, used_b, free_b = shutil.disk_usage(".")
    pct_available = ((free_b / gb) / (total_b / gb)) * 100
    d_metric = pct_available < 20
    print(pct_available)
    print(d_metric)

    # monitor available memory, alert if < 500MB
    mem = psutil.virtual_memory()
    m_metric = mem.available <= THRESHOLD
    print(mem)
    print(m_metric)

    # monitor local host, alert if can't resolve to 127.0.0.1
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    r_metric = host_ip == "127.0.0.1"
    print(hostname)
    print(r_metric)

    # generate email if any of the monitors fail
    if c_metric == True:
        c_subject = "Error - CPU usage is over 80%"
        message = emails.generate_status(c_subject)
        emails.send(message)

   if d_metric == True:
        d_subject = "Error - Available disk space is less than 20%"
        message = emails.generate_status(d_subject)
        emails.send(message)

    if m_metric == True:
        m_subject = "Error - Available memory is less than 500MB"
        message = emails.generate_status(m_subject)
        emails.send(message)

   if r_metric == True:
        r_subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate_status(r_subject)
        emails.send(message) 

    
if __name__ == "__main__":
  main(sys.argv)
