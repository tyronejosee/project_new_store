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
      },
    },
  },
  plugins: [],
}

