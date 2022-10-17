import API from "../API";

export default {
    // Estacionamientos
    getLots() {
        return API.get('/lots/')
    },
    createLot(data) {
        return API.post('/lots/', data)
    },
    // Reservas
    getReserves() {
        return API.get('/reserves/')
    },
    createReserve(data) {
        return API.post('/reserves/', data)
    },
}