import { mount } from '@vue/test-utils'
import Default from '../layouts/default'

describe('Layout', () => {
  const wrapper = mount(Default)
  it('default layout is vue instance', () => {
    expect(wrapper.isVueInstance()).toBeTruthy()
  })

  it('has a navbar', () => {
    expect(wrapper.contains('#app-bar')).toBe(true)
  })
})
