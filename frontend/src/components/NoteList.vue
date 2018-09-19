<template lang="pug">
  #app
    .card(v-for="note in notes" :key="note.id")
      .card-header
        button.btn.btn-success.pull-right(@click="readNote(note)") {{"Прочитано"}}
        .card-title {{note.created_at}}
        .card-subtitle
      .card-body {{note.text}}
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'note-list',
  computed: mapGetters(['notes']),
  methods: {
    readNote (note) {
      // Вызываем действие `readNote` из нашего хранилища, которое
      // попытается удалить заметку из нашех базы данных, отправив запрос к API
      console.log('FFFFFFFFFFFFFFF')
      this.$store.dispatch('readNote', note)
    },
    update () {
      console.log('in update')
      var v = this
      // this.lastId = 10
      this.intervalid1 = setInterval(function () {
        console.log('GET API')
        v.$store.dispatch('addNotes')
      }, 10000)
    }
  },
  mounted () {
    console.log('in mounted')
    this.update()
  },
  beforeMount () {
    // Перед тем как загрузить страницу, нам нужно получить список всех
    // имеющихся заметок. Для этого мы вызываем действие `getNotes` из
    // нашего хранилища
    console.log('in beforeMount')
    this.$store.dispatch('getNotes')
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
