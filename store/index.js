import Vuex from 'vuex'
import categoriesModule from './categories'



const createStore = () => {
  return new Vuex.Store({
    modules: {
      categoriesModule
    },
    state: {

    }
  })
}

export default createStore;