let selectedNoteId = null;

async function display_notes() {
    const response = await fetch("/get_notes");
    const data = await response.json();
    const notesContainer = document.querySelector("#notes-container");
    notesContainer.innerHTML = "";

    data["notes"].forEach(note => {
        const button = document.createElement("button");
        button.textContent = note["name_page"];
        button.onclick = function() { select_note(note); };
        notesContainer.appendChild(button);
        notesContainer.appendChild(document.createElement("br"));
    });
}

function select_note(note) {
    selectedNoteId = note["id"];
    document.querySelector("#note-title").value = note["name_page"];
    document.querySelector("#note-content").value = note["page_content"];
}

function create_note() {
    selectedNoteId = null;
    document.querySelector("#note-title").value = "";
    document.querySelector("#note-content").value = "";
    document.querySelector("#note-title").focus();
}

async function save_note() {
    const title = document.querySelector("#note-title").value;
    const content = document.querySelector("#note-content").value;

    if (selectedNoteId === null) {
        await fetch("/create_note", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({"name_page": title, "page_content": content})});
    } else {
        await fetch("/update_note", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({"note_id": selectedNoteId, "name_page": title, "page_content": content})});
    }

    location.reload();
}

async function delete_note() {
    if (selectedNoteId === null) return;

    await fetch("/delete_note", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({"note_id": selectedNoteId})});

    location.reload();
}

display_notes();