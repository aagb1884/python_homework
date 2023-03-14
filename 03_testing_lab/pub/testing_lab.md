# Lab - Pub

## Task

The task for this lab is to plan and create an object oriented model of a Pub, with Drinks and Customers! You should write tests for all your classes and methods. Make sure that you create a separate file for each class and a separate test file for each class.

## Learning Objectives

1. Create your own classes
2. Create multiple objects
3. Add some properties
4. Add some methods and behaviours
5. Get methods and behaviours to interact with properties
6. Get classes to interact with each other
7. Test classes and methods
 

Advanced extensions:

  - Create a `Food` class, that has a `name`, `price` and `rejuvenation_level`. Each time a `Customer` buys `Food`, their `drunkenness` should go down by the `rejuvenation_level`
  - Pub can have a `stock` (maybe a Dictionary?) to keep track the amount of `drinks` available (Hard! Might need to change the drinks List to a drinks Dictionary)
  - Pub can have a `stock_value` method to check the total value of its `drinks`
  - Perhaps `Customer`s can be served in groups, not just individually. But the whole group should get denied service if one of the parties has too much `drunkenness`. **Hint:** This could be solved with list comprehension, but a conditional for loop would do it too!

### Files and Directories

  - In your working directory, create two directories, one for your classes and one for your tests
  - create a `run_tests.py` file in your working directory. Use this file to run your tests.
  - If a method returns a boolean i.e. `True` or `False` then create _at least_ two tests for the method, one where you expect the result to be `True`, and one where you expect the result to be `False`

**REMEMBER** to commit to git regularly