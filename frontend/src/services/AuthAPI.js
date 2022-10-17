import API from "./API";

export default {
    createUser(data) {
        return API.post('/auth/users/', data)
    },
    loginUser(data) {
        return API.post('/auth/token/login/', data)
    },
    logoutUser() { // token in bbdd
        return API.post('/auth/token/logout/')
    },
}