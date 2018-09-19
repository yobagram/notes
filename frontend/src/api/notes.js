import { HTTP } from './common'

export const Note = {
  create (config) {
    return HTTP.post('/notes/', config).then(response => {
      return response.data
    })
  },
  read (note) {
    return HTTP.post(`/mark_read?id=${note.id}`)
  },
  list (lastId) {
    console.log('ниже lastId функции list:')
    console.log(lastId)
    return HTTP.get('/get_messages?last_id=' + String(lastId)).then(response => {
      console.log('ниже data функции list:')
      console.log(response.data)
      return response.data
    })
  }
}
