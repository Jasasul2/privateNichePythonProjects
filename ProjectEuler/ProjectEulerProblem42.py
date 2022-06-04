import math 

alphabet_values = {}
alphastring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(alphastring)):
  alphabet_values[alphastring[i]] = i + 1 
print(alphabet_values)

def get_alphabetical_value(text):
  value = 0
  for char in text:
    value += alphabet_values[char]
  return value
  
def check_triangularity(n):
  m = (math.sqrt(8 * n + 1) - 1) / 2
  if(m.is_integer() == True):
    return True 
  return False 
     
with open("words.txt", "r") as file:
  word_list = []
  for line in file:
    list = line.split(",")
    
  total_triangular_count = 0
  
  for i in range(len(list)): 
    clean_word = list[i][1:-1]
    if(check_triangularity(get_alphabetical_value(clean_word)) == True): 
      total_triangular_count += 1
    
  print(total_triangular_count)
  
