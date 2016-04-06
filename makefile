# extract rhythms from README.md file
extract:
	cat README.md | grep -Po '`([B|T|S-]+)`' | sed "s/[\`\|]//g" > rhythms.txt
