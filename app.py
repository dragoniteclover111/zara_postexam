print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling.Life is good.")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find something fun to do.")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("Get some sleep. You deserve a good rest after all the hard work you did!")
      counter += 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("you'll do well")
      counter += 1
   if each_word == "relieved"
      feelings_list.append ("relieved")
      encouragement_list.append ("I knew wou would do fine!") 
      if each_word == "disappointed"
      feelings_list.append ("disappointed")
      encouragement_list.append ("It's ok if you didn't do well this time! You can always try again and do better next year! Don't give up!") 
      if each_word == "doubtful"
      feelings_list.append ("doubtful")
      encouragement_list.append ("Don't think too much about it! You've worked hard and I'm sure you'll do fine!") 
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
