import requests
import os
from bs4 import BeautifulSoup
import re
import time


s = requests.Session() 
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    })

def load_user_data(session, url):
    url = 'https://www.6pm.com' + str(url)
    request = session.get(url)
    #request = requests.get(url, proxies={"http":"http://10.10.1.10:3128"})
    return request.text

def pars(s, url) :
    data = load_user_data(s, url)
    soup = BeautifulSoup(data, features="lxml")
    link_list = soup.findAll('article', {'class': ['ob Db HN searchThreeWideMobile rb ub']})

    for i in link_list :
        link_list2 = i.find('a').get('href')
        
        new_price = i.find('span', {'class': 'Ob Pb'})
        new_price = str(new_price)
        new_price = re.findall('\$.*<' , new_price)
        new_price = str(new_price)
        new_price = re.sub( r'(\$)|(<)', '', new_price)
        new_price = re.sub(r',','' , new_price)
        new_price = float(new_price[2:-2])

        
        old_price = i.find('span', {'class': 'Bb'})
        old_price = str(old_price)
        old_price = re.findall('\$.*<' , old_price)
        old_price = str(old_price)
        old_price = re.sub( r'(\$)|(<)', '', old_price)
        old_price = re.sub(r',','' , old_price)
        old_price = float(old_price[2:-2])


        sale = (1- (new_price /old_price) ) * 100
        #print(sale)
        if( float(sale) > 77 ) :
            print(link_list2)
            RecordToFile('https://www.6pm.com' + link_list2, sale)

def isValidPage(url, s) :
    data = load_user_data(s, url)
    soup = BeautifulSoup(data, features="lxml")
    try:
        link_list = soup.find('div',{'class':['KN']}).find('h1').text
        link_list = str(link_list)
        #No Results Found
    except :
        return True
    
    if( link_list != 'No Results Found' ) : 
        return True
    else :
        return False

def RecordToFile(link, discont) :
    with open('6p_discont_today.txt', 'a+') as output_file:
        print(link, file=output_file)
        print(discont, file=output_file)
        print("\n")
        
