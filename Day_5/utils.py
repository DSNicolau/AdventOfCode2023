class Almanac:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()
        self.almanac = {}
        self.almanac_seeds()
        self.conversions = [ 'seed-to-soil',
                            'soil-to-fertilizer',
                            'fertilizer-to-water',
                            'water-to-light',
                            'light-to-temperature',
                            'temperature-to-humidity',
                            'humidity-to-location' ]
        self.complete_almanac()
        self.current_input = self.almanac['seeds']
    def read_data(self):
        return open(self.filename).read()
    
    def almanac_seeds(self):
        self.almanac['seeds'] = [int(j) for j in ((self.data.split(':')[1]).split('\n')[0]).split()]

    def complete_almanac(self):
        for key,conversion in enumerate(self.conversions):
            if key<len(self.conversions)-1:
                data = [x.split() for x in ((self.data.split(conversion+' map:')[1]).split('\n'+self.conversions[key+1])[0].splitlines()[1:])]
            else:
                data = [x.split() for x in ((self.data.split(conversion+' map:')[1]).splitlines()[1:])]
            self.almanac[conversion] = [self.min_max_dest(x) for x in data]

    def min_max_dest(self, data):
        min = int(data[1])
        max = int(data[1])+int(data[2])-1
        dest = int(data[0])
        return [min, max, dest]
    
    def compute(self):
        self.current_input = self.almanac['seeds']
        for conversion in self.conversions:
            self.find_dest(conversion=conversion)
            

    def find_dest(self,conversion):
        for key,seed in enumerate(self.current_input):
            number = [dest+seed-minim if minim<=seed<=maxim else seed for minim,maxim,dest in self.almanac[conversion]]
            self.current_input[key] = next((num for num in number if num!=seed), seed)

    
    def print_min_location(self):
        return min(self.current_input)