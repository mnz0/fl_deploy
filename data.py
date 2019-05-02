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
	'arhives': ['zip', 'rar', '7zip', 'tar', 'tar']}
	

def get_content(folder):

	folder_list = []
	file_list = []

	for f_check in os.listdir(folder):

		to_check = os.path.join(project_dir, f_check)  # File section 
		
		if os.path.isfile(to_check):
			 file_list.append(to_check)

		if os.path.isdir(to_check): # Folder section 
			folder_list.append(to_check)
			
	return file_list, folder_list

	



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

	files = get_content(folder)[0]
	folders = get_content(folder)[1]

	if len(files) > 0:
		print(files)
		
	if len(folders) > 0:
		print(folders)

	if len(folders) > 0 and len(files) > 0:
		print('Foldrer contain files and folder "tmp line"')

	else:
		print("Folder is empty")
		sys.exit()

	


main_deploy(project_dir)