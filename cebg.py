import os, errno
import json
import time
import collections
from pprint import pprint

def mkdir_folder(mkdir_list, folder):
	newlist = []
	for path in mkdir_list:
		newlist.append(folder + '\\' + path)
	return newlist

def mkdir_p(path):
	try:
		print "[creating]:",path
		os.makedirs(path)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else: raise

def touch(fname, times = None):
	with file(fname, 'a'):
		print "[creating]:",fname
		os.utime(fname, times)

def handle_mkdirlist(mkdir_list):
	newlist = []
	for i in mkdir_list:
		newlist.append(i.replace('/','\\'))
	for i in newlist:
		try:
			temp = i.index('\\')
			mkdir_p(i[:i.rfind('\\')])
		except ValueError as exc:
			pass
	for i in newlist:
		touch(i)

__manifest__ = json.loads('{\
	"manifest_version":2,\
	"version":"0.1",\
	"name":"pyExtension",\
	"description":"pyDescription",\
	"content_scripts":[{\
		"matches":[],\
		"js":[],\
		"css":[]\
		}],\
	"permissions":[\
		],\
	"background":{\
			"page":"",\
			"scripts":[]\
		},\
	"options_page":""\
	}', object_pairs_hook=collections.OrderedDict)

def main():
	manifest = __manifest__
	has_bg_page = True
	mkdir_list = []

	print 'name:',
	manifest['name'] = raw_input()

	print 'version:',
	manifest['version'] = raw_input()

	print 'description:',
	manifest['description'] = raw_input()

	print 'content_scripts|matches:',
	cs_matches = raw_input().split(' ')
	if cs_matches != ['']:
		manifest['content_scripts'][0]['matches'] = cs_matches

	print 'content_scripts|js:',
	cs_js = raw_input().split(' ')
	if cs_js != ['']:
		manifest['content_scripts'][0]['js'] = cs_js
		for i in cs_js:mkdir_list.append(i)

	print 'content_scripts|css:',
	cs_css = raw_input().split()
	if cs_css != ['']:
		manifest['content_scripts'][0]['css'] = cs_css
		for i in cs_css:mkdir_list.append(i)

	print 'permissions:',
	perms = raw_input().split()
	if perms != ['']:
		manifest['permissions'] = perms

	# `background` can have either `page` or `script` property
	print 'background|page:',
	bg_page = raw_input()
	if bg_page != '':
		manifest['background']['page'] = bg_page
		mkdir_list.append(bg_page)
	else:
		manifest['background'].pop('page')
		has_bg_page = False

	if not has_bg_page:
		print 'background|scripts:',
		bg_scripts = raw_input().split()
		if bg_scripts != ['']:
			manifest['background']['scripts'] = bg_scripts
			for i in bg_scripts:mkdir_list.append(i)
		else:
			manifest['background'].pop('scripts')
	else:
		manifest['background'].pop('scripts')

	print 'options_page:',
	opt_page = raw_input()
	if opt_page != '':
		manifest['options_page'] = opt_page
		mkdir_list.append(opt_page)

	# pprint(manifest)
	print 'extension-folder:',
	folder = raw_input()
	mkdir_list = mkdir_folder(mkdir_list, folder)
	handle_mkdirlist(mkdir_list)

	with open(folder + '\\'+ 'manifest.json','w') as outfile:
		json.dump(manifest, outfile)

if __name__ == "__main__":
	main()