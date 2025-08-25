1. How to concatenate strings in python? 
   We can generate by using '+' operator, str1+str2
2. What is the purpose of the __dict__ attribute in Python?
    To store the attributes of an object

3. How do you create a dictionary using a comprehension in Python?
    There are many ways to create a dictionary like- using {'curly braces'}, using list container: dict(), making empty dictionary {} and then adding keys and values, and using a comprehension in python.

    ```bash
        {key_expr: value_expr for item in iterable if condition}
    ```
    ```bash
           nums = [1, 2, 3, 4]
           squares = {n: n**2 for n in nums}
           print(squares)
    ```
4. How do you create a multiline string in Python?
   We can create a multiline string using triple quotes (''' or """)     

5. How do you convert a floating-point number to an integer in Python?
   In Python, we can convert a floating-point number(float) to an integer(int) using the built-in int() functions

6. How do you convert a list of strings to a single string in Python?
   We can convert a list of strings into a single string by using the join() method.   
   ```bash
          words = ["Python", "is", "fun"]
          sentence = " ".join(words)   # join with a space
           print(sentence)
    ```

7. What is the output of the following code? 
```bash
       x = [1, 2, 3, 4]
       y = filter(lambda a: a % 2 == 0, x)
       print(list(y))
```
    filter() function keeps only elements where the lambda returns True. Here, it keeps even numbers, so the output is [2, 4]

8.  What is the purpose of the enumerate() function in Python?
    The enumerate() function in Python is used when you want to iterate over a sequence (like a list, tuple, or string) and keep track of both the index and the value at the same time.
    example:
    ```bash
           fruits = ["apple", "banana", "cherry"]
           for index, fruit in enumerate(fruits):
               print(index, fruit)
    ```

9. How do you check if a key is present in a dictionary?
   Using- key in dictionary
   ```bash
          my_dict = {"a": 1, "b": 2, "c": 3}
          print("a" in my_dict)   
    ```

10. How do you find the length of a list in Python?
Using- len(list)  # 'list' is list name                   

11. What is the purpose of the max() function in Python?

    To find the maximum value in a list

12. What is a variable in python?

    A location in memory to store data.

13. What is the output of the following code?

    ```bash x = 5
            y = 2
            print(x // y)  
    ```
    2

14. What is the correct way to check if a variable is of a specific type in Python?

    The correct way to check if a variable is of a specific type is to use isinstance() .           
    ```bash
           x = 10
           if isinstance(x, int):
               print("x is an integer")
    ```

15. How do you convert a string to an integer in Python?

   We can convert a string to an integer using the built-in "int()" function.
   ```bash
          num_str = "42"
          num_int = int(num_str)
    ```

16. What is the scope of a global variable in Python?

    A global variable is a variable that is defined outside of all functions and classes.

    ##### 📌 Scope:

    (a) Accessible throughout the entire file (module) where it is defined.

    (b) Can be read from inside functions and classes (without redefining).

    (c) Can be modified inside a function only if you explicitly declare it as global

17. What does the type() function return in Python?

    The type of the variable

18. Which of the following data types is immutable in Python?

    Tuple 

19. Which of the following is a valid variable name in Python?

    * Rules for valid variable names in Python:

      (a) Must begin with a letter (a–z, A–Z) or an underscore (_).

      (b) Cannot start with a digit.

      (c) Can contain letters, digits, and underscores.

      (d) Cannot contain special characters (-, @, #, etc.).

      (e) Cannot be a reserved keyword (like global, class, if, etc)
       