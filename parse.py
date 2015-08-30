#!/usr/bin/env python
from bs4 import BeautifulSoup, Comment
import sys
import xerox


def parse():
    try:
        file_path = sys.argv[1]
    except IndexError:
        # assume `email.html`
        file_path = 'email.html'

    try:
        with open(file_path, 'r') as html_file:
            data = html_file.read()

            # extract body
            soup = BeautifulSoup(data, 'html.parser')
            body = soup.body.contents[1]

            # strip comments
            [comment.extract() for comment in body.findAll(
                text=lambda text: isinstance(text, Comment))]

            # replace image tags with the name of the image
            body_soup = BeautifulSoup(str(body), 'html.parser')
            for img in body_soup.findAll('img'):
                img.replace_with(img['name'])

            # add trouble link row
            trouble_row = body_soup.new_tag('tr')
            trouble_column = body_soup.new_tag('td')
            trouble_column.string = 'trouble'
            trouble_row.append(trouble_column)
            body_soup.tr.insert_before(trouble_row)

            # add inline css to each td
            for td in body_soup.find_all('td'):
                td['style'] = 'text-align: left; vertical-align: top;'

            # right align trouble link text
            body_soup.tr.td['style'] = 'text-align: right; vertical-align: top;'

            # copy HTML to clipboard FTW
            xerox.copy(unicode(body_soup))
            sys.stdout.write('HTML copied to clipboard' + '\n')

    except IOError:
        sys.stdout.write('Could not find path to file.' + '\n')

if __name__ == '__main__':
    parse()
