page = 1
test = 1


def nextPage(page, test):
    page += 1
    test = 3
    return page, test


page, test = nextPage(page, test)
