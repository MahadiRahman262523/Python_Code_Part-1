items = [int,float,"mrd","srs","mrdsrs",29,38,34.78,5,2,1,78,90,56,71,bool,6,6]

for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)