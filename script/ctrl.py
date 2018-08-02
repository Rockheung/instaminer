import os

# SWAP PART
# If swapping(query = 'someone', instagram_id = 00000000), SWAP MODE
# If swapping(query_rollback = 'someone'), GO BACK TO rh_ass and STANBY MODE
def swapping(db_path = os.path.join(os.getenv('HOME'), 'Pictures/4K Stogram/.stogram.sqlite'),
             query = 'rh_ass',
             instagram_id = 1270251951,
             query_rollback = 'rh_ass'):
    import sqlite3, os

    db = sqlite3.connect(db_path)
    c = db.cursor()

    c.execute('UPDATE subscriptions SET instagram_id = ? WHERE query = ?', (instagram_id, query_rollback, ))
    c.execute('UPDATE subscriptions SET query = ? WHERE query = ?', (query, query_rollback, ))

    db.commit()
    db.close()

    return query

# AND RESTART 4KSTORGRAM
def restart_4kstogram(db_path = os.path.join(os.getenv('HOME'), 'Pictures/4K Stogram/.stogram.sqlite'),
                      query = 'rh_ass'):
    from subprocess import Popen, call, check_output, CalledProcessError
    from time import sleep
    import os, sqlite3

    for i in range(6):
        try:
            pid_o = check_output(['pidof', '4kstogram-bin'])
            call(['kill','-9',pid_o[:-1]])
            sleep(5)

        except CalledProcessError:
            print('No 4kstogram is running')
            break

    exe = check_output(['which', '4kstogram'])
    print('Start 4kstogram where is {}'.format(exe))

    while (True):

        try:
            Popen(['bash', exe[:-1]])
            sleep(5)
            pid_n = check_output(['pidof', '4kstogram-bin'])
            print('got new pid = {}'.format(pid_n))
            break

        except CalledProcessError:
            print('No 4kstogram is running')

    ready = 0

    while (ready == 0):

        print('Checkout if 4K Stogram is ready')
        sleep(5)
        db = sqlite3.connect(db_path)
        c = db.cursor()

        c.execute('SELECT finished FROM subscriptions WHERE query = ?', (query, ))
        ready = c.fetchone()[0]

        db.commit()
        db.close()

    return 0



