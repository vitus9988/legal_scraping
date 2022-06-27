from module import web_crawling as wc
import urllib.robotparser


def robots_checker(robots_page, inner_page):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(f"{robots_page}")
    rp.read()
    return rp.can_fetch("*", f"{inner_page}")


def main(robots_page, inner_page):
    if robots_checker(robots_page, inner_page) is True:
        soup = wc(inner_page)
        print(soup)
    else:
        print('error')


if __name__ == '__main__':
    #main("https://www.dcinside.com/robots.txt",'https://gall.dcinside.com/board/lists/?id=tree')
    main('https://www.tistory.com','https://www.tistory.com/category/sports')