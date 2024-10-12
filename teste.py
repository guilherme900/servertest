
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase"
)



mycursor = mydb.cursor()

mycursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        email VARCHAR (30) NOT NULL,
        vendedor ENUM('V','C') DEFAULT 'C',
        cpf VARCHAR (66) NOT NULL,
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
        product INT NOT NULL,
        image BLOB NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (product) REFERENCES products(id)
        );
""") 
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS ordems(
        id INT NOT NULL AUTO_INCREMENT,
        product INT NOT NULL,
        user INT NOT NULL,
        statos ENUM('A','T','E') DEFAULT 'A'
        date DATETIME NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (product) REFERENCES products(id),
        FOREIGN KEY (user) REFERENCES users(id)
        );
""")

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)