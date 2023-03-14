# Git & GitHub Homework

### Local

* Create a folder in your week\_01/day_1 directory

```
mkdir precourse_recap
cd precourse_recap
```

* Initialize a git repository in the folder

```
git init
```

* Create a new file called precourse_recap.py

```
touch precourse_recap.py
```
* In the file, write a simple Python program:

  * create variables of different types
  * call some methods/functions using these variables
  * use some operators (e.g. +, -)

  For example:
  ```python
  # create variables of different types
  day_of_week = "Monday"
  current_week = 1
  current_day_of_week = 1

  # call the print function using the variables and some operators
  # we also use the str() function to convert integers to strings

  print("Today is " + day_of_week + ", Week " + str(current_week) 
        + " Day " + str(current_day_of_week) + " of CodeClan")

  # run your file in your terminal:
  # python3 precourse_recap.py
  #
  # and it should print out:
  # Today is Monday, Week 1 Day 1 of CodeClan
  ```

  Another example:
  ```python
  current_week = 1
  current_day_of_week = 1
  total_course_weeks = 16
  total_course_days_per_week = 5

  def weeks_to_go():
    weeks_left = total_course_weeks - current_week
    days_left = total_course_days_per_week - current_day_of_week
    print(f"Only {weeks_left} weeks and {days_left} days to go!")
      

  def motivate_me():
    print("We got this!! You're doing great!!!")

  
  weeks_to_go()
  motivate_me()

  # Only 15 weeks and 4 days to go!
  # We got this!! You're doing great!!!
  ```

* Save the file!
* Stage the file

```
git add .
```

* Commit the files to the repository

```
git commit -m "first commit"
```

### Remote - Github

* Create a new repository

### Local

* Add the Github remote
* Push to the remote repository

```
git push origin main
```
