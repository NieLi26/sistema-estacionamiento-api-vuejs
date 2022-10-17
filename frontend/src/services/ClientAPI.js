import API from "./API";

export default {
    getClients() {
        return API.get('/clients/')
    },
    getClient(pk) {
        return API.get(`/clients/${pk}/`)
    },
    createClient(data) {
        return API.post('/clients/', data)
    },
    updateClient(pk, data) {
        return API.patch(`/clients/${pk}/`, data)
    },
    deleteClient(pk) {
        return API.delete(`/clients/${pk}/`)
    },
}