import API from "./API";

export default {
    getLots() {
        return API.get('/lots/')
    },
    getLots(pk) {
        return API.get(`/lots/${pk}/`)
    },
    createlot(data) {
        return API.post('/lots/', data)
    },
    updateLot(pk, data) {
        return API.patch(`/lots/${pk}/`, data)
    },
    deleteLot(pk) {
        return API.delete(`/lots/${pk}/`)
    },
}