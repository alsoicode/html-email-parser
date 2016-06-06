#!/usr/bin/env python
from bs4 import BeautifulSoup, Comment
from mimetypes import MimeTypes
from os.path import exists, splitext
import sys
import xerox


def parse(return_output=True, file_path=None):
    if not file_path:
        try:
            file_path = sys.argv[1]
        except IndexError:
            # assume `email.html`
            file_path = 'email.html'

    # check file exists
    if not exists(file_path):
        raise IOError('File does not exist')

    # check extension and mimetype
    filename, ext = splitext(file_path)
    mime_type = MimeTypes().guess_type(file_path)[0]
    if ext.lower() not in ['.htm', '.html'] or mime_type != 'text/html':
        raise Exception('File does not appear to be an HTML file.')

    # process file
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

        # add unsubscribe link
        unsubscribe_row = body_soup.new_tag('tr')
        unsubscribe_column = body_soup.new_tag('td')
        unsubscribe_column['style'] = 'text-align: right; vertical-align: top; padding: 10px; font: Arial, Helvetica, sans-serif;'
        unsubscribe_link = body_soup.new_tag('a')
        unsubscribe_link.string = 'Unsubscribe'
        unsubscribe_link['href'] = 'http://riverspirittulsaemail.com/unsubscribe/'
        unsubscribe_column.append(unsubscribe_link)
        unsubscribe_row.append(unsubscribe_column)
        body_soup.find_all('tr')[-1].insert_after(unsubscribe_row)

        # right align trouble link text
        body_soup.tr.td['style'] = 'text-align: right; vertical-align: top;'

        output = unicode(body_soup)

        # copy HTML to clipboard FTW
        xerox.copy(output)
        sys.stdout.write('HTML copied to clipboard' + '\n')

        if return_output:
            return output


if __name__ == '__main__':
    parse(return_output=False)
