import API from "./API";

export default {
    getClients() {
        return API.get('/clients/')
    },
    getClientsPaginator(page_number) {
        return API.get(`/clients-pagination/?page=${page_number}`)
    },
    getClient(pk) {
        return API.get(`/clients/${pk}/`)
    },
    createClient(data) {
        return API.post('/clients/', data)
    },
    updateClient(pk, data) {
        return API.put(`/clients/${pk}/`, data)
    },
    deleteClient(pk) {
        return API.delete(`/clients/${pk}/`)
    },
}