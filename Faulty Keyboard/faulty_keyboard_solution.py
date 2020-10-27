def faulty_keyboard(string):
  faulty_string = ""
  count = 0

  for word in string:
    for char in word:
      if(char == "A" or char == "a"):
        count += 1

      else:
        if(count == 0):
          faulty_string += char
        elif(count%2 != 0):
            faulty_string += char.upper()
        elif(count%2 == 0):
            faulty_string += char.lower()

        
    print(faulty_string +"\n")
  return faulty_string

def main():
  correct_string = "My name is Shashwat"
  print(faulty_keyboard(correct_string)) ## My nME IS SHshwT

main()