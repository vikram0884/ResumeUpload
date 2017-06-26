from getpass import getpass
import MySQLdb, os

class Credentials(object):
    """
    Needed to establish database connection
    """
    def __init__(self, host=None, user=None, password=None, database=None):
        """
        Sets the credentials which will be used for database connection
        """
        self.host = raw_input("Enter the DB server(Press Enter if its localhost):") if not host else host
        self.host = host if host else "localhost"
        self.user = raw_input("Enter the USER name:") if not user else user
        pass1, pass2 = range(2)
        while pass1 != pass2:
            pass1 = getpass("Password:")
            pass2 = getpass("Password(Enter Again):")
            if pass1 != pass2:
                print "Password don't match.. enter again"
            else:
                self.password = pass1
        self.database = raw_input("Enter dbname:") if not database else database

    def get_credentials(self):
        """
        Gets credentails to use for establishing db connection
        """
        return ( self.host, self.user, self.password, self.database )

    def get_config_info(self):
        """
        Used to create cnf file
        """
        return "[client]\nhost=%s\nuser=%s\npassword=%s\ndatabase=%s\n"%self.get_credentials()


class DBConnector(object):
    """
    DB handle to execute queries for the configured Credentials object
    """
    def __init__(self, credentials=None):
        """
        Creates connection and cursor for db operations
        """
        if not isinstance(credentials, Credentials):
            credentials = Credentials()
        self.dbcon  = MySQLdb.connect(*credentials.get_credentials())
        self.set_cursor()

    def execute(self, query):
        """
        Execute the query
        """
        return self.cursor.execute(query)

    def set_cursor(self):
        """
        gets cursor to execute queries
        """
        self.cursor = self.dbcon.cursor()

    def commit(self):
        """
        Commits the db changes so far done to the database
        """
        self.dbcon.commit()

class CreateDatabase(object):
    """
    Creates database which will be used by the app
    """
    def __init__(self, dbcon=None, user_credential=None):
        """
        Uses dbcon to create database for the app
        """
        if not isinstance(dbcon, DBConnector):
            dbcon = DBConnector()
        dbname = raw_input("Enter the db name to be created for the app to use:") if not user_credential.database else user_credential.database
        query = "CREATE DATABASE %(dbname)s"%locals()
        dbcon.execute(query)
        dbcon.commit()

class SetDBUser(object):
    """
    Creates database which will be used by the app
    """
    def __init__(self, dbcon=None, user_credential=None, user_permissions=["SELECT", "INSERT", "UPDATE", "CREATE","ALTER", "REFERENCES","INDEX",]):
        """
        Uses dbcon to create database for the app
        """
        if not isinstance(dbcon, DBConnector):
            dbcon = DBConnector()
        if not isinstance(user_credential, Credentials):
            user_credential = Credentials()
        permissions = ",".join(user_permissions)
        host, user, password, database = user_credential.get_credentials()
        #self.cnf_config = host, user, password, database
        cquery = "CREATE USER '%(user)s'@'%(host)s' IDENTIFIED BY '%(password)s'"%locals()
        gquery = "GRANT %(permissions)s ON %(database)s.* TO '%(user)s'@'%(host)s'"%locals()
        dbcon.execute(cquery)
        dbcon.execute(gquery)
        dbcon.execute("FLUSH PRIVILEGES")
        dbcon.commit()

class SetDBConfigFile(object):
    """
    Creates database config file for django to use for database authentication
    """
    def __init__(self, filename, credentials):
        """
        Created cnf file for the app
        """
        os.remove(filename)
        self.file = open(filename, "w+")
        if not isinstance(credentials, Credentials):
            credentials = Credentials()
        self.file.write(credentials.get_config_info())
        self.file.flush()
        self.file.close()
        os.system("chmod 644 "+filename)

class DJangoTasks(object):
    """
    Used for making db preparation and for starting dev server
    """
    def __init__(self):
        """
        Runs the django prep for the app
        """
        os.system("python manage.py createsuperuser")
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")
        os.system("python manage.py runserver")

class Tasks(object):
    """
    Sets the environment for the app to start successfully
    """
    #need to add a class to check and install dependencies based on requirements.txt
    tasks = { 
                # Can change 1 in the tuple to 0 if the task is not needed, still its not meaningful to task 1 as its needed to connect to DB
                1 : (1, 'Root DB credentials', Credentials, []), 
                2 : (1, 'DB User to create  ', Credentials, []),
                3 : (1, 'DB Connection creation', DBConnector, [1,]),
                4 : (1, 'db creation for the app', CreateDatabase, [3, 2]),
                5 : (1, 'DB User creation & permissions', SetDBUser, [3, 2]),
                6 : (1, 'DB Config file creation       ', SetDBConfigFile, ['conn.cnf', 2]),
                7 : (1, 'DJango task', DJangoTasks, []),
            }
    def __init__(self):
        """
        Initiates the process for setting the environement
        """
        index, obj = {}, {}
        for no in Tasks.tasks:
            todo, desc, cls, args = Tasks.tasks.get(no, (None, None, None, None) )
            if not todo:
                continue
            print "Task %s : %s"%(no, desc,)
            index[no] = cls
            if not args:
                obj[no] = index[no]()
            else:
                arguments = ""
                for arg in args:
                    if isinstance(arg, str):
                        arguments+="'%(arg)s',"%locals()
                    else:
                        arguments+="obj[%(arg)s],"%locals()
                arguments = arguments[:-1]
                obj[no] = index[no](*eval(arguments)) if arguments.count(",") > 0 else index[no](eval(arguments))
if __name__ == '__main__':
    task = Tasks()







