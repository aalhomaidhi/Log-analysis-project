#!/usr/bin/env python3
import psycopg2

# database name that given from Udacity :)
DBNAME = "news"



# Connection fancution that Connects to the database and runs the query 
# then returns the results to the function to Continu and print the result
def conn(query):
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  results = c.fetchall()
  db.close()
  return results



# this function contain a query that answer What are the most popular three articles of all time
# and passed to conn fun and print result
def popular_articles():

  # According to PEP 8 (Maximum Line Length), a line should never be longer than 79 characters
  # so the query should be like:
  popular_articles_query =  """
                      
                      SELECT articles.title, COUNT(*) AS view
                      FROM articles
                      JOIN log
                      ON log.path LIKE CONCAT('/article/%', articles.slug)
                      GROUP BY articles.title
                      ORDER BY view DESC
                      LIMIT 3;

                           """
  
  popular_articles_result = conn(popular_articles_query)
  popular_articles_title = "What are the most popular three articles of all time?"
  
  print(popular_articles_title)
  print("-" * 60)

  for i in popular_articles_result:
    print(str(i[0])+" - "+str(i[1]))




# this function contain a query that answer Who are the most popular article authors of all time
# and passed to conn fun and print result
def popular_authors():
  
  # According to PEP 8 (Maximum Line Length), a line should never be longer than 79 characters
  # so the query should be like:
  popular_authors_query =  """
                    
                    SELECT authors.name, COUNT(*) AS view
                    FROM articles
                    JOIN authors
                    ON authors.id = articles.author
                    JOIN log
                    ON log.path LIKE CONCAT('/article/%', articles.slug)
                    GROUP BY authors.name
                    ORDER BY view DESC;

                           """

  popular_authors_result = conn(popular_authors_query)
  popular_authors_title = "Who are the most popular article authors of all time? "
  
  print(popular_authors_title)
  print("-" * 60)

  for i in popular_authors_result:
    print(str(i[0])+" - "+str(i[1]))




def error_day():
  
  # According to PEP 8 (Maximum Line Length), a line should never be longer than 79 characters
  # so the query should be like:

  # i use VIEWs to slove this question 
  error_day_query =  """

                    SELECT  to_char(error.day,'MON dd, yyyy'),  (errors * 100.0 / total) AS perc
                    FROM error, total
                    WHERE error.day = total.day and (errors * 100.0 / total) > 1
                    ORDER BY to_char desc

                    """

  error_day_result = conn(error_day_query)
  error_day_title = "days did more than 1% of requests lead to errors: "
  
  print(error_day_title)
  print("-" * 60)

  for i in error_day_result:
    print(str(i[0])+" - "+str('%.2f' % i[1])+" %")




# running the code and call the methods:
if __name__ == '__main__':

  popular_articles()
  print("\n")
  popular_authors()
  print("\n")
  error_day()