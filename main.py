import os
from datetime import datetime
from pytz import timezone
from weather import parsing_beautifulsoup, extract_weather
from github_utils import get_github_repo, upload_github_issue

if __name__ == "__main__":
    access_token = os.environ['YM_SECRET']
    repository_name = "github-actions-python-example"
    
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_data = today.strftime("%Y년 %m월 %d일")

    url = "http://www.weather.go.kr/w/weather/forecast/short-term.do"

    soup = parsing_beautifulsoup(url, verify=False)
    upload_contents = extract_weather(soup)
    
    issue_title = f"기상청 날씨 예보 알림({today_data})"

    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
