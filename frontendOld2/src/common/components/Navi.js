import React from "react";
import { Link } from 'react-router-dom';
import styled from 'styled-components';


const Navi = () => (
    <NaviDiv>
     
     <NaviList>
            <NaviItem><Link to='/signUp'style={{textDecorationLine:'none',color:'black'}}><strong>SignUp</strong></Link></NaviItem>
            <NaviItem><Link to='/todo'style={{textDecorationLine:'none',color:'black'}}><strong>Todo</strong></Link></NaviItem>
            <NaviItem><Link to='/counter'style={{textDecorationLine:'none',color:'black'}}><strong>Counter</strong></Link></NaviItem>
            <NaviItem><Link to='/math'style={{textDecorationLine:'none',color:'black'}}><strong>math</strong></Link></NaviItem>
            <NaviItem><Link to='/linear'style={{textDecorationLine:'none',color:'black'}}><strong>linear</strong></Link></NaviItem>

            <NaviItem><Link to="/nonlinear"style={{textDecorationLine:'none',color:'black'}}><strong>nonlinear</strong></Link></NaviItem>
            <NaviItem><Link to="/brute-force"style={{textDecorationLine:'none',color:'black'}}><strong>Brute Force</strong></Link></NaviItem>

            <NaviItem><Link to="/divide-conquer"style={{textDecorationLine:'none',color:'black'}}><strong>Divide & Conquer</strong></Link></NaviItem>
            <NaviItem><Link to="/greedy"style={{textDecorationLine:'none',color:'black'}}><strong>Greedy</strong></Link></NaviItem>
            <NaviItem><Link to="/dynamic-programming"style={{textDecorationLine:'none',color:'black'}}><strong>Dynamic Programming</strong></Link></NaviItem>

            <NaviItem><Link to="/back-tracking "style={{textDecorationLine:'none',color:'black'}}><strong>Back Tracking</strong></Link></NaviItem>
        </NaviList>
    </NaviDiv>
)
export default Navi




const NaviDiv = styled.div`
    padding-bottom: 30px;
    
`
const NaviList = styled.ul`
    display: flex;
    width: min-content;
    height:10px;
    margin: 30px
    
`

const NaviItem = styled.li`
    width: 200px;
    color: none;
    font-family: "ls";
    font-size: 1.5em;
    list-style: none;
    `