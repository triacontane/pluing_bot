def tweet(param):
    import tweepy
    import requests
    import random
    import os

    sheet_id = '1BnTyJr3Z1WoW4FMKtvKaICl4SQ5ehL5RxTDSV81oVQc'
    sheet_name = 'プラグイン一覧(MZ)'
    app_key = os.environ.get('google_sheet_api_key', 'ENV_ERR')
    url = 'https://sheets.googleapis.com/v4/spreadsheets/' + sheet_id + '/values/' + sheet_name + '?key=' + app_key

    response = requests.get(url)
    values = response.json()['values']
    start_row = 4
    rand_index = random.randint(start_row, len(values) - 1)
    current_data = values[rand_index]

    if len(current_data) < 5:
        print('No data')
        exit()

    plugin_full_url = current_data[4]
    plugin_file_name = plugin_full_url.split('/')[-1]
    git_hub_url = 'https://github.com/triacontane/RPGMakerMV/blob/mz_master/' + plugin_file_name

    tweet_text = '【' + current_data[1] + '】'
    tweet_text += '\n' + current_data[3]
    tweet_text += '\n' + git_hub_url
    print(tweet_text)

    c_key = os.environ.get("consumer_key", "ENV_ERR")
    c_secret = os.environ.get("consumer_secret", "ENV_ERR")
    a_token = os.environ.get("access_token", "ENV_ERR")
    a_token_secret = os.environ.get("access_token_secret", "ENV_ERR")

    client = tweepy.Client(consumer_key=c_key, consumer_secret=c_secret,
                           access_token=a_token, access_token_secret=a_token_secret)
    client.create_tweet(text=tweet_text)

    return 'ok'
