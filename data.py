import os
import sys
import subprocess #for copy files 

project_name = r' '

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
	folder_name = []

	for element in os.listdir(path):

		# if element in os.path.isdir(path):

		# if element in os.path.isfile(path):
		

	# return files_list, folder_name


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
		subprocess.run(['cp', str(src_path), str(dst_path)])
	if sys.platform.startswith('win32'):
		subprocess.run(['xcopy.exe', str(src_path), str(dst_path)])


def main_deploy(folder):

	if check_source(folder) == True:

		files = get_files(folder)
		# archives = sort_files(files)[0]
		# media = sort_files(files)[1]
		# other = sort_files(files)[2]

		print(media)
		print(archives)
		print(other)


# main_deploy(project_dir)
get_files(project_dir)