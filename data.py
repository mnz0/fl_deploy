import os

project_dir = ''

file_types = {
	'media_formats': ['dpx', 'exr', 'png', 'tiff', 'jpeg', 'hdr', 'rat'], # Media formats collection
	'arhives': ['zip', 'rar', '7zip', 'tar'] }

folders_pattern = {
	'project_pattern': ['source', 'result', 'comp', 'render', 'track'],
	'result_pattern': ['exr', 'png', 'tiff', 'dpx']}




def get_folders_and_files(path):
	





def project_folders_deploy():

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


project_folders_deploy()
