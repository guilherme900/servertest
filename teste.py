
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
        iduser INT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (iduser)
        );
""")
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS images(
        id  INT NOT NULL AUTO_INCREMENT,
        idproduto INT NOT NULL,
        image BLOB NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (idproduto
        );
""") 
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS ordems(
        id  INT NOT NULL AUTO_INCREMENT,
        idproduto INT NOT NULL,
        iduser INT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (idproduto),
        FOREIGN KEY (iduser)
        );
""")

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)