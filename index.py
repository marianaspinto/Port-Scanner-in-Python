# The Socket library allows establishing TCP or UDP connections,
# which are essential for scanning ports on a IPadress or dominian.
import socket

# Request the IP address or the domain you wish to scan.
alvo = input("Enter the IP address or domain to scan.")

# Define a range of ports to scan.
inicio_de_porta = int(input("Enter the starting port number"))
fim_de_porta = int(input("Enter the final port number"))