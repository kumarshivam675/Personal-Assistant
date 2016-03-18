import csv


def complaintLodge(problem,lat, long, url, caption):
    hello = [[problem,lat,long,url,caption]]

    print lat, long, url, caption
    with open('sidd/complaint.csv', 'a') as testfile:
        csv_writer = csv.writer(testfile)
        csv_writer.writerow(hello[0])	
