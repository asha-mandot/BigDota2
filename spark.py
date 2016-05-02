from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext


#defining the sql and conf objects for spark
#Note: these need not be defines if the code is run n databricks cluster, becuase they (SC and CONF) are defined by default
conf = SparkConf().setAppName("Dota2")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


#path should be changed where data resides.
#In our case we are using databricks sparks cluster.
#So pthis path is databricks tables  where in the data files are resided on aws S3 storage.
#registering the data as datafrmae
df = sqlContext.read.json("/FileStore/tables/3v7vab741462231829765/my_match_history.json")
df.printSchema()

#registering the data from datafram to table
sqlContext.registerDataFrameAsTable(df, "my_full_table")

#performing few ETL and Field profiling using the queries.
#Hero_summary and item_summar ETl and profiling
hero_summary = sqlContext.read.json("/FileStore/tables/wbn4nbby1461991735655/hero_summary.json")
sqlContext.registerDataFrameAsTable(hero_summary, "hero_summary")
hero_summary.printSchema()

item_summary = sqlContext.read.json("/FileStore/tables/vvzkk2qc1462214278912/item_summmary.json")
sqlContext.registerDataFrameAsTable(item_summary, "item_summary")
item_summary.printSchema()

#Query for Changing the data values - profiling
hero_profile = sqlContext.sql("UPDATE my_full_table SET my_full_table.reslt.players.hero_id = hero_summary.heroes.localized_name from hero_summary where my_full_table.reslt.players.hero_id = hero_summary.heroes.hero_id")
item0_profile = sqlContext.sql("UPDATE my_full_table SET my_full_table.reslt.players.item_0 = item_summary.items.localized_name from item_summary where my_full_table.reslt.players.item_0 = item_summary.items.id")
item1_profile = sqlContext.sql("UPDATE my_full_table SET my_full_table.reslt.players.item_1 = item_summary.items.localized_name from item_summary where my_full_table.reslt.players.item_1 = item_summary.items.id")
item2_profile = sqlContext.sql("UPDATE my_full_table SET my_full_table.reslt.players.item_2 = item_summary.items.localized_name from item_summary where my_full_table.reslt.players.item_2 = item_summary.items.id")
item3_profile = sqlContext.sql("UPDATE my_full_table SET my_full_table.reslt.players.item_3 = item_summary.items.localized_name from item_summary where my_full_table.reslt.players.item_3 = item_summary.items.id")
item4_profile = sqlContext.sql("UPDATE my_full_table SET my_full_table.reslt.players.item_4 = item_summary.items.localized_name from item_summary where my_full_table.reslt.players.item_4 = item_summary.items.id")
item5_profile = sqlContext.sql("UPDATE my_full_table SET my_full_table.reslt.players.item_5 = item_summary.items.localized_name from item_summary where my_full_table.reslt.players.item_5 = item_summary.items.id")



#####################################################
#Spark SQL - Analytics for players - kills , Deaths and Assits
#Analytics for the players average kills he makes in overall of all the matches played , this is visualized by respective player vs all professional players
#Same analyitcs is applied to for deaths and assists to be found out.
#note user will be just changing the files to deaths and assists in AVG() function to find them.
Query_one= sqlContext.sql("SELECT first(reslt.players.accont_id) as player , reslt.players.hero_id as hero_played , AVG(reslt.players.kills) as kills from my_full_table GROUP BY reslt.players.hero_id")
Query_one.show()
display(Query_one) # to visulaize in databricks with graphs- please use this


#Anlaytics for the players average kills  when played with specific hero  . This is visualized with respect to other professional players
#The hero name_has to be changed in query where clause hero_id = "" when user want s to check for other heroes he played.
Query_two= sqlContext.sql("SELECT reslt.players.accont_id as player , first(reslt.players.hero_id) as hero_played , AVG(reslt.players.kills) as kills from my_full_table where reslt.players.hero_id = 28 GROUP BY reslt.players.hero_id , reslt.players.accont_id ")
Query_two.show()
display(Query_two) # to visulaize in databricks with graphs- please use this
#####################################################





