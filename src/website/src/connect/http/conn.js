import axios from 'axios'
const axiosConn = axios.create({
    baseURL: 'http://'+window.location.hostname,
    headers: {'Content-Type': 'text/plain'},
  });
axiosConn.interceptors.response.use(function (response) {
    return modifyResponse(response)
})
var modifyResponse = (response)=>{

    if(response && response.data){
        let data = response.data
        return data
    }
    return response;
}
export default axiosConn