try:
    text = input('Enter something -->')
except EOFError:
    print('why did you do an eof on me')
except KeyboardInterrupt:
    print('you cancelled the operation')
else:
    print('you entered {}'.format(text))
