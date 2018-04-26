# Functions:
def getHTML(url):
    import requests
    from bs4 import BeautifulSoup
    req=requests.get(url)
    html=BeautifulSoup(req.text, "html.parser")
    print(html)
    return html
def safeFile(html):
    open_file = open('file.txt', 'w')
    open_file.write(str(html))
    open_file.close()

# User interface:
print('Wellcome to web decode with Python,')
response="write the url of the web you want to deploy:"
print(response)
while response !="":
    response = raw_input("\n Just press Enter to see https://www.milanuncios.com/coches-de-segunda-mano/ by default")
    if response == "":
        html = getHTML("https://www.milanuncios.com/coches-de-segunda-mano/")
    else:
        html = getHTML(response)
print('Do you want to safe the code in a file.txt?')
response=' '
while response !="":
    response = raw_input("\n Y/n\n")
    if response == "" or response == "y" or response == "Y":
        print('Your file has been created')
        safeFile(html)
        response = ''
    elif response == 'n':
        print('Thank for used Python decode.')
        response = ""
