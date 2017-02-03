page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">polymorphic desire so much of a <a href="http://www.wikipedia.org"> flying sideways like a goose during a hurricane.')


#start_link = page.find('<a href="http://'[9:])
#end_link = page.find('"', start_link)
#url = page[start_link: end_link]
#print url


def to_get_target(s):
    start_link = s.find('<a href=')
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', start_quote + 1)
    url = s[start_quote + 1 : end_quote] 
    return url, s[end_quote:] 