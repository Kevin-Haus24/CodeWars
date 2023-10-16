def domain_name(url):
    if 'http://' in url:
        url = url.replace('http://', '')
        if 'www.' in url:
            url = url.replace('www.', '')
            url = url[0:url.find('.')]
            return url
        url = url[0:url.find('.')]
        return url

    if 'https://' in url:
        url = url.replace('https://', '')
        if 'www.' in url:
            url = url.replace('www.', '')
            url = url[0:url.find('.')]
            return url
        url = url[0:url.find('.')]
        return url

    if 'www.' in url:
        url = url.replace('www.', '')
        url = url[0:url.find('.')]
        return url
    return url[0:url.find('.')]


print(domain_name("http://google.com"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("www.xakep.ru"))