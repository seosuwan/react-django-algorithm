import React from "react";
import { useDispatch, useSelector } from "react-redux";
import styled from 'styled-components'

export default function ToDoList (){
    const todos = useSelector( state => state.todos)
    const dispatch = useDispatch()
    return(
        <ToDoListDiv>
        {todos.length === 0 && (<h1>등록된 할일이 없습니다.</h1>)}
        {todos.length !== 0 && (<h1>{todos.length}개의 할일 목록 있습니다.</h1>)}
       
       </ToDoListDiv>
     )
}
const ToDoListDiv = styled.div `text-align: center; margin: 20em`