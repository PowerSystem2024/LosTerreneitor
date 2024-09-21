<script lang="js">
import { apiKey } from './constants.vue'
let hook = {}

export class getLocation {
  static async getData() {
    const response = await fetch('https://geolocation.microlink.io')
    const data = await response.json()
    return data
  }

  static async currentPosition() {
    return new Promise((resolve, reject) => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const latitude = position.coords.latitude
            const longitude = position.coords.longitude
            hook.lat = latitude
            hook.lon = longitude
            resolve(hook)
          },
          (error) => {
            reject(error)
          }
        )
      } else {
        reject(new Error('Geolocalización no está soportada por este navegador'))
      }
    })
  }

  static async apiData() {
    const lat = await this.lat()
    const lon = await this.lon()
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`
    const res = await fetch(url)
    const data = res.json()
    return data
  }

  static async ip() {
    const data = await this.getData()
    return data.ip.address
  }

  static async city() {
    const data = (await this.apiData()) ?? (await this.getData())
    return data.name ?? data.city.name
  }

  static async country() {
    const data = (await this.apiData()) ?? (await this.getData())
    return data.sys.country ?? data.country.name
  }

  static async flag() {
    const data = await this.getData()
    return data.country.flag
  }

  static async lat() {
    const data = await this.currentPosition()
    return data.lat
  }

  static async lon() {
    const data = await this.currentPosition()
    return data.lon
  }
}
</script>
