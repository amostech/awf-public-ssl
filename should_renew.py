#!/usr/bin/python3
import OpenSSL
import ssl, socket
import sys
from datetime import datetime

cert=ssl.get_server_certificate(( sys.argv[1], sys.argv[2]))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

expiry_date = datetime.strptime( x509.get_notAfter() , '%Y%m%d%H%M%SZ')
now = datetime.now()

delta = expiry_date - now
print(">> Delta Days: " + str(delta.days) )
print(">> Certificate expires:" + str( x509.get_notAfter()) )
if delta.days <= 7:
        print(">> Certificate expires in less than 7 days. Exit 1 => Should Renew!")
        exit(1)
else:
        print("Certificate not due for renewal... Exit 0 => All good")
