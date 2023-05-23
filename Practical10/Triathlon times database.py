# Create a class called	‘triathlon’ which contains various	attributes	about triathletes and their	competitions.
class triathlon (object):
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def all (self,location,time_swim,time_cycle,time_run,time_total):
        print('information: ','name:',first_name +' ' + last_name,' location:',location,' time_swim:',time_swim,' time_cycle:',time_cycle,' time_run:',time_run,' time_total:',time_total)

# Hi, professor, I put the parameters outside the class instead of putting them inside of the parentheses, thinking that it may be more convenient for you to modify the data.
fist_name = 'Bob'
last_name = 'Black'
location ='Wahington'
time_swim = 20
time_cycle = 30
time_run = 30
time_total = time_swim+time_cycle+time_run
# include an example of	using this	class	within	your	code.
# Hi, professor, you can also edit the name in the parentheses below.
triathlon('Bob','Black').all(location, time_swim, time_cycle,time_run, time_total)
# output: information:  name: Bob  location: Wahington  time_swim: 20  time_cycle: 30  time_run: 30  time_total: 80
