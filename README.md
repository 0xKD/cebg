# cebg.py
### Chrome Extension Boilerplate Generator
A simple, interactive python script to quickly generate manifest.json and create other specified files and directories for use in a Chrome extension

* Inputs for properties with multiple values (for eg. content_script|js, storage) are separated by a space.
* Subdirectories can be specified (js/plugins/active.js)

cebg in action:

	C:\Users\GitHub\Documents\GitHub\cebg>python cebg.py
	name: GitHub-tools
	version: 0.1.1
	description: Just testing.
	content_scripts|matches: https://*.github.com/* http://*.github.com/*
	content_scripts|js: js/github_tools.js js/jquery.js
	content_scripts|css: css/style.css css/github_bootstrap.css
	permissions: storage
	background|page: background.html
	options_page: options.html
	extension-folder: git-tools
	[creating]: git-tools\js
	[creating]: git-tools\js
	[creating]: git-tools\css
	[creating]: git-tools\css
	[creating]: git-tools
	[creating]: git-tools
	[creating]: git-tools\js\github_tools.js
	[creating]: git-tools\js\jquery.js
	[creating]: git-tools\css\style.css
	[creating]: git-tools\css\github_bootstrap.css
	[creating]: git-tools\background.html
	[creating]: git-tools\options.html