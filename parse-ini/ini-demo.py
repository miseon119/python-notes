import configparser

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# parse existing file
config.read('hello.ini')

# read values from a section
string_val = config.get('student', 'id')
age_val = config.getboolean('student', 'male')
grade_val = config.getint('student', 'grade')
score_val = config.getfloat('student', 'score')

# update existing value
config.set('student', 'id', 'b222')

# add a new section and some values
config.add_section('teacher')
config.set('teacher', 'id', 'k8')
config.set('teacher', 'age', '38')

# save to a file
with open('hello2.ini', 'w') as configfile:
    config.write(configfile)
