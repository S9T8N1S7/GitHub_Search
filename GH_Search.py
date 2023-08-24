import requests

def search_repositories(keywords):
    for keyword in keywords:
        url = f"https://api.github.com/search/repositories?q={keyword}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total_count = data['total_count']
            print(f"Results for '{keyword}': {total_count} repositories found")

            for item in data['items']:
                print(f"Name: {item['name']}")
                print(f"Description: {item['description']}")
                print(f"URL: {item['html_url']}")
                print("--------------------------")
        else:
            print(f"Error occurred while searching for '{keyword}': {response.status_code}")

# Слова-триггеры, используемые для поиска
keywords = ["hello", "privet"]
search_repositories(keywords)
