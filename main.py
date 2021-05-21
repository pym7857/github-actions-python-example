import os
from datetime import datetime
from pytz import timezone
from weather import parsing_beautifulsoup, extract_weather
from github_utils import get_github_repo, upload_github_issue

if __name__ == "__main__":
    access_token = os.environ['YM_SECRET']
    repository_name = "github-actions-python-example"

    url = "https://www.weather.go.kr/w/weather/forecast/short-term.do"

    soup = parsing_beautifulsoup(url)
    upload_contents = extract_weather(soup)

    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")