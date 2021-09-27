import React from "react";
import {Route,Switch} from 'react-router-dom'
import { Navi } from "common";
import { Linear, Nonlinear } from "datastructure";
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "algorithm";
import { Mathematics } from "datastructure";
import {Home} from 'common/index'

const App = () => (
  <>
  <Navi/>
  <Switch>
    <Route exect path = '/home' component = {Home}/>
    <Route exact path = '/mathematics' component = {Mathematics}/>
    <Route exact path = '/linear' component = {Linear}/>
    <Route exact path = '/nonlinear' component = {Nonlinear}/>
    <Route exact path = '/backTracking' component = {BackTracking}/>
    <Route exact path = '/bruteForce' component = {BruteForce}/>
    <Route exact path = '/divideConquer' component = {DivideConquer}/>
    <Route exact path = '/dynamicProgramming' component = {DynamicProgramming}/>
    <Route exact path = '/greedy' component = {Greedy}/>
    
  </Switch>
  </>
)
export default App