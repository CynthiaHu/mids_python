# start Git Bash on Windows
# go to the directory for the python assignment
cd Desktop\python_course
cd assignment-upstream-fall-2016\week_1

# create s1 folder and s2, s3 under s1
mkdir s1
cd s1
mkdir s3
mkdir s2

# create a file in s3 and write to it
touch s3\conf.txt
@echo I love bash scripting. >> s3\conf.txt

# create file under s2
touch s2\text_chunk1.txt
@echo A whole new world. >> s2\text_chunk1.txt
@echo A new fantastic point of view. >> s2\text_chunk1.txt

# create another folder and file in s2
cd s2
mkdir Advanced

# copy the file to another folder and add string
# have to use \ instead of / for copying files
copy text_chunk1.txt Advanced\text_chunk2.txt
@echo Do you want to build a snowman? >> Advanced\text_chunk2.txt
