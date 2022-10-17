import API from "./API";

export default {
    getFaresPeriod() {
        return API.get('/fares-period/')
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