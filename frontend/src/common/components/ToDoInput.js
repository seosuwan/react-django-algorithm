import React,{useState} from "react"; //{}는 구조분해
import styled from 'styled-components';
import { v4 as uuidv4} from 'uuid'
import { useDispatch } from "react-redux";
import { addTodoAction } from "reducers/todo.reducer";
export default function ToDoInput (){
    const [todo , setTodo] = useState('')
    const dispatch = useDispatch()
    const submitForm = e => {
        e.preventDefault()
        const newTodo = {
            id:uuidv4(),
            name: todo,
            complete: false
        }
        addTodo(newTodo)
        setTodo('')   
    }
    const addTodo = todo => dispatch(addTodoAction(todo))
    const handleChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
        
        
    }
    return (
        <form onSubmit={submitForm} method='POST'>
        <Div>
        <input type = 'text'
                id='todo'
                name = 'todo'
                placeholder = "할일 입력"
                value = {todo}
                onChange={handleChange} />
        <input type = 'submit' 
                value='ADD'/><br/>
        </Div></form> 
    )
}
const Div = styled.div `text-align: center; margin: 20em`