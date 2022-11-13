import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Sh_reyasi03")
mycursor = mydb.cursor()

mycursor.execute("Use university_shortlisting")

#Create table commands
mycursor.execute("Create Table Tweets(Tweet_Id bigint NOT NULL, Tweeter_handle VARCHAR(2555), tweet_text VARCHAR(2555), created_date DateTime, hash_tag VARCHAR(250), PRIMARY KEY (Tweet_Id))")
mycursor.execute("Create Table User(Tweeter_handle Varchar(2555), Name VARCHAR(2555), profile_image_url VARCHAR(2555), Followers_count int, Account_created_on DateTime)")
mycursor.execute("Create Table Tweet_Tags(Tag_Id int NOT NULL AUTO_INCREMENT, Tag VARCHAR(2555), PRIMARY KEY(Tag_Id))")
mycursor.execute("Create Table Tweet_URL(Tweet_Id bigint NOT NULL, URL VARCHAR(2555), FOREIGN KEY(Tweet_Id) REFERENCES Tweets(tweet_Id))")
mycursor.execute("Create Table University(Tweet_Id bigint NOT NULL, University_Id int NOT NULL AUTO_INCREMENT, University_name VARCHAR (2555), Ranking int, Course VARCHAR(2555), GRE int, TOEFL int,IELTS int, Fees int, GPA float, Cost_of_living int, Acceptance_rate VARCHAR (2555), Average_salary int, University_link VARCHAR(2555), PRIMARY KEY(University_Id), FOREIGN KEY(Tweet_Id) REFERENCES Tweets(tweet_Id))")
mycursor.execute("Create Table Course(Course_Id int NOT NULL AUTO_INCREMENT, Course_name VARCHAR (2555), Credits int, PRIMARY KEY(Course_Id))")
