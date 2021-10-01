import SignIn from 'common/containers/Signin';
import React from 'react';
import { connect } from 'api';


export default function Home (){
    const handleClick = e => {
        e.preventDefault()
        alert('Home Click')
        connect()
        .then(res => {alert(`접속성공 : ${res.data.connection}`)})
        .catch(err => {alert(`접속 실패 : ${err}`)})
    }
    return (<div>
        <SignIn/>
        <button onClick={handleClick} >Connection</button>

    </div>)
}
