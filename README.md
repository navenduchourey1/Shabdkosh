# Shabdkosh
# Libraries used

- __BeautifulSoup__ is a Python library for pulling data out of HTML and XML files. And it provides idiomatic ways of navigating,
searching and modifying the parse tree.
- __Requests__ is a Python HTTP library, released under the Apache2 License. The goal of the
project is to make HTTP requests simpler and more human-friendly.
- __Json__ to work with JSON data in python we must import this library.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Bs4/Beutifulsoup and Request.

```bash
pip install Bs4
Pip install Requests
```
## Usage
The script is very easy to use to just have to download the additional 2 libraries(Bs4 and Requests) and rest are already available
in python.
you must provide the specific page URL to the Requests.get method to send an HTTP request to the page.
other than that you should also define the columns to be scrapped in the variable 

 > NUMBER_OF_COLUMNS_TO_SCRAPE max limit is 4.
 
If you want an insight into how program works uncomment the print statements in the program and it will help you gain some more knowledge
about the program.
> Output will be saved in a JSON file after completion.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
