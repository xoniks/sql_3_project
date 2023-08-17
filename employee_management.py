import sqlite3

def add_employee(name,rate):
    conn = sqlite3.connect('wage_payment.db')
    c = conn.cursor()

    c.execute('Insert Into employees (name, rate) Values (?,?)',(name, rate))

    conn.commit()
    conn.close()