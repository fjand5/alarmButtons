import axiosConn from './conn.js'
const getButtonsData = function (){
    const url = '/button/'
    return axiosConn.get(url)
}
const clearButton = function (id){
    const url = '/button/'
    return axiosConn.post(url,id)
}
export {getButtonsData,clearButton}
