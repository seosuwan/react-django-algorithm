const initialState = {todos:[], todo:{}}
export const addTodoAction = todo => ({type: 'ADD_TODO', payload: todo})
export const toggleTodoAction = todoId => ({type: 'TOGGLE_TODO', payload:todoId})
export const deleteTodoAction = todoId => ({type: 'DELETE_TODO', payload:todoId})
const todoReducer = (state = initialState, action)  => {
    switch(action.type){
        case 'ADD_TODO': return {...state, todos:[...state.todos, action.payload]}  //...state는 todos 만 핸들링하겠다, todos 안에 ...state는 그 전 state는 계속 가지고가겠다는 의미
        case 'TOGGLE_TODO': return {...state, todos:state.todos.map(todo => (todo.id === action.payload)
                                                                    ?{...todo, complete: !todo.complete}: todo)}
        case 'DELETE_TODO': return {...state, todos:state.todos.filter(todo => todo.id != action.payload)}  //...state는 todos 만 핸들링하겠다, todos 안에 ...state는 그 전 state는 계속 가지고가겠다는 의미
        default : return state
    }
}

export default todoReducer