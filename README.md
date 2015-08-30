# html-email-parser
Converts HTML exported from Adobe Fireworks to old-school HTML for emails.

## Requirements
 - A Linux distro, like Ubuntu
 - [BeautifulSoup 4](http://www.crummy.com/software/BeautifulSoup/)
 - [Xerox](https://github.com/kennethreitz/xerox)
 - xclip

xclip may be installed via: `apt-get install xclip` on Ubuntu

## Usage
It is recommended that you symlink parser.py into your /usr/local/bin for ease-of-use.

    sudo ln -s path/to/parse.py /usr/local/bin

and set the file to executable:

    sudo chmod +x path/to/parse.py

The parser will process the contents of the path passed as the first argument:

    $ parse.py path/to/file.html

which, if successfully parsed, will copy the HTML to the clipboard and output:

    $ HTML copied to clipboard
