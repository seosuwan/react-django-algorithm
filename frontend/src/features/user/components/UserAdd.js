import axios from 'axios';
import React, { useState } from 'react';
import { useHistory  } from 'react-router-dom';


export default function UserAdd() {
    const history = useHistory()
    const SERVER = 'http://localhost:8000/api'
    const [join, setjoin] = useState({
        username:'',password:'',email:'',name:'',birth:'', address:''
    })
    const {username, password, email, name, birth,address} = join
    const handleChange = e => {
        const {value, name} = e.target
        setjoin({
            ...join,
            [name] : value
        })
    }
    const userJoin = joinRequest => 
    axios.post(`${SERVER}/users/join`, JSON.stringify(joinRequest),{headers})
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'JWT fefege..'
      }
    const handleSubmit = e => {
        e.preventDefault()
        const joinRequest = {...join}
        alert(`회원가입 정보: ${JSON.stringify(joinRequest)}`)
        userJoin(joinRequest)
        .then(res =>{
            alert('회원가입 성공')
            history.push('/userLogin')
        })
        .catch(err =>{
            alert(`회원가입 실패 :${err} `)
        })
    }


  return (
    <div>
         <h1>회원 가입을 환영합니다</h1>
    <form onSubmit={handleSubmit} method='POST'>
        <ul>
            <li>
                <label>
                    아이디: <input type="text" id="username" name='username' value={username} size="1" minlength="1" maxlength="15" onChange={handleChange}/>
                </label>
                <small>4~15자리 이내의 영문과 숫자</small>
            </li>
            <li>
                <label>
                    이메일: <input type="email" id="email" name="email" value={email} onChange={handleChange}/> 
                </label>
            </li>
            <li>
                <label>
                    비밀번호: <input type="password" id="password" name="password" value={password} onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    생년월일: <input type="text" id="birth" name="birth" value={birth} onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    이름: <input type="text" id="name" name="name" value={name} onChange={handleChange}/>
                    
                </label>
            </li>
            <li>
                <label>
                    주소: <input type="text" id="address" name="address" value={address} onChange={handleChange}/>
                    
                </label>
            </li>
            <li>
                <input type="submit" value="회원가입"/>
            </li>
        </ul>
    </form>
</div>
)
}