import hashlib
import os
import sys

def openfile():
	try:
		hFile = open(sys.argv[1],'rb')
		contents = hFile.read()
		hFile.close()
		return(contents)
	except:
		print('error opening file')
		sys.exit()
		
if len(sys.argv) == 3:
	algo = sys.argv[2]
	contents = openfile()		
	if algo.lower() == 'sha1':
		print hashlib.sha1(contents).hexdigest()
		
		
	else:
		print 'algorithm not recognized'

	if algo.lower() == 'sha224':
		hashlib.sha224(contents).hexdigest
	if algo.lower() == 'sha':
		hashlib.sha(contents).hexdigest
	if algo.lower() == 'sha384':
		hashlib.sha384(contents).hexdigest
	if algo.lower() == 'sha256':
		hashlib.sha256(contents).hexdigest
	if algo.lower() == 'sha512':
		hashlib.sha512(contents).hexdigest
	if algo.lower() == 'md4':
		hashlib.md4(contents).hexdigest
	if algo.lower() == 'md5':
		hashlib.md5(contents).hexdigest
	if algo.lower() == 'sha1':
		hashlib.sha1(contents).hexdigest
	if algo.lower() == 'sha224':
		hashlib.sha224(contents).hexdigest
	if algo.lower() == 'md5':
		hashlib.md5(contents).hexdigest
	if algo.lower() == 'sha384':
		hashlib.sha384(contents).hexdigest
	if algo.lower() == 'sha256':
		hashlib.sha256(contents).hexdigest
	if algo.lower() == 'sha512':
		hashlib.sha512(contents).hexdigest
		
else:
	print 'usage:', sys.argv[0], '<file directory>', hashlib.algorithms_available