#!/usr/bin/env python3
import webbrowser
import sys

search_sources =  [
    'medium.com',
    'stackoverflow.com',
    'stackexchange.com',
    'learn-cpp.org',
    'realpython.com',
    'users.rust-lang.org'
]


def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def main():
    query = create_query()
    if not query:
        print("Please provide a search query.")
        sys.exit(1)

    # Appending site filters to the query
    site_filters = ' OR '.join([f'site:{site}' for site in search_sources])
    full_query = f"{query} {site_filters}"

    url = f"https://www.google.com/search?q={full_query.replace(' ', '+')}"
    webbrowser.open(url)

if __name__ == "__main__":
    main()


