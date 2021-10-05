
import React from 'react';
import { connect } from 'common/modules/commonAPI';
import { Signin } from 'features/user';



export default function Home (){
    const handleClick = e => {
        e.preventDefault()
        alert('Home Click')
        connect()
        .then(res => {alert(`접속성공 : ${res.data.connection}`)})
        .catch(err => {alert(`접속 실패 : ${err}`)})
    }
    return (<div>
        <Signin/>
        <button onClick={handleClick} >Connection</button>

    </div>)
}