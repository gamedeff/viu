# -*- coding: windows-1251 -*-

import os, re
from subprocess import Popen, PIPE

start_n = 2145

first_frame_time = 5
frames_num = 5

video_folder = "J:\Music\Video\Scooter\Live"
screenshots_folder = "screenshots"

viu_log = "viu_log.txt"

outfile = os.path.join(os.getcwd(), "out.txt")

def humanize_time(secs):
	hours = secs // 3600 
	s = secs - (hours * 3600) # remaining seconds
	minutes = s // 60
	seconds = s - (minutes * 60) # remaining seconds
	strtime = "%s" % hours if hours >= 10 else "0%s" % hours
	strtime = strtime + ":" + ("%s" % minutes if minutes >= 10 else "0%s" % minutes)
	strtime = strtime + ":" + ("%s" % seconds if seconds >= 10 else "0%s" % seconds)
	return strtime

def __exec__(*args):
	""" build and execute a command line """
	cmdline = []
	cmdline.extend(args)
	print cmdline
	p = Popen(cmdline, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	p.wait()
	return p.communicate()

def ensure_dir(f):
#	d = os.path.dirname(f)
	if not os.path.exists(f):
		os.makedirs(f)

def getframesnum(f):
	ff = 'getframesnum.bat "%s"' % f.replace("\\", "\\\\");
	print ff
	fin, fout = os.popen4(ff)
	return fout.read()

def process_file(file, nn):
	if nn >= start_n:
		fin, fout = os.popen4('MediaInfo.exe --Inform=file://%s "%s"' % (os.path.join(os.getcwd(), "template.txt"), file))
		#print __exec__("MediaInfo.exe", "--Inform=file://%s" % os.path.join(os.getcwd(), "template.txt"), '"%s"' % file)
		out = open(outfile, "at")
		out.write(fout.read())
		out.write('\r\n[spoiler="Скриншоты"]\r\n')
		out.close()

	ff = 'MediaInfo.exe --Inform=General;%%Duration%% "%s"' % file
	#log.write("%s\r\n" % ff)
	print ff
	total_time = 0
	tt = os.popen4(ff)[1].read()
	try:
		total_time = int(tt) // 1000
	except:
		total_time = int(getframesnum(file)) // 1000
		total_time = total_time // 2
	time_step = (total_time - first_frame_time) // frames_num
	for i in range(0, frames_num):
		if i + nn >= start_n:
			ensure_dir(screenshots_folder)
			frame_image = os.path.join(screenshots_folder, "ss%d.jpg" % (i + nn))
			log = open(viu_log, "at")
			upload_picture = True
			fwd = True
			k = 0
			while not os.path.isfile(frame_image):
				#ff = 'ffmpeg.exe -i "%s" -vframes 1 -ss %s -an -vcodec mjpeg %s' % (file, humanize_time(first_frame_time + k + i * time_step), frame_image)
				ff = 'getframeavs.bat "%s" %d %d' % (file.replace("&", "^&"), first_frame_time + i * time_step, i + nn)
				log.write("%s\r\n" % ff)
				print ff
				os.popen4(ff)[1].read()

				# k = -k
				# if fwd:
					# k = k + 1
				# fwd = not fwd

				# if i * time_step + abs(k) > (i + 1) * time_step or i * time_step - abs(k) < (i - 1) * time_step:
					# sss = "%d > %d or %d < %d" % (i * time_step + abs(k), (i + 1) * time_step, i * time_step - abs(k), (i - 1) * time_step)
					# print sss
					# log.write("%s\r\n" % sss)
					# upload_picture = False
					# break

			if upload_picture:
				#out.write(__exec__("C:\\Python25\\python.exe", "uimge.py", "-p", frame_image, "--bo")[0]) # stdout
				ff = 'C:\\Python25\\python.exe uimge.py -v %s --bo' % frame_image
				log.write("%s\r\n" % ff)
				print ff
				fr = os.popen4(ff)[1].read()
				log.write("%s\r\n" % fr)
				while fr.find("[img]") < 0:
					fr = os.popen4(ff)[1].read()
					log.write("%s\r\n" % fr)
				out = open(outfile, "at")
				out.write(fr)
				out.close()

			log.close()
	out = open(outfile, "at")
	out.write("[/spoiler]\r\n\r\n")
	out.close()

def sortedWalk(target_folder, processed_folders_num, processed_files_num):
	from os.path import isdir, join, splitext

	not_video_exts = [".db", ".txt", ".nfo", ".sfv", ".jpg", ".png", ".mpcpl", ".mp3"]

	# Get the names from inside the path. Get directories and the files
	# into separate lists and then sort them.
	names = os.listdir(target_folder)
	dirs = []
	nondirs = []
	for name in names:
		if isdir(join(target_folder, name)):
			dirs.append(name)
		else:
			nondirs.append(name)

	dirs.sort()
	nondirs.sort()

	if processed_files_num * frames_num + frames_num > start_n:
		out = open(outfile, "at")
		out.write('[spoiler="%s"]\r\n' % os.path.split(target_folder)[1])
		out.close()

	# List the files in this directory first (as a generator).
	for name in nondirs:
		fname = join(target_folder, name)
		if not splitext(fname)[1].lower() in not_video_exts:
			if processed_files_num * frames_num + frames_num > start_n:
				process_file(fname, processed_files_num * frames_num)
			processed_files_num = processed_files_num + 1

	# Generate the content of the subdirectories recursively.
	for subdir in dirs:
#		out.write('[spoiler="%s"]\r\n' % subdir)
		processed_folders_num, processed_files_num = sortedWalk(join(target_folder, subdir), processed_folders_num, processed_files_num)
#		out.write("[/spoiler]\r\n")
#		processed_folders_num = processed_folders_num + 1

	if processed_files_num * frames_num + frames_num > start_n:
		out = open(outfile, "at")
		out.write("[/spoiler]\r\n\r\n")
		out.close()
	processed_folders_num = processed_folders_num + 1

	return [processed_folders_num, processed_files_num]

processed_folders_num, processed_files_num = sortedWalk(video_folder, 0, 0)

print "Processed folders: %d" % processed_folders_num
print "Processed files:   %d" % processed_files_num