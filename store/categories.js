export const state = () => ({
  categories: [
    {id: "01", name : "Young Money", ammount: 10000, payment: 47500, members: 10, interval: '7', start: '2020-08-12', finished: "false", maxUsers: 10},
    {id: "02", name : "Cash Money", ammount: 30000, payment: 143500, members: 5, interval: '10', start: '2020-08-20', finished: "false", maxUsers: 10},
    {id: "03", name : "Ultimate", ammount: 2000, payment: 275000, members: 15, interval: '10', start: '2020-08-20', finished: "false", maxUsers: 20},
  ]
})

export const getters = {
  getCategories(state){
    return state.categories
  }
}