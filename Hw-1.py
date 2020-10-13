dbase = [
    '+5(4671)849-6225',
    '+394(63)128-1148',
    '535(02)715-68-89',
    '+72(23)661-8520',
    '+194(455)628-2961',
    '092158146777',
    '+862(179)416-6138',
    '+3(2697)794-4711',
    '+98(393)874-4458',
    '+3(632)626-8042',
    '+7611528-9013',
    '+88135130-7172',
    '94(3005)670-58-48',
    '+264925558-7301',
    '58(6929)091-8491',
    '+581(067)254-6659',
    '+4(838)997-1720',
    '+7(163)228-1948',
    '72236618520',
    '967(28)959-4951',
    '+53(2121)207-3793',
    '+80(922)2856718',
    '7121-2173999'
]
print(f"{dbase}\n")
newDbase = []
list = []
for x in dbase:
    newDbase.append(
        x.strip('+').replace('(', '').replace(')', '').replace('-', ''))

countryCodeCheck = []
print(f"{newDbase}\n")
longestNum = newDbase[0]

for x in newDbase:
    countryCode, regionalCode, personalNumber = (x[:len(x) - 10:1]), \
                                                x[len(x) - 10:len(x) - 7:1], \
                                                x[len(x) - 7::1]
    print(f"{x} {(countryCode, regionalCode, personalNumber)}")  # (71, 987, 4216455)

    if len(longestNum) < len(x):
        longestNum = x
    if countryCode == '7':
        list.append(x)
    countryCodeCheck.append(countryCode)
print(f"\n int the database {len(newDbase)} number\n")
dBaseSet = set(newDbase)
print(f" remove the repeated number: {len(dBaseSet)} ]\n")
print(countryCodeCheck)
countryCodeCheck = set(countryCodeCheck)
print(countryCodeCheck)
print(f" in the database: {len(countryCodeCheck)} country\n")
print(f" the longest number:{longestNum} and it length: {len(longestNum)} \n")
print(" the russian numbers in the database", list)
