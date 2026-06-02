const KEY = 'lan-example-notes';

export function loadNotes() {
  try {
    return JSON.parse(localStorage.getItem(KEY) || '[]');
  } catch {
    return [];
  }
}

export function saveNote(note) {
  const notes = loadNotes();
  const saved = { id: crypto.randomUUID(), ...note };
  notes.push(saved);
  localStorage.setItem(KEY, JSON.stringify(notes));
  return saved;
}
