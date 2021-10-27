import axios from 'axios';
import React, { useState } from 'react';
import { useHistory  } from 'react-router-dom';

export function UserModify() {
  const history = useHistory()
    const SERVER = 'http://localhost:8080'
    const sessionUser = JSON.parse(localStorage.getItem('sessionUser')) 
    const [modify, setModify] = useState({
        userId:sessionUser.userId,
        username:sessionUser.username,
        password:sessionUser.password,
        email:sessionUser.email,
        name:sessionUser.name,
        regDate: sessionUser.regDate
    })
    
    const handleChange = e => {
        const {value, name} = e.target
        setModify({
            ...modify,
            [name] : value
        })
    }
    const UserModify = modifyRequest => 
    axios.put(`${SERVER}/users`, JSON.stringify(modifyRequest),{headers})
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'JWT fefege..'
      }
    const handleSubmit = e => {
        e.preventDefault()
        const modifyRequest = {...modify}
        alert(`회원정보 수정: ${JSON.stringify(modifyRequest)}`)
        UserModify(modifyRequest)
        .then(res =>{
            alert('회원정보 수정 성공')
            history.push('/userDetail')
        })
        .catch(err =>{
            alert(`회원정보 수정 실패 :${err} `)
        })
    }
  
  return (
    <div>
    <h1>회원정보 수정</h1>
<form onSubmit={handleSubmit} method='PUT'>
   <ul>
       <li>
       <label>
          <span>회원번호: {sessionUser.userId} </span>
        </label>
       </li>
       <li>
       <label>
         <span>아이디 : {sessionUser.username} </span>
        </label>
       </li>
       <li>
           <label>
               비밀번호: <input type="password" id="password" name="password" placeholder={sessionUser.password} onChange={handleChange}/>
           </label>
       </li>
       <li>
       <label>
              이메일: <input type="email" id="email" name="email" placeholder={sessionUser.email} onChange={handleChange}/>
        </label>
         </li>
       <li>
           <label>
               이름: <input type="text" id="name" name="name" placeholder={sessionUser.name} onChange={handleChange}/>
               
           </label>
       </li>
       <li>
           <input type="submit" value="수정" />
       </li>
   </ul>
</form>
</div>
  );
}
export default UserModify