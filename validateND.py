def validate_north_data(name, code):
    import requests
    import re
    import bs4

    url = 'https://www.northdata.de/'
    #company = 'a) Weingut Bergdolt-Reif & Nett GmbH&Co.KG'
    #code = 'HRA 61393 Ludwigshafen a. Rhein'
    
    search_url = url + name + '+' + code
    search_url = re.sub(r" ", "+", search_url)
    r = requests.get(search_url)
    
    try:
        soup = bs4.BeautifulSoup(r.text, "lxml")
        name = soup.find_all("a", class_="title")[0].text.split(',')[0]
        registerNr = soup.find_all("div", class_="extra text")[0].text

        registerNr = [int(s) for s in str.split(registerNr) if s.isdigit()][0]

        code = [int(s) for s in str.split(code) if s.isdigit()][0]

        if code == registerNr:
            return name
        #else:
        #    return None
    except:
        return False