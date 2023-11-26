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

        light: '#f5f5f5',
        lightTab: '#FFFFFF',
        lightHover: '#e5e5e5',

        dark: '#171717',
        darkTab: '#292524',
        darkHover: '#404040',
      },
    },
  },
  plugins: [],
}

