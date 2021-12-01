def get_titles_links(links, subtexts):
    final_list = []

    for idx, item in enumerate(links):
        title = links[idx].getText()                      # getting all titles
        link = links[idx].get('href', None)               # getting all links
        subtext = subtexts[idx].select('.score')          # getting the list of all elements with class 'score'
        if subtext:
            points = int(subtext[0].getText()[:-6])       # retreiving all integer scores
            if points > 100:
                final_list.append({'Title': title, 'Link': link, 'Votes': points})  #Appending all elements as a dictionary to the list

    return final_list
