from pyspark import pipelines as dp

@dp.table
def demo_table_dab():
    return spark.range(100)