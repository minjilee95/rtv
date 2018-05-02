import urllib


def photoName(url):

    link = list(url)
    #print(link)

    totalElements = len(link)
    fileNumber = totalElements - 10
    #print(link[fileNumber:])

    return(''.join(link[fileNumber:]))


def downloader(url, fileName):

    urllib.urlretrieve(url, fileName)


def main():

    url = ('https://i.redd.it/anw3funzp8u01.jpg')

    #print(url)

    name = photoName(url)
    #print(name)
    downloader(url, name)
    print("\nYour Image Has Been Saved")


if __name__ == "__main__":
    main()