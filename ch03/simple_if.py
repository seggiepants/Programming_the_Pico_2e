response = input('Enter a number: ')
try:
    number = int(response)
    if number > 10:
        print('That''s a big number')
    else:
        print('That''s a small number')
except:
    print('That''s not a number.')