import sqlite3, os
import codecs
import sys

db_path = os.path.join(os.getcwd(), sys.argv[1])
print(db_path)
me = 'heung.rocks'


def db_subscriptions_fake_adder(id,
                                query,
                                finished,
                                instagram_id,
                                attributes,
                                db_path = db_path,
                                query_original = me):

    db_4Kstogram = sqlite3.connect(db_path)
    c = db_4Kstogram.cursor()

    c.execute('CREATE TEMPORARY TABLE tmp AS SELECT * FROM subscriptions WHERE query = ?', (query_original,))

    c.execute('UPDATE tmp SET id = ?', (id,))
    c.execute('UPDATE tmp SET query = ?', (query,))
    c.execute('UPDATE tmp SET finished = ?', (finished,))
    c.execute('UPDATE tmp SET instagram_id = ?', (instagram_id,))
    c.execute('UPDATE tmp SET attributes = ?', (attributes, ))

    c.execute('INSERT INTO subscriptions SELECT * FROM tmp')
    c.execute('DROP TABLE tmp')

    db_4Kstogram.commit()

    db_4Kstogram.close()

if __name__ == '__main__':
    db_subscriptions_fake_adder(id= 000000000,
                                query= 'jeongjiweon275',
                                finished= 0,
                                instagram_id= 8200567920,
                                attributes= '{"visualIndex":"_BASE64_LTI="}'
)
#
# with open('sql.bin', 'w') as f:
#     f.write(c.fetchone()[0])
# blob = c.fetchone()[0]

# print(c.fetchone()[0].decode('utf-8'))
#
def id_gen():
    pass

def query_gen():
    pass

def date_addd_gen():
    pass

def instagram_id_gen(id = 'jh_kim_honey'):
    pass
