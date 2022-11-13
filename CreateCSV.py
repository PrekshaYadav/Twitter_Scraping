import csv

#creating CSV file to store all the hashtags
fieldnames = [['#unishortlisting'],['#usgradstudies'],['#usgradshortlisting']]
with open('unitag.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for sublist in fieldnames:
        writer.writerow(sublist)


