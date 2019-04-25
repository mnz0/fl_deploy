import os
import sys
import subprocess #for copy files 


project_dir = r'F:\_work\test'
	
folders_pattern = {
	'project_pattern': ['source', 'result', 'comp', 'render', 'track'],
	'result_pattern': ['exr', 'png', 'tiff', 'dpx']}

file_types = {
	'media_formats': ['dpx', 'exr', 'png', 'tiff', 'jpeg', 'hdr', 'rat', 'tga'], # Media formats collection
	'arhives': ['zip', 'rar', '7zip', 'tar']}
	

def check_source(dirname):

	if len(os.listdir(dirname)) == 0 and os.path.isfile(dirname):
		print('{} is empty'.format(dirname))
		sys.exit()
	else:
		return True


def get_files(path):

	files_list = []
	os.path.abspath(path)
	for root, dirs, files in os.walk(path):
		for f  in files:
			files_list.append(f)

	return files_list


def sort_files(infiles_list):

	arch_files = []
	media_files = []
	other_formats = []

	for file in infiles_list:

		if os.path.splitext(file)[1][1:] in file_types['media_formats']:  #media content detect! 
			media_files.append(file)

		if os.path.splitext(file)[1][1:] in file_types['arhives']:  #arhive content detect! 
			arch_files.append(file)

		if os.path.splitext(file)[1][1:] in file_types['arhives'] != True and os.path.splitext(file)[0][1:] in file_types['media_formats'] != True: #Check other files
			other_formats.append(file)
			for f in other_formats:
				print('File {} is not support', format(f)) 

	return arch_files, media_files, other_formats
	

def project_folders_create():

	""" This function makes folder structure for source files, ref and result sequences.
		Folders struct get from "folder_patterns" dict.
	"""

	for folders_name in folders_pattern['project_pattern']:

			if 'result' in folders_pattern['project_pattern']:
				os.mkdir(folders_name.upper())
			else:
				print('Pattern "result" in folders pattern is not exist')

	ready_folders = [files for files in os.listdir('.')]
	if 'RESULT' in ready_folders:
		os.chdir('RESULT')
		for folders_name in folders_pattern['result_pattern']:
			os.mkdir(folders_name.upper())
		os.chdir('..')


def copy_files(src_path, dst_path):

	'''
	cross platform copy (I hope that`s work)
	'''
	if sys.platform.startswith('linux'):
		subprocess.run(['cp', str(src_path), str(dst_path) ])
	if sys.platform.startswith('win32'):




def deploy():

	