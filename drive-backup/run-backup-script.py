

import argparse
import gzip
import os
import shutil
import sys
import threading
import math


NUMBER_OF_THREADS= 10
worker_threads_status = [0] * NUMBER_OF_THREADS
files_to_delete =[]
folders_to_delete = []
files_to_copy=[]

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-target', nargs=1, required=True,
                        help='Target Backup folder')
    parser.add_argument('-source', nargs='+', required=True,
                        help='Source Files to be added')

    # no input means show me the help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()

# check timestamps
def size_if_newer(source, target):

	src_stat = os.stat(source)

	try:
		target_ts = os.stat(target).st_mtime
	except:
		target_ts = 0

    # The time difference of one second is necessary since subsecond accuracy
    # of os.st_mtime is striped by copy2
	return src_stat.st_size if (src_stat.st_mtime - target_ts > 1) else False

# delete folders and files from the target path
def deleteItems(files, directories):
	for file in files:
		os.remove(file)
	for dir in directories:
		shutil.rmtree(dir)


# copy the files to the location
def copyfunction(source, destination, stat_num):
	shutil.copy2(source, destination)
	worker_threads_status[stat_num] = 0

# 100 - 8100
#  1  - 81
# copy thread controller
def copyfiles2(source, destination):
	nm_of_files = len(files_to_copy)
	factor = 100.0/nm_of_files
	factor2 = 20.0/nm_of_files
	cntr=0
	i=0
	sys.stdout.write("[%-20s] %d%%" % ('=', 0))
	
	for file in files_to_copy:
		try:
			shutil.copy2(file, destination+'/'+file)
			i=i+1
			sys.stdout.write('\r')
			sys.stdout.write("[%-20s] %d%%" % ('='*int(factor2*i), int(i*factor)))
			sys.stdout.flush()
		except:
			print sys.exc_info()[0]
			print file
	
	print
# copy files in a multi-threaded way. Not so good :/
def copyfiles(source, destination):

	for file in files_to_copy:
		cnt = 0
		while True:
			if worker_threads_status[cnt] == 0:
				break
			else:
				cnt = (cnt +1)%NUMBER_OF_THREADS

		thread = threading.Thread(target=copyfunction,  args=(file, destination+'/'+file, cnt))
		thread.start()

# main function
def sync_root(root, arg):
	utargetroot = unicode(arg.target[0],"utf-8")
	usourceroot = unicode(root, "utf-8")

	for path, _ , files in os.walk(usourceroot):
		target=utargetroot+'/'+path+'/'

		if os.path.exists(target):
			target_dir_contents = os.listdir(target)

			#mark elements that don't exist in original
			for element in target_dir_contents:
				if os.path.isfile(target+'/'+element):
					if element not in files:
						files_to_delete.append(target+'/'+element)
				else:
					if element not in _:
						folders_to_delete.append(target+'/'+element)

			#check which files to copy
			for file in files:
				size = size_if_newer(path+'/'+file, target+'/'+file)
				if size:
					files_to_copy.append(path+'/'+file)
		else:
			os.makedirs(target)
			for dir in _:
				os.makedirs(target+'/'+dir)

	print "# Folders to delete: %d"%(len(folders_to_delete))
	print "# Files to delete: %d"%(len(files_to_delete))
	print files_to_delete
	print "# Files to copy: %d"%(len(files_to_copy))


	if (len(folders_to_delete) | len(files_to_delete) |len(files_to_copy)) ==0:
		return

	user_input= raw_input("# Do you want to continue? Y/N ")
	if user_input[0] == "Y" or user_input[0] == "y":
		deleteItems(files_to_delete,folders_to_delete)
		if len(files_to_copy):
			copyfiles2(usourceroot, utargetroot)
	else:
		print "# Exiting"
	# for path, _, files in os.walk(uniroot):
		# #print path
		# number_of_folders = number_of_folders+1
		# number_of_files = number_of_files+len(files)
		# print files
		# #for path2, _2, files2 in os.walk(path[0]):
		# for source in files:

			# source = path + '/' + source

			# sync_file(source, target+source)
			# #threaded_sync_file(source, target + source)
# #            sync_file(source, target + source, compress)




	#for thread in worker_threads:
	#	thread.join()


if __name__ == '__main__':
	arg = parse_input()
	print('### Start copy ####')

	for root in arg.source:
		sync_root(root, arg)
	print('### Done ###')
