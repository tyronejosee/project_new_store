/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#dc2626',
        primaryHover: '#b91c1c',
        primaryFocus: '#fca5a5',

        secondary: '#e5e5e5',
        secondaryHover: '#d4d4d4',
        secondaryFocus: '#f5f5f5',

        light: '#f5f5f5', /** n 100 */
        lightTab: '#FFFFFF', /** white */
        lightHover: '#e5e5e5', /** n 200 */

        dark: '#171717', /** n 900 */
        darkTab: '#262626', /** n 800 */
        darkHover: '#404040', /** n 700 */
      },
      fontFamily: {
        body: ['Poppins']
      },
    },
  },
  darkMode: 'class',
  plugins: [],
}

