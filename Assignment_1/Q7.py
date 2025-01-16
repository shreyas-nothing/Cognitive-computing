# Q.7.1 Write a program to create a text file, write some text into it, and then read and print the content.
with open('example.txt','w') as file:
    file.write('Hello world.\n\tHow are you all?')
    file.write('\n\tThis is an example file')

with open('example.txt','r') as file:
    content = file.read()
    print('File content : ',content)

print('\n')
# Q.7.2 Write a program to append text to an existing file and print the updated content.
with open('example.txt','a') as file:
    file.write('\n\tThis line is updated')

with open('example.txt','r') as file:
    content = file.read()
    print('Updated file content : ' , content)

print('\n')
# Q.7.3 Write a program to count the number of lines in a text file.
with open('example.txt','r') as file:
    lines = file.readlines()
    
count_line = len(lines)
print(count_line)