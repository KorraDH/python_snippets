import sys, traceback, os, ftplib
#import xml.etree.ElementTree as ET
#import os, time, gzip
from os import listdir
from os.path import isfile, join
from ftplib import FTP

def ftpupload(filepath, ftphost, ftpuser, ftppasswd):
	file=None
	filenames = [f for f in listdir(filepath) if isfile(join(filepath, f))]
	for filename in filenames:
		print('Trying to connect...')
		ftp = FTP(ftphost,ftpuser, ftppasswd,50)
		#Setting active mode: only for PetVillage - Magento
		ftp.set_pasv(False)
		local_filename = os.path.join(filepath, filename)
		file = open(local_filename, "rb")
		ftp.cwd("//exchange//import//")
		ftp.storbinary('STOR ' + filename, file)
		ftp.quit()
		file.close()
		print('File transfered')

#MAIN
ftphost='111.111.111.111'
ftpuser='utente'
ftppasswd='password'
filepath="I:\\ITER\\export\\"
filepath="\\\\srv-iter\\Condivisioni\\ITER\\export\\"
ftpupload(filepath, ftphost, ftpuser, ftppasswd)                        
                           