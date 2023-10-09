def matsuri_tweet(param):
    import tweepy
    import requests
    import random
    import os

    sheet_id = '1Po7srijCSNCjDvFhrQ-C35lpwF5wppReXW8x655zc1o'
    sheet_name = 'matsuri_talk'
    app_key = os.environ.get('google_sheet_api_key', 'ENV_ERR')
    url = 'https://sheets.googleapis.com/v4/spreadsheets/' + sheet_id + '/values/' + sheet_name + '?key=' + app_key

    response = requests.get(url)
    json = response.json()
    if json['values'] is None:
        print(response.json())
        exit()

    values = response.json()['values']
    start_row = 2
    rand_index = random.randint(start_row, len(values) - 1)
    current_data = values[rand_index]

    if len(current_data) < 4:
        print('No data')
        print(current_data)
        exit()

    tweet_text = current_data[1]
    tweet_text += '\n出典【' + current_data[2] + '】' + current_data[3]
    print(tweet_text)

    c_key = os.environ.get("matsuri_x_consumer_key", "ENV_ERR")
    c_secret = os.environ.get("matsuri_x_consumer_secret", "ENV_ERR")
    a_token = os.environ.get("matsuri_x_access_token", "ENV_ERR")
    a_token_secret = os.environ.get("matsuri_x_access_token_secret", "ENV_ERR")

    client = tweepy.Client(consumer_key=c_key, consumer_secret=c_secret,
                           access_token=a_token, access_token_secret=a_token_secret)
    client.create_tweet(text=tweet_text)

    return 'ok'
