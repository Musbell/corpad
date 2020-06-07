export const state = () => ({
  categories: [
    {
      id: '01',
      name: 'Young Millionaires',
      fee: 30000,
      members: 20,
      maxMembers: 20
    },
    {
      id: '02',
      name: 'Cash Money',
      fee: 10000,
      members: 13,
      maxMembers: 20
    }
  ]
})

export const mutations = {}

export const getters = {
  findCategory(state) {
    return (id) => {
      return state.categories.find((cat) => {
        return cat.id === id
      })
    }
  }
}
