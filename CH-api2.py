import requests

url = "https://www.coursehero.com/subjects/health-science/questions"

querystring = {"__chid":"c60e3039-d6fb-458e-838e-1a969db0f556"}

payload = ""
headers = {
    'cookie': "root_session_id=b4a6247b-7cd9-4d01-b277-079c9ac5674f; device_view=full; visid_incap_987752=pfjvlwCrSCK/2eoEMlDhb8cvnWIAAAAAQUIPAAAAAABMOLpbwzxfYiWK1Wpju+28; last_viewed_question=20883967; nlbi_987752=7XMzXrgwM2WY+Rk05Tz1lQAAAACaAgGsRllPsKfnR1707Ytm; has_called_TBM=1; PHPSESSID=2160ec02-efea-495f-8192-1005dc6ffa99; incap_ses_1171_987752=zf0xWCT+8UpfzD1Z+jpAEAgNnmIAAAAA71B46UmrgzdOIlImNEDx5A==; incap_ses_149_987752=uZycBthlB1h48B6xOlsRAtMQnmIAAAAA1AWFZDh9tNOc9jxLZmVbtA==; incap_ses_8217_987752=Och3Uj31vSFMgv0LaaYIcsMVnmIAAAAAsJUKpA9gi8R4Ngb9TQeLxA==; incap_ses_1460_987752=bdafAgVdr2mETENMh/ZCFEQanmIAAAAAaxAqvUpES+Vo4iP5qY8APw==; incap_ses_1451_987752=T4ioIuT42SgzeJfUHP0iFB4inmIAAAAAY+6wSVyufoEI4+bNuSXXZA==; incap_ses_356_987752=cOpTHFx88Dz0J77SC8/wBCoknmIAAAAAZhBxFjonprOBCaEkk3e0qQ==; nlbi_987752_2147483392=XnAVUx/IcnskBN/i5Tz1lQAAAAABgcCiY9ProTSRcXT7bz3J; incap_ses_1457_987752=gYEbVlPBHH7R3WG1DU44FIknnmIAAAAA6EwIvfkPZBuTolaRCos/WQ==; reese84=3:4Mt+x+oCs0Q5DbFyKkd4Zw==:tPSj55Mk1az+RCNHTormFCmRSiSS3mZKE/GAW+Bb8IAtzgR45GqAAdTKnQpS3m0K1plWdH5AqXmAm+Uwu5lnpq9BDj5oJf5GA54ud+wjiF3FngL+in/wqPgzDIXF3xaLtLZubcYsyjg1uE8AmwWuRT8AreTtNjz4ZqL+F9JgIlL9OH7HyJ4qPjgamUiWqoazCukZhTOuya/rXtw6FjAjch7hUYk8UYsQAyIbYCOdlL1tWUWftqYDlW8eUNvBX1XFJPsJEIS5FDkTnrZj3pwAuA06ng748f6DfEEoGjb84AZEujo9JwHZJoCNhB5p0Lyjkd/OF6OhVlG5d2tFzoKgMpXbQImmYSpkhrhFXtspPFGw4aVnjf97AApar0kWKj1TkZk5WuqwUZqOplbTp7IU+eADmeJfNn/85s6wUzIHrzmBXzVDQkjFzRdZJWdAc+wj:+wTTcbX662nrfaJhv7hLMgOTLAqU8gbWDUDRzYFBIr4=",
    'authority': "www.coursehero.com",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "max-age=0",
    'referer': "https://www.coursehero.com/tutors/homework-help/",
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': "document",
    'sec-fetch-mode': "navigate",
    'sec-fetch-site': "same-origin",
    'sec-fetch-user': "?1",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(len(response.text))