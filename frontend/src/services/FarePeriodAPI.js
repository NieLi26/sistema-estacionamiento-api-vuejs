import API from "./API";

export default {
    getFaresPeriod() {
        return API.get('/fares-period/')
    },
    getFaresPeriodPaginator(page_number) {
        return API.get(`/fares-period-pagination/?page=${page_number}`)
    },
    getFarePeriod(pk) {
        return API.get(`/fares-period/${pk}/`)
    },
    createFarePeriod(data) {
        return API.post('/fares-period/', data)
    },
    updateFarePeriod(pk, data) {
        return API.patch(`/fares-period/${pk}/`, data)
    },
    deleteFarePeriod(pk) {
        return API.delete(`/fares-period/${pk}/`)
    },
}