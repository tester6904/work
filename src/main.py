name = input("your name: ").strip()

if name:
  style = input("friendly? (y/n):").strip().lower()
greeting = "Hey" if style =="y" else "Welcome"
  print(f"{greetin},{name}!")
else:
  print("Name required.")
  
