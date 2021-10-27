import React from "react";
import { useHistory  } from 'react-router-dom';

export default function Home () {
    const sessionUser = localStorage.getItem("sessionUser")
    const history = useHistory()
    const logout = e => {
        e.preventDefault()
        localStorage.setItem('sessionUser','')
        history.push('/')
    }
    return(
    <div>
        {sessionUser !== ""&& <input type="button" value="로그아웃" onClick={logout}/>}
        <h1>안녕하세요 HOME 입니다............</h1>

        {sessionUser !== ""? <h1>{sessionUser.username} 접속중...</h1>
        :<>
        <button onClick = {e => history.push('/userAdd')}>회원가입하세요</button>
        <button onClick = {e => history.push('/userLogin')}>로그인</button></>}
    </div>)
}