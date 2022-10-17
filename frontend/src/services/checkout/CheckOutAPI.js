import API from "../API";

export default {
    // Estacionamientos
    // getLots() {
    //     return API.get('/lots/')
    // },
    // createLot(data) {
    //     return API.post('/lots/', data)
    // },
    // Reservas
    getCheckOut() {
        return API.get('/checkout/')
    },
    createPayment(data) {
        return API.post('/checkout/', data)
    },
    getReserve(pk) {
        return API.get(`/reserves/${pk}/`)
    },
    updateReserve(pk, data) {
        return API.patch(`/reserves/${pk}/`, data)
    },
    // createReserve(data) {
    //     return API.post('/reserves/', data)
    // },
}