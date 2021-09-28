const initialState = {todos : [], todo:{}} //전역
export const addTodoAction = todo => ({type: "ADD_TODO", payload: todo})
const todoReducer  = (state = initialState, action) => {
    switch(action.type){
        default : return state
    }


}
export default todoReducer