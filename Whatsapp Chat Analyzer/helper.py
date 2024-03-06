from urlextract import URLExtract
import pandas as pd
from collections import Counter
import emoji
from wordcloud import WordCloud

# Initialize URL extractor
extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    # Concatenate all messages into a single string
    all_messages = ' '.join(df['message'])

    # Count words
    words = all_messages.split()

    # Fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # Fetch number of links
    links = extract.find_urls(all_messages)

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    user_counts = df['user'].value_counts().head()
    user_percentages = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})
    return user_counts, user_percentages

def create_wordcloud(selected_user, df):
    # Read stop words
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = set(f.read().splitlines())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Remove media messages and stop words
    filtered_messages = df.loc[df['message'] != '<Media omitted>\n', 'message'].str.lower().apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

    # Generate word cloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(' '.join(filtered_messages))

    return df_wc

def most_common_words(selected_user, df):
    # Read stop words
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = set(f.read().splitlines())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Remove media messages and stop words, then count words
    words = [word for message in df.loc[df['message'] != '<Media omitted>\n', 'message'].str.lower() for word in message.split() if word not in stop_words]
    most_common_df = pd.DataFrame(Counter(words).most_common(20))

    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = [c for message in df['message'] for c in message if emoji.is_emoji(c)]
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    timeline['time'] = timeline['month'] + ' ' + timeline['year'].astype(str)
    
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline 

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()