#####################################################
#Analytics for the players count of last hits the makes in overall of all the matches played , this is visualized by respective player vs all professional players
Query_three= sqlContext.sql("SELECT first(reslt.players.accont_id) as player , reslt.players.hero_id as hero_played , count(reslt.players.last_hits) as last_hits from my_full_table GROUP BY reslt.players.hero_id")
Query_three.show()
display(Query_three) # to visulaize in databricks with graphs- please use this


#Anlaytics for the players count of  last hits on creeps and heroes  when played with specific hero  . This is visualized with respect to other professional players
#The hero name_has to be changed in query where clause hero_id = "" when user want s to check for other heroes he played.
Query_four = sqlContext.sql("SELECT reslt.players.accont_id as player , first(reslt.players.hero_id) as hero_played , count(reslt.players.last_hits) as last_hits from my_full_table where reslt.players.hero_id = 28 GROUP BY reslt.players.hero_id , reslt.players.accont_id ")
Query_four.show()
display(Query_three) # to visulaize in databricks with graphs- please use this


#Analytics for the players average denies he makes in overall of all the matches played , this is visualized by respective player vs all professional players
Query_five= sqlContext.sql("SELECT first(reslt.players.accont_id) as player , reslt.players.hero_id as hero_played , count(reslt.players.denies) as denies from my_full_table GROUP BY reslt.players.hero_id")
Query_five.show()
display(Query_five) # to visulaize in databricks with graphs- please use this



#Anlaytics for the players average denies on creeps and heroes  when played with specific hero  . This is visualized with respect to other professional players
#The hero name_has to be changed in query where clause hero_id = "" when user want s to check for other heroes he played.
Query_six = sqlContext.sql("SELECT reslt.players.accont_id as player , first(reslt.players.hero_id) as hero_played , count(reslt.players.denies) as denies from my_full_table where reslt.players.hero_id = 28 GROUP BY reslt.players.hero_id , reslt.players.accont_id ")
Query_six.show()
display(Query_six) # to visulaize in databricks with graphs- please use this
#####################################################




#####################################################
#Hero healing and damage Analytics- comparing it to professional players


#Analytics for the players average healing he makes in overall of all the matches played , this is visualized by respective player vs all professional players
Query_7= sqlContext.sql("SELECT first(reslt.players.accont_id) as player , reslt.players.hero_id as hero_played , AVG(reslt.players.hero_healing) as hero_healing from my_full_table GROUP BY reslt.players.hero_id")
Query_7.show()
display(Query_7) # to visulaize in databricks with graphs- please use this



#Anlaytics for the players average denies on creeps and heroes  when played with specific hero  . This is visualized with respect to other professional players
#The hero name_has to be changed in query where clause hero_id = "" when user want s to check for other heroes he played.
Query_8 = sqlContext.sql("SELECT reslt.players.accont_id as player , first(reslt.players.hero_id) as hero_played , count(reslt.players.hero_healing) as hero_healing from my_full_table where reslt.players.hero_id = 28 GROUP BY reslt.players.hero_id , reslt.players.accont_id ")
Query_8.show()
display(Query_8) # to visulaize in databricks with graphs- please use this


#Analytics for the players average healing he makes in overall of all the matches played , this is visualized by respective player vs all professional players
Query_9= sqlContext.sql("SELECT first(reslt.players.accont_id) as player , reslt.players.hero_id as hero_played , AVG(reslt.players.hero_damage) as damage from my_full_table GROUP BY reslt.players.hero_id")
Query_9.show()
display(Query_9) # to visulaize in databricks with graphs- please use this



#Anlaytics for the players average damage on creeps and heroes  when played with specific hero  . This is visualized with respect to other professional players
#The hero name_has to be changed in query where clause hero_id = "" when user want s to check for other heroes he played.
Query_10 = sqlContext.sql("SELECT reslt.players.accont_id as player , first(reslt.players.hero_id) as hero_played , count(reslt.players.hero_damage) as damage from my_full_table where reslt.players.hero_id = 28 GROUP BY reslt.players.hero_id , reslt.players.accont_id ")
Query_10.show()
display(Query_10) # to visulaize in databricks with graphs- please use this

#####################################################








