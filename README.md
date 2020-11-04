# Ransomware-Linux
Here is a short directory providing a ramsomware written in Python for Linux. It is created in a pedagogic objective. 
The Ransomware encrypts all the files in the directory /tmp by downloading a key from a local server.
1. 
The server is launched first with 
python3 server.py

2.
Open a second tab and launch 
python3 main.py 
This will encrypt the files.
For decrypting :
python3 main.py --action decrypt --keyfile keyfile.txt
