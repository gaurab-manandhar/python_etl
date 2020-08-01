from variables import Variable
import psycopg2


#Database credential
class DB_Connection():
  # Creating varaible object and setting values
  var_ob = Variable()
  cred = var_ob.db_get()
  connection=""
  cur=""

  #Function to open database connection
  def db_connect(self):
    self.connection = psycopg2.connect("host={} dbname={} user={}".format(self.cred[0], self.cred[1], self.cred[2]))
    self.cur = self.connection.cursor()
    return self.cur

  #Function to close database connection
  def db_close(self):
    try:
      self.cur.close()
      self.connection()
    except(Exception, psycopg2.Error) as error :
      print(error)
  #Function to check table exists
  def has_table(self,table_name):
    if self.connection:
      self.db_close()
      self.db_connect()
    else:
      self.db_connect()
    try:
      self.cur.execute("SELECT * FROM {}".format(table_name))
      self.db_close()
      return True
    except:
      return False

  #Function to reconized CRUD operation
  def crud_ops(self, query,value=""):
    if self.connection:#Check database connection
      self.db_close()
      self.db_connect()
    else:
      self.db_connect()

    ops_list = ["CREATE","UPDATE","DELETE"]
    if [crud for crud in ops_list if(crud in query)] : #Check SQL statement in  generate querry
      try:
        self.cur.execute(query)
        self.connection.commit()
        self.cur.close()
        return True
      except:
        print("Cannot perform CRUD Operation!!")
        return False

    elif "SELECT" in query:
      try:
        self.cur.execute(query)
        return self.curr.fetchall()
      except:
        print("Unable to select given table!!")
        return False
    elif "INSERT" in query:
      try:
        self.cur.executemany(query,value)
        self.connection.commit()
        self.cur.close()
        return True
      except(Exception, psycopg2.Error) as error:
        print(error)
        return False