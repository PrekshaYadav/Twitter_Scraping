USE university_shortlisting;

SELECT  * from tweets;
SELECT  * from tweet_url;
SELECT  * from tweet_tags;
SELECT  * from user;
SELECT  * from university;
SELECT  * from course;

drop table tweets;
drop table tweet_url;
drop table tweet_tags;
drop table user;
drop table university;
drop table course;

delete from tweets;
delete from tweet_url;
delete from tweet_tags;
delete from user;
delete from university;
delete from course;



15 Questions (5 questions each team member)

1. Search universities that provide DS courses.
select * from University 
where course = "Data Science";

2. Search for the top 3 universities.
select * from University 
order by ranking asc limit 3

3. Search for the universities with fees less than 20000.
select * from University 
where fees < 20000;

4. Universities which does not requires GPA greater than 3.5
	select University_Id, University_name, Course, GPA, University_link from University 
	where GPA < 3.5;

5. A university which accepts a score less than 90.
 select University_Id, University_name, Course, TOEFL, University_link from University 
 where TOEFL < 90; 
 
 6. University accepting average educational profile.
select University_Id, University_name, GRE, TOEFL, GPA from University 
where gpa <3.5 && GRE<315 && TOEFL<95;

7. University name starting from ‘U’ and sorted by ranking.
Select University_name from University 
where University_name like 'U%' order by ranking asc;

8. University with lowest cost of living along with the best ranking.
Select University_name, min(ranking), min(cost_of_living) from University

9. University with low fees and good return of interest.
Select University_Id, University_name, fees, Average_salary from University 
order by fees asc, Average_salary desc;

10. Finding the latest tweets related to the university
select tweets.tweet_id, tweets.tweet_text, tweets.created_date,university.university_name 
from tweets left join university
on tweets.tweet_id = university.tweet_Id
where university.University_name = 'University of Arizona'
order by created_date desc;

11. Search for universities which rank between top 20-30.
select * from University
where ranking BETWEEN 20 and 30;

12. View the universities which has CGPA cutoff of 3.5 and above
select University_name, GPA from university 
where GPA >= 3.5;

13. View the universities which offer course of “Computer science and engineering”.
select University_name, course from University 
where course = 'Computer science and Engineering';

14. View the course which has requirements of IELTS>=7.0 band.
select university_name, course, IELTS from university 
where IELTS >= 7;

15. View the twitter username for the tweets related to Princeton University.
select tweeter_handle from tweets left join university
on tweets.tweet_Id = university.tweet_Id
where university.University_name = 'Princeton University';

------------------------------------------------------------------------------------------------------
Assignment questions

1. What user posted this tweet?
select tweets.tweeter_handle
from tweets left join tweet_url 
on tweets.Tweet_Id = tweet_url.tweet_Id 
where tweet_url.url = 'https://twitter.com/Uni_Shortlistin/status/1590597710973140993';

2. When did the user post this tweet?
select tweets.created_date 
from tweets left join tweet_url 
on tweets.Tweet_Id = tweet_url.tweet_Id 
where tweet_url.url = 'https://twitter.com/Uni_Shortlistin/status/1590597710973140993';

3. What tweets have this user posted in the past 24 hours?
select * from tweets 
where tweeter_handle = 'Uni_Shortlistin' && created_date > '2022-11-10 05:54:19';

4.How many tweets have this user posted in the past 24 hours?
select count(tweet_id) from tweets 
where tweeter_handle = 'Uni_Shortlistin' && created_date > '2022-11-10 05:54:19';

5. When did this user join Twitter?
select Account_created_on from user 
where tweeter_handle = 'Uni_Shortlistin';

6. What keywords/ hashtags are popular?
select hash_tag, count(hash_tag) as frequency 
from tweets 
group by hash_tag 
order by count(hash_tag) desc;






 

