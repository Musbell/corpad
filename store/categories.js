const state = {
  categories: [
    {id: "01", name : "Young Money", ammount: 10000, payment: 47500, members: 10, interval: '7', start: '2020-08-12', takenPositions: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], finished: "false", maxUsers: 10, description: 'This is the Group for Ultimate Miliionaires. Dont Join if kana da taurin bashi. Make sure you pay kudi on time. You will recieve your kudi on time too. danna spin domin kayi joining'},
    {id: "02", name : "Cash Money", ammount: 30000, payment: 143500, members: 5, interval: '10', start: '2020-08-20', takenPositions: [0, 1, 3, 5, 9], finished: "false", maxUsers: 10, description: 'This is the Group for Ultimate Miliionaires. Dont Join if kana da taurin bashi. Make sure you pay kudi on time. You will recieve your kudi on time too. danna spin domin kayi joining'},
    {id: "03", name : "Ultimate", ammount: 2000, payment: 275000, members: 15, interval: '10', start: '2020-08-20', takenPositions: [], finished: "false", maxUsers: 20, description: 'This is the Group for Ultimate Miliionaires. Dont Join if kana da taurin bashi. Make sure you pay kudi on time. You will recieve your kudi on time too. danna spin domin kayi joining'},
  ]
}

const getters = {
  categories(state){
    return state.categories
  },
  singleCategory(state){
    return id => {
      return state.categories.find(cat => {
        return cat.id === id
      })
    }
  }
}

export default {
  namespaced: true,
  state,
  getters
}