import sqlite3, os
import codecs
import sys


def get_pk(db_path, query):
    import sqlite3, os
    import sys

    try:
        db_path = os.path.join(os.getcwd(), db_path)
    except IndexError:
        db_path = os.path.join(os.getcwd(), '.stogram.sqlite')

    try:
        query = query
    except IndexError:
        query = 'heung.rocks'

    db_4Kstogram = sqlite3.connect(db_path)
    c = db_4Kstogram.cursor()

    c.execute('SELECT id FROM subscriptions WHERE query = ?', (query,))
    blob = c.fetchone()

    db_4Kstogram.commit()
    db_4Kstogram.close()

    return blob[0]

if __name__ == '__main__':
    blob = get_pk(db_path = sys.argv[1],
                  query = sys.argv[2])
    with open('{}.bin_id'.format(sys.argv[2]), 'wb') as bf:
        bf.write(blob)
