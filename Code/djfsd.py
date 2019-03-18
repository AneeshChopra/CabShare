import sqlite3

def insert(R,N,P,G,De,Da,Pick):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO passengers VALUES (?,?,?,?,?,?,?,'')",(R,N,P,G,De,Da,Pick))
    conn.commit()
    conn.close()

def view(R):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM passengers WHERE Destination=(Select Destination From passengers WHERE regno=?) AND Dates=(Select Dates From passengers WHERE regno=?) AND Groupcode=''",(R,R))
    rows=cur.fetchall()
    conn.close()
    return rows

def search(R,N,P,G,De,Da,Pick,Rg):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM passengers where (Destination=(Select Destination From passengers WHERE regno=?) AND Dates=(Select Dates From passengers WHERE regno=?)) AND (name LIKE ? OR regno=? OR mobileno=? OR gender=?);",(Rg,Rg,N + '%',R,P,G))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(R):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM passengers WHERE regno=?;",(R,))
    conn.commit()
    conn.close()

def update_p(R,A,B,C):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    print(R,A,B,C)
    cur.execute("UPDATE passengers SET name=? , mobileno=?, gender=? WHERE regno=?;", (A,B,C,R))
    conn.commit()
    conn.close()

def update_t(R,A,B,C):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    print(R,A,B,C)
    cur.execute("UPDATE passengers SET Destination=? , Dates=?, pickup=? WHERE regno=?;", (A,B,C,R))
    conn.commit()
    conn.close()

def update(R,Da):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE passengers SET Dates=? WHERE regno=?;", (Da,R))
    conn.commit()
    conn.close()

def selected(R,Reg):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE passengers SET Groupcode=? WHERE regno=?;", (R, Reg))
    conn.commit()
    conn.close()

def later(Reg):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE passengers SET Groupcode='' WHERE Groupcode=?;", (Reg,))
    conn.commit()
    conn.close()


#selected("","17BCE2184")

#insert("17BCE2120","Aditya Ghai",9999335015,"Male","chennai airport","2018-11-1",16.3)
#print(view("chennai airport","2018-11-2",28.3))

def same_year(De,Da,Pi,R,Reg):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers where (Destination=(Select Destination From passengers WHERE regno=?) AND Dates=(Select Dates From passengers WHERE regno=?) ) AND (regno LIKE ?) AND (Groupcode = '' OR Groupcode=?);",(Reg,Reg,R+'%',Reg))
    row=cur.fetchall()
    conn.commit()
    conn.close()
    return row

def insert_car(A,B,C,D,E,F,G,H):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO cars VALUES (?,?,?,?,?,?,?,?)",(A,B,C,D,E,F,G,H))
    conn.commit()
    conn.close()


def insert_driver(A,B,C,D):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO driver VALUES (?,?,?,?)",(A,B,C,D))
    conn.commit()
    conn.close()

def view_selected(R):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers WHERE Groupcode=?;", (R,))
    row=cur.fetchall()
    conn.commit()
    conn.close()
    return row

def view_cars():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT carmodel,cartype,maxseat,ac,ppkm,carplate FROM cars WHERE Booked='No';" )
    row = cur.fetchall()
    conn.commit()
    conn.close()
    print(row)
    return row

def search_cars(A,B,C,D):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT carmodel,cartype,maxseat,ac,ppkm,carplate FROM cars WHERE cartype=? OR maxseat>=? OR ac=? OR ppkm<=?;",(A,B,C,D) )
    row = cur.fetchall()
    conn.commit()
    conn.close()
    print(row)
    return row

def book_car(A,B):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE passengers SET pickup=(SELECT min(pickup) FROM passengers where Groupcode=?) WHERE Groupcode=?",(B,B))
    cur.execute(
        "UPDATE passengers SET Groupcode=(SELECT carcode FROM cars where carplate=?) WHERE regno=?;",
        (A, B))
    cur.execute(
        "UPDATE cars SET Booked='Yes' WHERE carplate=?;",
        (A,))
    conn.commit()
    conn.close()


view_cars()

#insert_car("TN76MG6162","Toyota Innova","SUV",7,"Yes",12.0,"7AM6162","No")
#insert_driver("Aadish Mandal",6872600544,"TN76MG6162","7AM6162")

def get_information(A):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM driver WHERE cplate=?;",
        (A,))
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("SELECT * FROM cars ;")
row = cur.fetchall()
conn.commit()
conn.close()
print(row)
