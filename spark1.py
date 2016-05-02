from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("Dota2")
sc = SparkContext(conf=conf)


sqlContext = SQLContext(sc)
df = sqlContext.read.json("/user/cloudera/my_match_history.json")
df.printSchema()


sqlContext.registerDataFrameAsTable(df, "my_full_table")

# df2 = sqlContext.sql("SELECT first(reslt.players.accont_id) as player , reslt.players.hero_id as herp_played , AVG(reslt.players.kills) as kills from my_full_table GROUP BY reslt.players.hero_id")

df3 = sqlContext.sql("SELECT reslt.players.accont_id as player , first(reslt.players.hero_id) as herp_played , AVG(reslt.players.kills) as kills from my_full_table where reslt.players.hero_id = 28 GROUP BY reslt.players.hero_id , reslt.players.accont_id ")


df3.show()
