import sqlite3

def ajouter_billet(id, nom, tel):
    conn = sqlite3.connect('billets.db')
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO billets (id_billets, nom, numero, utilise)
        VALUES (?, ?, ?, 'NON')
    """, (id, nom, tel)
    )

    conn.commit()
    conn.close()


ajouter_billet('VAS_001', 'Jao', '0329564811')