from flask import Flask
import sqlite3

app = Flask(__name__)

def get_billet(id_billets):
    conn = sqlite3.connect("billets.db")
    cur = conn.cursor()

    cur.execute("""
    SELECT nom, numero, utilise
    FROM billets
    WHERE id_billets = ?
    """, (id_billets,)
    )

    results = cur.fetchone()
    conn.close()

    return results

@app.route("/billets/str:<id_billets>")

def billet(id_billets):
    data = get_billet(id_billets)
    if not data :
       return "Billet inexistant"
    
    nom, numero, utilise = data

    if utilise == 'OUI':
        return "Billet utilise"
    
    else :
        conn = sqlite3.connect('billets.db')
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE billets
            SET utilise = 'OUI'
            WHERE id_billets = ?
        """, (id_billets,)
        )

        conn.commit()
        conn.close()

        return f"""
        <h2>Billet Valide</h2>
        <p>ID : {id_billets}</p>
        <p>Nom : {nom}</p>
        <p>Tel : {numero}</p>
    """
    