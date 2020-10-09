  
# Modul
import sys
import urllib3
from bs4 import BeautifulSoup


def scan(x):

    # Using readline() 
    scan = open('urbanscan.txt', 'r') 
    count = 0
    pricelist =[]

    #get max line from file
    num_lines = sum(1 for line in open('urbanscan.txt'))
   
    while True: 
        count += 1

        # Get next line from file 
        line = scan.readline() 
  
        # if line is empty 
        # end of file is reached 
        if not line: 
            break
        if count > 13 and count < (num_lines - 2):
            output = line.strip()
            output = output[:-14]
            print("{}".format(output)) 
        
            # Writing to a file 
            urls = open( x, 'a')
            url = "https://urbansportsclub.com/de" + output 
            
            
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            #dummy for write html to file
            #urls.writelines(str(r.data))
            soup = BeautifulSoup(r.data)
            findings = soup.find_all('p',{'class':'smm-membership-plans__plan-price'})
            for price in findings:
                price_string = price.text
                price_string = price_string.replace("\n", "")
                price_string = price_string.replace("\xa0", "")
                price_string = price_string.replace(" ", "")
                price_string = price_string.replace("/Monat*","")
                price_string = price_string.replace("*","")
                pricelist.append(price_string)
            pricelist = list(dict.fromkeys(pricelist))
            url = url + " " + str(pricelist)
            urls.write((url))
            urls.write("\n")
            pricelist.clear()

    urls.close()  
    scan.close() 
	


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please specify a file name to save the urls')
    else:
        arg = (sys.argv[1])
        f = scan(arg)
        print('Write urls to file {0}'.format(arg))


