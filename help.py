my_file = open("abalone_wsex2.txt")
string_list = my_file.readlines()
my_file.close()

missing = False
for i in range(len(string_list)):
  s = string_list[i]
  s_array = s.split(",")
  
  # make sex variable ints
  sex = s_array[0]
  if (sex == "M"): s_array[0] = "0"
  elif (sex == "F"): s_array[0] = "1"
  else:
    string_list[i] = ""
    continue

  for j in range(len(s_array)):
    if (s_array[j] == ""):
      missing = True
  if missing: string_list[i] = ""
  else: string_list[i] = " ".join(s_array)

my_file = open("abalone_wsex2.txt", "w")
new_file_contents = "".join(string_list)
print(new_file_contents)

my_file.write(new_file_contents)
my_file.close()

#length diameter height whole_wt shucked_wt viscera_wt shell_wt rings