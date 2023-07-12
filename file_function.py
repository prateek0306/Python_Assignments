def file_func(file='assign7.txt'):
    try:  
      f=open(file,'+a')
      f.writelines([' roll no-43\n','name-prateek\n','class-TYCO'])
      f.seek(0)
      print(f.readlines())
      f.close()
    except IOError:
       print('IOError raised')
file_func()



