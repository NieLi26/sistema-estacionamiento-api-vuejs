import API from "./API";

export default {
    getFares() {
        return API.get('/fares/')
    },
    getFaresPaginator(page_number) {
        return API.get(`/fares-pagination/?page=${page_number}`)
    },
    getFare(pk) {
        return API.get(`/fares/${pk}/`)
    },
    createFare(data) {
        return API.post('/fares/', data)
    },
    updateFare(pk, data) {
        return API.patch(`/fares/${pk}/`, data)
    },
    deleteFare(pk) {
        return API.delete(`/fares/${pk}/`)
    },
}