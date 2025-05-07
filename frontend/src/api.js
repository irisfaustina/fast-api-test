import axios from "axios";

//create an instance of acios with the base url
const api = axios.create({
    baseURL: "http://localhost:8000", //url of the backend API for testing, change to server url in production
});
    
//export the api instance
export default api;
