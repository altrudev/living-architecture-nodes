import { saveNote, loadNotes } from './storage.js';

export function addNote(text) {
  if (!text || !text.trim()) {
    throw new Error('Note text is required');
  }
  return saveNote({ text: text.trim(), createdAt: new Date().toISOString() });
}

export function listNotes() {
  return loadNotes();
}
