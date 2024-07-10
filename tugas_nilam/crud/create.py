import mysql.connector

def create_record(nis, nama, kelas):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sekolah"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO siswa (nis, nama, kelas) VALUES ( %s, %s, %s)"
    val = (nis, nama, kelas)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()