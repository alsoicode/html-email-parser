# html-email-parser
Converts HTML exported from Adobe Fireworks to old-school HTML for emails.

## Requirements
 - [BeautifulSoup 4](http://www.crummy.com/software/BeautifulSoup/)
 - [Xerox](https://github.com/kennethreitz/xerox)
 - xclip

xclip may be installed via: `apt-get install xclip` on Ubuntu

## Usage
It is recommended that you symlink parser.py into your /usr/local/bin for ease-of-use on *nix distros or add the directory for parse.py to your `PATH` environment variable on Windows.

    sudo ln -s path/to/parse.py /usr/local/bin

and set the file to executable (not required for Windows):

    sudo chmod +x path/to/parse.py

The parser will process the contents of the path passed as the first argument:

    $ parse.py path/to/file.html

which, if successfully parsed, will copy the HTML to the clipboard and output:

    $ HTML copied to clipboard
