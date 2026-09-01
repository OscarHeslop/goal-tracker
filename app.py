from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "storage/notes.db"


def create_pages_db():

    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_page TEXT NOT NULL,
            page_content TEXT
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():

    conn = sqlite3.connect(DATABASE)

    notes = conn.execute("""
        SELECT id, name_page, page_content
        FROM notes
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return render_template("index.html", notes=notes)


@app.route("/create_note", methods=["POST"])
def create_note():

    name_page = request.form["name_page"]
    page_content = request.form["page_content"]

    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        INSERT INTO notes (name_page, page_content)
        VALUES (?, ?)
    """, (name_page, page_content))

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/update_note", methods=["POST"])
def update_note():

    note_id = request.form["note_id"]
    name_page = request.form["name_page"]
    page_content = request.form["page_content"]

    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        UPDATE notes
        SET name_page = ?, page_content = ?
        WHERE id = ?
    """, (name_page, page_content, note_id))

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":

    create_pages_db()

    app.run(debug=True)

