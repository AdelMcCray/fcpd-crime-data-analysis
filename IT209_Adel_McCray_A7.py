class FCPDCrime(list):
    def __init__(self, name):
        self.name = name
        super().__init__()
    
    def load(self, file = 'crime.csv'):
        o_file = open(file, 'r')
        f_lines = o_file.readlines()
        for l in f_lines[1:]:
            lines = l.strip().split(',')
            self.append(lines)
        o_file.close()
        return len(self)
        
    def printCrimes(self, zip = 'all', type = 'all', date = 'all'):
        for crime in self:
            if (zip == 'all' or crime[2] == zip) and (type == 'all' or crime[4] == type) and (date == 'all' or crime[1] == date): 
                print(crime)
                
    def zipCodeList(self, zip_c):
        zip_list = []
        for i in self:
            if i[2] == zip_c:
                zip_list.append(i)
        return zip_list
        
        
    def countByZip(self):
        zip_count = {}
        for i in self:
            zp = i[2]
            zip_count[zp] = zip_count.get(zp, 0) + 1
        total_ct = len(self)
        for z in sorted(zip_count):
            print(f"{z}: {zip_count[z]} ({zip_count[z] / total_ct:.2%})")
            
    def countByCrime(self, select = 'all'):
        crime_ct = {}
        for i in self:
            if select == 'all' or i[2] == select:
                ct = i[4]
                crime_ct[ct] = crime_ct.get(ct, 0) + 1
        for ct in sorted(crime_ct):
            print(f"{ct}: {crime_ct[ct]}")
            
            

    
FC = FCPDCrime("Fairfax County Police Crime Report")

   
count = FC.load("crime.csv")
print("Records loaded:", count)
print()

   
print("All Crimes:")
FC.printCrimes()
print()

   
print("Crime Counts by Zip:")
FC.countByZip()
print()

    
print("Crime Counts by Type:")
FC.countByCrime()
print()
