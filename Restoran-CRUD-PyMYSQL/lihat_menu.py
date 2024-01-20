import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_restoran',
)

try:
    with connection.cursor () as cursor:
        sql = "SELECT kd_menu, menu, jenis, harga, status, foto, kd_kategori 'desc' FROM tb_menu"
        try:
            cursor.execute (sql)
            result = cursor.fetchall ()
            print ("+-------------------------------------------------------------------------------+")
            print ("Kode Menu\tMenu\t\tJenis\tHarga\tStatus\tFoto\tKode Kategori")
            print ("+-------------------------------------------------------------------------------+")
            for row in result:
                # print (str (row[0]) + "\t" + row[1]+ "\t" + row[2])
                print (str (row[0]) + "\t\t" + row [1] + "\t" + row [2]+ "\t" + row [3]+ "\t" + row[4] + "\t" + row [5]+ "\t" + row [6])
        
        except:
            print ("Oops! Something wrong")
    connection.commit ()
finally:
    connection.close ()