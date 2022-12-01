import API from "./API";

export default {
    getReservePeriods() {
        return API.get('/reserve-period/')
    },
    getReservePeriodPaginator(page_number, q) {
        return API.get(`/reserve-period-pagination/?page=${page_number}&q=${q}`)
    },
    createReservePeriod(data) {
        return API.post('/reserve-period/', data)
    },
    updateReservePeriod(pk, data) {
        return API.put(`/reserve-period/${pk}/`, data)
    },
    deleteReservePeriod(pk) {
        return API.delete(`/reserve-period/${pk}/`)
    },
}