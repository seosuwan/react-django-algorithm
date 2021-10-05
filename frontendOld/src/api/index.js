import axios from 'axios' //서버통신lib!

const server = 'http://127.0.0.1:8000' //서버 url
const header = {'Content-Type':'application/json'} //json객체 타입으로 처리할거다
export const connect = () => axios.get(`${server}/api/connect`) //기능 실행 실제경로
export const userRegister = body => axios.post(`${server}/api/users/register`, {header, body})
export const userList = () => axios.get(`${server}/api/users/list`)
export const userDetail = id => axios.get(`${server}/api/users/${id}`)
export const userRetriever = (key, value) => axios.get(`${server}/api/users/${key}/${value}`)
export const userModify = body => axios.put(`${server}/api/users`, {header, body})
export const userRemove = id => axios.delete(`${server}/api/users/${id}`)