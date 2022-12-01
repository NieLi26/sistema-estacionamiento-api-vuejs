import API from "../API";

export default {
    // Estacionamientos
    getLots() {
        return API.get('/lots/')
    },
    getLot(pk) {
        return API.get(`/lots/${pk}/`)
    },
    createLot(data) {
        return API.post('/lots/', data)
    },
    // Reservas
    getReserves() {
        return API.get('/reserves/')
    },
    getReservePaginator(page_number, q) {
        return API.get(`/reserve-pagination/?page=${page_number}&q=${q}`)
    },
    createReserve(data) {
        return API.post('/reserves/', data)
    },
}