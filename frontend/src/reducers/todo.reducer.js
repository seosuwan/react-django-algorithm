const initialState = {todos : [],todo : {}}
export const addTodoAction = todo => ({type :'ADD_TODO', payload: todo})
export const toggleTodoAction = id => ({type : 'TOGGLE_TODO', payload: id})
export const deleteTodoAction = id => ({type : 'DELETE_TODO', payload: id})
const todoReducer = (state = initialState, action)  => {
    switch (action.type){
        case 'TOGGLE_TODO' : return {...state, todos: state.todos.map(todo => (todo.id === action.payload)
                                                                    ?{...todo, complete: !todo.complete}: todo )}
        case 'DELETE_TODO' : return {...state, todos: state.todos.filter(todo => todo.id != action.payload)}
        case 'ADD_TODO': return {...state, todos:[...state.todos, action.payload]}
        default: return state
    }
}

export default todoReducer