# Create a class called	‘triathlon’ which contains various	attributes	about triathletes and their	competitions.
class triathlon (object):
    def __init__(self,name):
        self.x = name
    def all (self,location,time_swim,time_cycle,time_run,time_total):
        print('all information: ','name:',name,' location:',location,' time_swim:',time_swim,' time_cycle:',time_cycle,' time_run:',time_run,' time_total:',time_total)

# Hi, professor, I put the parameters outside the class instead of putting them inside of the parentheses, thinking that it may be more convenient for you to modify the data.
name = 'Bob'
location ='Wahington'
time_swim = 20
time_cycle = 30
time_run = 30
time_total = time_swim+time_cycle+time_run
# include an example of	using this	class	within	your	code.
triathlon(name).all(location, time_swim, time_cycle,time_run, time_total)
