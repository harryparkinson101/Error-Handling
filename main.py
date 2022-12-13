# Error Handling
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a number higher than 0')

    if age <= 0:
      print('Age must be a positive integer')
      
    else:
        print('Thank you.')
        break
        
