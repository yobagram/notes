import Vue from 'vue'
import Vuex from 'vuex'
import { Note } from '../api/notes'
import {
  READ_NOTE,
  SET_NOTES,
  ADD_NOTES
} from './mutation-types.js'

Vue.use(Vuex)

// Состояние
const state = {
  notes: [], // список заметок
  lastId: 0 // id последнего элемента
}

// Геттеры
const getters = {
  notes: state => state.notes, // получаем список заметок из состояния
  lastId: state => state.lastId // получаем lastId
}

// Мутации
const mutations = {
  // Убираем заметку из списка
  [READ_NOTE] (state, { id }) {
    state.notes = state.notes.filter(note => {
      return note.id !== id
    })
  },
  // Задаем список заметок
  [SET_NOTES] (state, { notes }) {
    state.lastId = notes[0]['id']
    state.notes = notes
  },
  // Добавляем в список заметок
  [ADD_NOTES] (state, { notes }) {
    state.lastId = notes[0]['id']
    state.notes.unshift(...notes)
    console.log('state.notes:')
    console.log(state.notes)
  }
}

// Действия
const actions = {
  readNote ({ commit }, note) {
    Note.read(note).then(response => {
      commit(READ_NOTE, note)
    })
  },
  getNotes ({ commit }) {
    state.lastId = 0
    Note.list(state.lastId).then(notes => {
      if (notes.length !== 0) {
        state.lastId = notes[0]['id']
        commit(SET_NOTES, { notes })
      }
    })
  },
  addNotes ({ commit }) {
    Note.list(state.lastId).then(notes => {
      if (notes.length !== 0) {
        console.log(notes)
        console.log('notes.length !== 0')
        state.lastId = notes[0]['id']
        console.log(state.lastId)
        commit(ADD_NOTES, { notes })
      }
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
