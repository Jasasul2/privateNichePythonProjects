# Author : Ondřej Maceška 
# Date : 17.12.2021
# Description : 
#   - used for goal comletion - in every text file in this directory, each line of text represents a task 
#   - if the task is marked from the right side as DONE or PROGRESS, you get points 
#   - prints the total percentage of completed tasks 

import os 
cwd = os.getcwd()

def evalauate(filepath):
    with open(filepath, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        done = 0.0
        line_count = 0
        new_string = ""
        for line in lines:
            words = line.split()
            if(len(words) > 0):
                if(words[-1] == "DONE"):
                    done += 1
                elif(words[-1] == "PROGRESS"):
                    done += 0.5
                if(words[0] != "DONE:"):
                    new_string += line
                    line_count += 1.0
        
        file.seek(0)
        file.truncate()
        file.write(new_string)
        file.write(f"\nDONE: {done} / {line_count}")
    
    return (done, line_count)

if __name__ == '__main__':
    files = os.listdir(cwd)
    total_done = 0
    total_lines = 0
    for file in files:
        if(file[0] != "l"):
            result = evalauate(file)
            total_done += result[0]
            total_lines += result[1]
    
    print(f"Totaly done : {total_done} / {total_lines}")
    print(f"Sucess rate: {total_done/total_lines}")