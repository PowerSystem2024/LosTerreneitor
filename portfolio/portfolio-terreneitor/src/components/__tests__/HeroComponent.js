import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import HeroComponent from '../HeroComponent.vue'

describe('HelloWorld', () => {
  it('renders properly', () => {
    const wrapper = mount(HeroComponent, { props: { msg: 'Vitest' } })
    expect(wrapper.text()).toContain('Terreneitor')
  })
})
