import axios from "axios";

const baseDomain = 'http://127.0.0.1:8000';
const baseURL = `${baseDomain}/api`;

// export default(url='http://127.0.0.1:8000') => {
//     return axios.create({ // create por crea uan instancia de axios
//         baseURL
//     });
// }

export default axios.create({ // create por crea uan instancia de axios
    baseURL
});