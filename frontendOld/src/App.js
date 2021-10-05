import React from "react";
import {Redirect,Route,Switch} from 'react-router-dom'
import { Navi, SignUp, Todo } from "common";
import { Linear, Nonlinear } from "datastructure";
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "algorithm";
import { Mathematics } from "datastructure";
import {Home} from 'common/index'
import { Counter } from "common/index";
import {createStore , combineReducers} from 'redux'
import {Provider} from 'react-redux'
import {todoReducer,userReducer} from 'reducers'
import { Router } from "@material-ui/icons";
const rootReducer = combineReducers({userReducer, todoReducer})
const store = createStore(rootReducer)
const App = () => (
    <Provider store = {store}> 
      <Navi/>
        <Switch>
          <Route exact path='/' component= { Home }/>
          <Redirect from='/home' to= { '/' }/>
          <Route exact path = '/signUp' component = {SignUp}/>
          <Route exact path = '/mathematics' component = {Mathematics}/>
          <Route exact path = '/counter' component = {Counter}/>
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

