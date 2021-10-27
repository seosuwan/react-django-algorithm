import styled from 'styled-components';
import { ToDoInput, ToDoList } from 'features/todos';

export default function Todo (){
    
    return (
        <Div>
        <ToDoInput/>
        <ToDoList/>
        </Div>
    )
}
            
            
        
        
        

const Div = styled.div `text-align: center;` 