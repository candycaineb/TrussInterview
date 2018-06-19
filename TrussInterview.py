import csv
import datetime
import sys

newRows = list() #Contains the data for the new csv file
f = sys.stdin.read().splitlines()
reader=csv.DictReader(f)
for row in reader:
    timeStamp = row["Timestamp"]       
    FormattedTime = datetime.datetime.strptime(timeStamp, '%m/%d/%y %I:%M:%S %p').strftime('%y-%m-%d %I:%M:%S %p') #Change format of the date
    EstTime = datetime.datetime.strptime(FormattedTime, '%y-%m-%d %I:%M:%S %p') + datetime.timedelta(hours=3)#Add 3 hours to change PST to EST
    newTime = EstTime.strftime("%y-%m-%d %I:%M:%S %p")

    address = row["Address"]
    
    ZIP = row["ZIP"]
    newZip = str("%05d" % int(ZIP))

    fullName = row["FullName"]
    newName = (fullName.upper())

    fooDuration = row["FooDuration"]
    hr, minu, sec = fooDuration.split(':')
    sec, ms = sec.split('.')
    foo = float(sec) + int(ms)/1000.0 + int(minu)*60000 + int(hr)*360000#convert everything to sec

    barDuration = row["BarDuration"]
    hr, minu, sec = barDuration.split(':')
    sec, ms = sec.split('.')
    bar = float(sec) + int(ms)/1000.0 + int(minu)*60000 + int(hr)*360000#convert everything to sec

    ttlDuration = foo+bar

    notes = row["Notes"]
    
    newRows.append(newTime + ";" + address + ";" + newZip + ";" + newName + ";" + str(foo) + ";" + str(bar) + ";"+ str(ttlDuration) + ";" + notes )                     



#Write the output to sys.stdout
writer = csv.writer(sys.stdout, delimiter=',')
writer.writerow(reader.fieldnames)
for row in newRows:
    time, addr, zc, nm, foo, bar, ttl, notes = row.split(';')
    writer.writerow([time]+ [addr]+ [zc]+ [nm]+ [foo]+ [bar]+ [ttl]+ [notes])#zip code is written with 0 prefix, certain apps may not show the 0 prefix
    


