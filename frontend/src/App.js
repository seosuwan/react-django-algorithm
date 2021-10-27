import React from "react";
import {Redirect,Route,Switch} from 'react-router-dom'
import './App.css';
import { Home,Navi } from "features/common";
import { UserLogin, UserList, UserDetail, UserAdd,UserModify,UserRemove } from "features/user";


const App = () => (
  <div>
    <Navi/>
      <Switch>
        <Route exact path='/' component= { Home }/>
        <Redirect from='/home' to= { '/' }/>
        <Route exact path = '/userAdd' component = {UserAdd}/>
        <Route exact path = '/userDetail' component = {UserDetail}/>
        <Route exact path = '/userList' component = {UserList}/>
        <Route exact path = '/userLogin' component = {UserLogin}/>
        <Route exact path = '/userModify' component = {UserModify}/>
        <Route exact path = '/userRemove' component = {UserRemove}/>
      </Switch>
  </div>

)
export default App