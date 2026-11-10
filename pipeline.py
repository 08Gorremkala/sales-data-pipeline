# Bronze - Raw Data

data = [
    (1001, "Asha", "Hyderabad", 5000),
    (1002, "Ravi", "Chennai", 7000),
    (1003, "Priya", "Mumbai", 9000)
]

columns = [
    "Order_ID",
    "Customer_Name",
    "City",
    "Total_Amount"
]

bronze_df = spark.createDataFrame(data, columns)

display(bronze_df)