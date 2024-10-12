
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase"
)



mycursor = mydb.cursor()

mycursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        email VARCHAR (30) NOT NULL,
        vendedor ENUM('V','C') DEFAULT 'C',
        password VARCHAR (66) NOT NULL,
        PRIMARY KEY (id)
        );
""")
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
        id  INT NOT NULL AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        quantity INT NOT NULL,
        valor INT NOT NULL,
        user INT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (user) REFERENCES users(id)
        );
""")
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS images(
        id  INT NOT NULL AUTO_INCREMENT,
        produto INT NOT NULL,
        image BLOB NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (produto) REFERENCES users(products),
        );
""") 
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS ordems(
        id  INT NOT NULL AUTO_INCREMENT,
        produto INT NOT NULL,
        user INT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (produto) REFERENCES users(products),
        FOREIGN KEY (user) REFERENCES users(id)
        );
""")

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)