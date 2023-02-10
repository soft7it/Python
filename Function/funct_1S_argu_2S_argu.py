def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name':'John', 'age': 25}

student_info( *courses, **info)