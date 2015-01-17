import mechanize

# The URL to this service
URL = 'http://cepstral.com/cgi-bin/demos/weather'

def main():
    # Create a Browser instance
    b - mechanize.Browser()
    #Load the page
    b.open(URL)
    #Select the form
    b.select form(nr=0)
    #Fill out the form
    b['city'] = 'San Francisco'
    # Submit!
    return b.submit()

if __name__ == '__main__'
    import sys
    sys.stdout.write(main(),read())
