# Create a function named ds with parameters roll_no and name
def ds(roll_no, name):
  
  # Add those parameters in the following data structures: list, tuple, sets and dictionaries 
  lst = [roll_no, name]
  tup = (roll_no, name) 
  st = {roll_no, name} 
  dct = {"roll_no": roll_no, "name": name}

  print("Initial values:")
  print("List:", lst)
  print("Tuple:", tup)
  print("Set:", st)
  print("Dictionary:", dct)

  # After adding values change the values during runtime 
  lst[0] = 1 
  lst[1] = "Kingo" 

  tup = (5, "Prabhat") 
  
  st.remove(roll_no) 
  st.remove(name) 
  st.add(67) 
  st.add("Yash")
  
  dct.update({'roll_no':99})
  dct.update({'name':'Raiden'})

  print("\nUpdated values:")
  print("List:", lst)
  print("Tuple:", tup)
  print("Set:", st)
  print("Dictionary:", dct)

  # Delete these data structures
  del lst 
  del tup 
  del st 
  del dct 

ds(43, "Prateek")
