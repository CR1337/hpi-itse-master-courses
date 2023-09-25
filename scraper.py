from typing import List

import requests
from bs4 import BeautifulSoup

from course import Course
from xslx_writer import XlsxWriter


class Scraper:

    BASE_URL: str = "https://hpi.de"
    OVERVIEW_URL: str = (
        f"{BASE_URL}/studium/im-studium/lehrveranstaltungen"
        "/it-systems-engineering-ma.html"
    )
    REQUEST_TIMEOUT: int = 5

    def _request_soup(self, url: str) -> BeautifulSoup:
        try:
            response = requests.get(url, timeout=self.REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print(f"Request timed out: {url}")
            exit(1)
        except requests.exceptions.TooManyRedirects:
            print(f"Too many redirects: {url}")
            exit(1)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e} from {url}")
            exit(1)
        except requests.exceptions.RequestException:
            print(f"Request exception: {url}")
            exit(1)
        else:
            return BeautifulSoup(response.text, "html.parser")

    def _get_course_links(self, overview: BeautifulSoup) -> List[str]:
        table = overview.find(
            "table", {"class": "contenttable contenttable-0 table"}
        )
        a_s = table.find_all("a", {"class": "courselink"})
        return [f"{self.BASE_URL}/{a['href']}" for a in a_s]

    def _get_title(self, course_soup: BeautifulSoup) -> str:
        h1 = course_soup.find("h1")
        return "".join(h1.text.split("(")[:-1]).strip()

    def _get_categories(self, course_soup: BeautifulSoup) -> List[str]:
        return [
            category for category in Course.CATEGORIES
            if category in str(course_soup)
        ]

    def _get_course(self, course_soup: BeautifulSoup) -> Course:
        ul = course_soup.find(
            "ul", {"class": "tx-ciuniversity-course-general-info"}
        )
        course = Course()
        course.title = self._get_title(course_soup)
        lis = ul.find_all("li")
        for li in lis:
            text = li.text
            if "Semesterwochenstunden" in text:
                course.sws = int(text.split(":")[1].strip())
            elif "ECTS" in text:
                course.ects = int(text.split(":")[1].strip())
            elif "Lehrform" in text:
                course.type_ = text.split(":")[1].strip()
            elif "Lehrsprache" in text:
                course.language = text.split(":")[1].strip()
            elif "Belegungsart" in text:
                course.mandatory = "Pflicht" in text
        course.categories = self._get_categories(course_soup)
        return course

    def scrape(self) -> List[Course]:
        overview = self._request_soup(self.OVERVIEW_URL)
        course_links = self._get_course_links(overview)
        course_soups = [self._request_soup(link) for link in course_links]
        courses = [
            self._get_course(course_soup) for course_soup in course_soups
        ]
        return courses


if __name__ == "__main__":
    courses = Scraper().scrape()
    for course in courses:
        print(course)
