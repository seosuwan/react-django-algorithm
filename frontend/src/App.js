import React from "react";
import {Redirect,Route,Switch} from 'react-router-dom'
import { Provider } from 'react-redux'
import { Navi,Home} from "common";
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "features/algorithm";
import { Mathematics,Linear, Nonlinear } from "features/datastructure";
//import { Counter } from "features/counter";
import {createStore , combineReducers} from 'redux'
import { CounterOld } from "features/counterOld";
import { SignUp, UserList, UserJoin, Signin } from "features/user";
import { Todo, ToDoInput, ToDoList } from "features/todos";
import { store } from "app/store";


const App = () => (
    <Provider store = {store}> 
      <Navi/>
        <Switch>
          <Route exact path='/' component= { Home }/>
          <Redirect from='/home' to= { '/' }/>
          <Route exact path = '/signUp' component = {SignUp}/>
          <Route exact path = '/mathematics' component = {Mathematics}/>
          <Route exact path = '/counterOld' component = {CounterOld}/>
          <Route exact path = '/todo' component = {Todo}/>
          <Route exact path = '/linear' component = {Linear}/>
          <Route exact path = '/nonlinear' component = {Nonlinear}/>
          <Route exact path = '/back-tracking' component = {BackTracking}/>
          <Route exact path = '/brute-force' component = {BruteForce}/>
          <Route exact path = '/divide-conquer' component = {DivideConquer}/>
          <Route exact path = '/dynamic-programming' component = {DynamicProgramming}/>
          <Route exact path = '/greedy' component = {Greedy}/>
          
        </Switch>
    </Provider>

)
export default App