brands_list = [
'/adidas/WgEB4gIBCw.zso?s=percentOff/desc/',
'/adidas-by-stella-mccartney/WgKzD-ICAQs.zso?s=percentOff/desc/',
'/adidas-golf/WgKDD-ICAQs.zso?s=percentOff/desc/',
'/adidas-golf-kids/WgLzHeICAQs.zso?s=percentOff/desc/',
'/adidas-kids/WgLgA-ICAQs.zso?s=percentOff/desc/',
'/adidas-originals/WgLSBuICAQs.zso?s=percentOff/desc/',
'/adidas-originals-kids/WgKYHOICAQs.zso?s=percentOff/desc/',
'/adidas-outdoor/WgLNGeICAQs.zso?s=percentOff/desc/',
'/adidas-outdoor-kids/WgKvGeICAQs.zso?s=percentOff/desc/',
'/adidas-running/WgLhBuICAQs.zso?s=percentOff/desc/',
'/adidas-skateboarding/WgLsHOICAQs.zso?s=percentOff/desc/',
'/alexander-mcqueen/WgKFEOICAQs.zso?s=percentOff/desc/',
'/asics/WgEL4gIBCw.zso?s=percentOff/desc/',
'/asics-kids/WgKmBuICAQs.zso?s=percentOff/desc/',
'/asics-tiger/WgKgI-ICAQs.zso?s=percentOff/desc/',
'/boss-hugo-boss/WgLAA-ICAQs.zso?s=percentOff/desc/',
'/boutique-moschino/WgLuI-ICAQs.zso?s=percentOff/desc/',
'/calvin-klein/WgKoCeICAQs.zso?s=percentOff/desc/',
'/calvin-klein-kids/WgLBEOICAQs.zso?s=percentOff/desc/',
'/calvin-klein-plus/WgK8H-ICAQs.zso?s=percentOff/desc/',
'/calvin-klein-underwear/WgKOF-ICAQs.zso?s=percentOff/desc/',
'/canali/WgK3JeICAQs.zso?s=percentOff/desc/',
'/chloe/WgKJFeICAQs.zso?s=percentOff/desc/',
'/chloe-gosselin/WgKfI-ICAQs.zso?s=percentOff/desc/',
'/chloe-kids/WgKyHOICAQs.zso?s=percentOff/desc/',
'/clarks/WgKQAuICAQs.zso?s=percentOff/desc/',
'/clarks-kids/WgK-FuICAQs.zso?s=percentOff/desc/',
'/columbia/WgLOAuICAQs.zso?s=percentOff/desc/',
'/columbia-college/WgLcJ-ICAQs.zso?s=percentOff/desc/',
'/columbia-kids/WgKqBOICAQs.zso?s=percentOff/desc/',
'/converse/WgEk4gIBCw.zso?s=percentOff/desc/',
'/converse-kids/WgLcA-ICAQs.zso?s=percentOff/desc/',
'/converse-skate/WgKEJeICAQs.zso?s=percentOff/desc/',
'/diesel/WgLGAuICAQs.zso?s=percentOff/desc/',
'/dkny/WgLdAuICAQs.zso?s=percentOff/desc/',
'/dkny-intimates/WgKbGeICAQs.zso?s=percentOff/desc/',
'/dolce-gabbana/WgKpGeICAQs.zso?s=percentOff/desc/',
'/dolce-gabbana-kids/WgK1I-ICAQs.zso?s=percentOff/desc/',
'/dsquared2/WgKABuICAQs.zso?s=percentOff/desc/',
'/emporio-armani/WgKgHuICAQs.zso?s=percentOff/desc/',
'/fendi-kids/WgLDG-ICAQs.zso?s=percentOff/desc/',
'/fossil/WgLEC-ICAQs.zso?s=percentOff/desc/',
'/g-star/WgLQFuICAQs.zso?s=percentOff/desc/',
'/giorgio-armani/WgL6FuICAQs.zso?s=percentOff/desc/',
'/gucci/WgL5FuICAQs.zso?s=percentOff/desc/',
'/guess/WgFN4gIBCw.zso?s=percentOff/desc/',
'/harley-davidson/WgLlAuICAQs.zso?s=percentOff/desc/',
'/ivanka-trump/WgLCGOICAQs.zso?s=percentOff/desc/',
'/kenzo-kids/WgKJI-ICAQs.zso?s=percentOff/desc/',
'/lacoste/WgKsCeICAQs.zso?s=percentOff/desc/',
'/lacoste-kids/WgLKCuICAQs.zso?s=percentOff/desc/',
'/lauren-ralph-lauren/WgLmAuICAQs.zso?s=percentOff/desc/',
'/lauren-ralph-lauren-kids/WgKkJ-ICAQs.zso?s=percentOff/desc/',
'/levis/WgFa4gIBCw.zso?s=percentOff/desc/',
'/levis-kids/WgKlFOICAQs.zso?s=percentOff/desc/',
'/levis-mens/WgLWGOICAQs.zso?s=percentOff/desc/',
'/levis-plus/WgKBGuICAQs.zso?s=percentOff/desc/',
'/levis-premium/WgKTJeICAQs.zso?s=percentOff/desc/',
'/levis-shoes/WgKCGuICAQs.zso?s=percentOff/desc/',
'/levis-womens/WgL8GeICAQs.zso?s=percentOff/desc/',
'/reebok/WgKAAeICAQs.zso?s=percentOff/desc/',
'/reebok-kids/WgLfA-ICAQs.zso?s=percentOff/desc/',
'/reebok-lifestyle/WgK2BuICAQs.zso?s=percentOff/desc/',
'/reebok-work/WgKnH-ICAQs.zso?s=percentOff/desc/',
'/roberto-cavalli/WgL_BeICAQs.zso?s=percentOff/desc/',
'/timberland/WgKgAeICAQs.zso?s=percentOff/desc/',
'/timberland-pro/WgKTBuICAQs.zso?s=percentOff/desc/',
'/tommy-hilfiger/WgKnB-ICAQs.zso?s=percentOff/desc/',
'/tommy-hilfiger-adaptive/WgLxJOICAQs.zso?s=percentOff/desc/',
'/ugg/WgKgAuICAQs.zso?s=percentOff/desc/',
'/ugg-kids/WgLzA-ICAQs.zso?s=percentOff/desc/',
'/valentino-bags-by-mario-valentino/WgK-H-ICAQs.zso?s=percentOff/desc/',
'/vans/WgKrAeICAQs.zso?s=percentOff/desc/',
'/vans-kids/WgLaA-ICAQs.zso?s=percentOff/desc/',
'/versace/WgL8DuICAQs.zso?s=percentOff/desc/',
'/versace-collection/WgKMG-ICAQs.zso?s=percentOff/desc/',
'/versace-jeans-couture/WgKLG-ICAQs.zso?s=percentOff/desc/',
'/versace-kids/WgKvHOICAQs.zso?s=percentOff/desc/',
'/victorias-secret/WgL9J-ICAQs.zso?s=percentOff/desc/',
'/michael-michael-kors/WgL1B-ICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/michael-kors/WgKKCeICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/moschino/WgKuB-ICAQs.zso?s=percentOff/desc/',
'/new-balance/WgFr4gICCzKSAwtbNzAgVE8gMTAwXQ.zso?s=percentOff/desc/',
'/nike/WgFv4gICCzKSAwtbNzAgVE8gMTAwXQ.zso?s=percentOff/desc/',
'/nike-golf/WgK7GuICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/nike-kids/WgLjDuICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/nike-sb/WgLlFeICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/the-north-face/WgLiBOICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/the-north-face-kids/WgLhCeICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/polo-ralph-lauren/WgL_A-ICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/polo-ralph-lauren-big-tall/WgK2J-ICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/polo-ralph-lauren-kids/WgLBBOICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/prada/WgL3FOICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/puma/WgF94gICCzKSAwtbNzAgVE8gMTAwXQ.zso?s=percentOff/desc/',
'/puma-golf/WgK5D-ICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/',
'/puma-kids/WgLbA-ICAgsykgMLWzcwIFRPIDEwMF0.zso?s=percentOff/desc/'
]
    


page = 0 ;
i    = 0 ;
size = len(brands_list) 
while( size ) :
    if(page) :
        result = isValidPage(brands_list[i], s)
        if(result) :
            pars(s, brands_list[i])
            page = page + 1 
            i = i + 1
            size = size - 1
            time.sleep(1)
            print(size)
    else :
        result = isValidPage(brands_list[i] + '&p=' + str(page) , s)
        if(result) :
            pars(s, brands_list[i] + '&p=' + str(page))
            page = page + 1
            i = i + 1
            size = size - 1
            time.sleep(1)
            print(size)



    
    
    
    
    
    
    
    






