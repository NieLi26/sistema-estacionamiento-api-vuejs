import API from "./API";

export default {
    getReservePeriods() {
        return API.get('/reserve-period/')
    },
    // getFare(pk) {
    //     return API.get(`/fares/${pk}/`)
    // },
    // createFare(data) {
    //     return API.post('/fares/', data)
    // },
    // updateFare(pk, data) {
    //     return API.patch(`/fares/${pk}/`, data)
    // },
    // deleteFare(pk) {
    //     return API.delete(`/fares/${pk}/`)
    // },
}