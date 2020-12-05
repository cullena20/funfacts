import bs4
import requests
import db_facts

conn = db_facts.connect()
cur = conn.cursor()
db_facts.create_table(conn)


def main():
    html_url = "https://www.thefactsite.com/top-100-random-funny-facts/"
    html_text = requests.get(html_url).text
    soup = bs4.BeautifulSoup(html_text, "html.parser")
    facts = soup.find_all("h2", class_="list")
    for fact in facts:
        fact = fact.text
        db_facts.insert(conn, cur, fact)


if __name__ == "__main__":
    main()
