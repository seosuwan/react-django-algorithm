import { ToDoList ,ToDoInput } from "common";

import styled from 'styled-components';

export default function Todo (){
    
    return (
        <Div>
        <ToDoInput/>
        <ToDoList/>
        </Div>
    )
}
            
            
        
        
        

const Div = styled.div `text-align: center;` 