import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("my_database.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "title":
            query_for_project(*args)

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)


def query_for_project(title):
    query = """SELECT description, max_grade, title FROM Projects WHERE title =?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    try: 
        print row
        print """\
        Description: %s  
        Max Grade: %r
        Title: %s""" % (row[0], row[1], row[2])
        #in try-except blocks, you want to put in the error that you want to catch, like so:
    except TypeError: 
        print "No row here."

    CONN.close()

if __name__ == "__main__":
    main()
