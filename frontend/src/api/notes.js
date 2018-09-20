import { HTTP } from './common'

export const Note = {
  read (note) {
    return HTTP.post(`/mark_read?id=${note.id}`)
  },
  list (lastId) {
    return HTTP.get('/get_messages?last_id=' + String(lastId)).then(response => {
      return response.data
    })
  }
}
