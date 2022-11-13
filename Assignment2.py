import tweepy #Library required for Twitter API
import csv
import pandas as pd
import os
import wget
import json
import pip
import mysql.connector


def line_to_dict(split_Line):
    # Assumes that the first ':' in a line
    # is always the key:value separator
    # print("Split Line ::::::::::::", split_Line)
    # print("Split Line1 ::::::::::::", type(split_Line))
    line_dict = {}
    for part in range(2, len(split_Line)):
        key, value = split_Line[part][0].split(":", maxsplit=1)
        line_dict[key] = value

    return line_dict

def convert(tweet_id) :

    f = open("data.txt", "r")
    content = f.read()
    splitcontent = content.splitlines()
    lines1 = []
    # Split each line by pipe
    lines = [line.split(' | ') for line in splitcontent]

    # Convert each line to dict
    # lines = [line_to_dict(lines) for l in lines]
    lines = line_to_dict(lines)

    university_val = (tweet_id, lines.get('University_name'), lines.get('Ranking'), lines.get('Course'), lines.get('GRE'), lines.get('TOEFL'), lines.get('IELTS'), lines.get('Fees'), lines.get('GPA'), lines.get('Cost_of_living'), lines.get('Acceptance_rate'), lines.get('Average_salary'), lines.get('University_link'))
    university_sql = "INSERT INTO university(Tweet_Id, University_name, Ranking, Course, GRE, TOEFL, IELTS, Fees, GPA, Cost_of_living, Acceptance_rate, Average_salary, University_link) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)"
    mycursor.execute(university_sql, university_val)

# connecting python to MySQL
mydb = mysql.connector.connect(host="localhost", user="root", password="Sh_reyasi03")
mycursor = mydb.cursor()
mycursor.execute("Use university_shortlisting")

package ='tweepy' #Just replace the package name with any package to install it.
pip.main(['install',package])

#API and access keys
consumer_key = "XE8CV9dui2y76WecW25l6mnzj"
consumer_secret = "Xfmuywuz85eeM4HP7Liz7Bd0yaH50nrZQNsMPNB4AmfetgYz7l"
access_key = "1101128446053298176-wMJTdtFEGbSqyVnwQtS25lUDDYyRlP"
access_secret = "XznIidNCMeAIk3PpUwTLYns0v2ZYlHHcKfZb6Kcc6Huwg"

#Creating an empty dataframe to store the information
tweets =pd.DataFrame(columns=["id","created_at","text","media_url","location"])


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

outtweets = [] #initialize master list to hold our ready tweets

#inserting values in user Table
user = api.get_user(screen_name="Uni_Shortlistin")
user_val = (user.screen_name, user.name, user.profile_image_url, user.followers_count, user.created_at)
user_sql = "INSERT INTO User(Tweeter_handle, name, profile_image_url, Followers_count, Account_created_on)VALUES (%s, %s, %s, %s, %s)"
mycursor.execute(user_sql, user_val)

#inserting values in course table
Course_sql = "INSERT INTO Course(Course_name, Credits) VALUES ('Data Science', '32')"
Course_sql1 = "INSERT INTO Course(Course_name, Credits) VALUES ('Analytics and Data Science', '32')"
Course_sql2 = "INSERT INTO Course(Course_name, Credits) VALUES ('Statistics - Data Science', '32')"
Course_sql3 = "INSERT INTO Course(Course_name, Credits) VALUES ('Computer Science', '32')"
Course_sql4 = "INSERT INTO Course(Course_name, Credits) VALUES ('Computer Science and Engineering', '32')"
Course_sql5 = "INSERT INTO Course(Course_name, Credits) VALUES ('Computer and Cognitive Science', '32')"
Course_sql6 = "INSERT INTO Course(Course_name, Credits) VALUES ('Linguistics and Computer Science', '32')"
Course_sql7 = "INSERT INTO Course(Course_name, Credits) VALUES ('Computer Science - Systems', '32')"
Course_sql8 = "INSERT INTO Course(Course_name, Credits) VALUES ('Information Systems', '32')"
mycursor.execute(Course_sql)
mycursor.execute(Course_sql1)
mycursor.execute(Course_sql2)
mycursor.execute(Course_sql3)
mycursor.execute(Course_sql4)
mycursor.execute(Course_sql5)
mycursor.execute(Course_sql6)
mycursor.execute(Course_sql7)
mycursor.execute(Course_sql8)

#followers of the user
users = []
for follower in user.followers():
    users.append([follower.screen_name, follower.name, follower.profile_image_url, follower.description,
                  follower.followers_count, follower.following])
    user_val = (follower.screen_name, follower.name, follower.profile_image_url, follower.followers_count, follower.created_at)
    user_sql = "INSERT INTO User(Tweeter_handle, name, profile_image_url, Followers_count, Account_created_on)VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(user_sql, user_val)

with open('unitag.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #inserting values in tweet_tags table
        tweet_tags_sql = "INSERT INTO tweet_tags (Tag) VALUES (%s)"
        tweet_tags_val = (row[0])
        mycursor.execute(tweet_tags_sql, (tweet_tags_val,))


        for tweet in tweepy.Cursor(api.search_tweets,q=row[0],count=100, #The q variable holds the hashtag
                                   lang="en",tweet_mode='extended').items():

            media = tweet.entities.get('media', [])
            media = tweet.entities.get('media')

            #inserting values in tweet table
            tweet_val = (tweet.id, tweet.user.screen_name, tweet.full_text.encode("utf-8"), tweet.created_at, tweet_tags_val )
            tweet_sql = "INSERT INTO tweets (tweet_ID, tweeter_handle, tweet_text, created_date, hash_tag) VALUES ( %s, %s, %s, %s, %s)"
            # print(user_txt)
            tweet_txt = tweet.full_text
            user = api.get_user(screen_name="Uni_Shortlistin")
            mycursor.execute(tweet_sql, tweet_val)

            # creating url for each tweet
            username = tweet.user.screen_name
            tweet_id = tweet.id
            url_txt ="https://twitter.com/"+ tweet.user.screen_name +"/status/"+ str(tweet.id)

            #inserting values in tweet_url table
            tweet_url_sql = "INSERT INTO tweet_url (Tweet_ID, URL) VALUES (%s, %s)"
            tweet_url_val = (tweet.id, url_txt)


            f = open("data.txt", "w")
            f.write(tweet_txt)
            f.close()
            convert(tweet.id)
            mycursor.execute(tweet_url_sql, (tweet_url_val))
            mydb.commit()