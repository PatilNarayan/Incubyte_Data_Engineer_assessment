# importing necessary libraries
import psycopg2
#connecting postgres database for ceating new table
conn = psycopg2.connect(database = "hospital", user = "postgres", password = "psql", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

#query execute in database
cur.execute('''CREATE TABLE patients
      (Customer_Name VARCHAR(255) PRIMARY KEY NOT NULL,
      Customer_Id  VARCHAR(18) NOT NULL,
      Open_Date  Date  NOT NULL,
      Last_Consulted_Date  Date,
      Vaccination_Id CHAR(5),
      Dr_Name CHAR(255),
      State CHAR(5),
      Country CHAR(5),
      post INT,
      DOB Date,
      Is_Active CHAR(1));''')
print("Table created successfully")

#commit the connection
conn.commit()
#connection close
conn.close()
