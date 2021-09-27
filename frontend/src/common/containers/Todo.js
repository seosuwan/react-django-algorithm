import React,{useState} from "react"; //{}는 구조분해
import styled from 'styled-components';
import Button from '@mui/material/Button';
import { TextField } from '@mui/material';

export default function Todo (){
    const [todo, setTodo] = useState('') //getter,setter
    let val = ''
    
    const add = e => {
        e.preventDefault()
        val = e.target.value
    }
    const del = e => {
        e.preventDefault()
        setTodo('')
    }
    const submitForm = e => {
        e.preventDefault()
        setTodo(val)
        document.getElementById('todo-input').value = ''
    }
    
    return (
        <form onSubmit={submitForm} method='POST'>
        <Div>
        <input type = 'text' id='todo-input' onChange={add}/>
        <input type = 'submit' value='ADD'/><br/>
        <span>{todo}</span> 
        <input type = 'button' onClick={del} value='DEL'/>
        </Div></form> )
}
            
            
        
        
        

const Div = styled.div `text-align: center; margin: 20em` 