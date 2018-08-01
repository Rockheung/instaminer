import os, sqlite3, sys

db_path = os.path.join(os.getcwd(), sys.argv[1])

if __name__ == '__main__':

    db_4Kstogram = sqlite3.connect(db_path)

    c = db_4Kstogram.cursor()
    c.execute('DELETE FROM subscriptions WHERE id = ?', (0,))

    db_4Kstogram.commit()

    db_4Kstogram.close()
