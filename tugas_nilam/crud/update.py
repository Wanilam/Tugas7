
import mysql.connector

def update_record(nis,  nama, kelas ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sekolah"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE siswa SET nis = %s, nama = %s, kelas = %s WHERE id = %s"
        val = (nis, nama, kelas, nis)
        print("Executing SQL:", sql % val)  
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()


