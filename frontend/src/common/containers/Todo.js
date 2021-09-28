import { ToDoList } from "common";
import ToDoInput from "common/components/ToDoInput";
import styled from 'styled-components';

export default function Todo (){
    
    return (
        <Div>
        <ToDoList/>
        <ToDoInput/>
        </Div>
    )
}
            
            
        
        
        

const Div = styled.div `text-align: center; margin: 20em` 