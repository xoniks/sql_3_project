import sqlite3

conn = sqlite3.connect('wage_payment.db')
c = conn.cursor()


c.execute(
    '''
        CREATE TABLE IF NOT EXISTS employees(
            id integer primary key,
            name text,
            rate real
    )'''
)

c.execute(
    '''
        CREATE TABLE IF NOT EXISTS wages (
            id integer primary key,
            employee_id integer,
            date Date,
            hours_worked real,
            amount_paid real,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
            )'''
)

conn.commit()
conn.close()