import requests
from bs4 import BeautifulSoup
from getcontents import get_titles_links
import pandas as pd
import pprint


def main():
    final_list = []

    for i in range(1,3):
        url = "https://news.ycombinator.com/news?p=" + str(i)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')        # getting the html content of the page
        links = soup.select('.titlelink')                         # getting the list of all elements with class 'titlelink'
        subtexts = soup.select('.subtext')                        # getting the list of all elements with class 'subtext'

        final_list_t = get_titles_links(links, subtexts)
        final_list_t.sort(key = lambda x:x['Votes'], reverse=True)
        df1 = pd.DataFrame(final_list_t)
        final_list.append(df1)
    df = pd.concat(final_list, ignore_index=True)
    df.to_csv('Top_hackernews_articles.csv', index=False)

if __name__ == '__main__':
    main()
