import re

class bag_rules:
    def __init__(self, your_bag_color, input_file='test.txt', verbose=False):
        self.your_bag_color = your_bag_color
        self.input_file = input_file
        self.verbose = verbose
        self.read_file()
        self.parse_file()

    def read_file(self):
        with open(self.input_file, 'r') as f:
            self.rules = f.read().splitlines()
    
    def parse_file(self):
        bags = {}
        for rule in self.rules:
            results = [x.group().strip() for x in re.finditer('(^.+?(?=bag))|(?=(\d))(.*?)(?=bag)', rule)]
            main_bag = results.pop(0)
            if main_bag not in bags.keys():
                bags[main_bag] = {}
            for result in results:
                a = [x.group().strip() for x in re.finditer('(^[0-9]+)|([a-z ]+)', result)]
                a[0] = int(a[0])
                bags[main_bag][a[1]] = a[0]
        self.bags = bags
    
    def check_contents(self, dictionary):
        return 1 if self.your_bag_color in dictionary.keys() else 0
    
    def check_sub_bags(self, d):        
        if  self.valid == 1:#or self.iterator >= len(self.bags.keys()):
            self.done = True
            return 
        
        for key in d.keys():
            if self.done: continue
            self.iterator += 1
            self.valid = max(self.check_contents(self.bags[key]), self.valid)
            if self.verbose: print(f"\tKEY={key}; VALID={self.valid}; ITER={self.iterator}")
            if self.valid == 1:
                self.done = True
            else:
                self.check_sub_bags(self.bags[key])
            
    
    def count_bags(self):
        n_outer_bags = 0
        for key in self.bags.keys():
            self.valid = 0
            self.iterator = 0
            self.done = False
            
            if key == self.your_bag_color: continue
            self.valid = self.check_contents(self.bags[key])
            
            if self.verbose: print(f"KEY={key}; VALID={self.valid};")
            while not self.done:
                self.check_sub_bags(self.bags[key])
                self.done=True
            n_outer_bags += self.valid
        return n_outer_bags

#part 1
b = bag_rules('shiny gold', input_file = 'input_07.txt', verbose=False)
print(b.bags)
n_outer_bags = b.count_bags()
print()
print(f"There are {n_outer_bags} bags that can contain yours")

