import React from "react";
import {useSelector} from 'react-redux'
import styled from 'styled-components';


export default function UserList(){
    const users = useSelector ( state => state.userReducer.users)
    return(
        <Div>
            {users.length === 0 && (<h1>등록된 회원 정보가 없습니다.</h1>)}
            {users.length !== 0 && (<h1>{users.length} 개의 회원 정보가 있습니다.</h1>)}
        </Div>
    )
}
const Div = styled.div `text-align: center;`