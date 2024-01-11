/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#dc2626',
      },
      fontFamily: {
        body: ['Poppins']
      },
    },
  },
  darkMode: 'class',
  plugins: [],
}
