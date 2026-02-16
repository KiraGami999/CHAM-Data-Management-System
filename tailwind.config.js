/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./Student Management/templates/**/*.html",
    "./Student Management/**/*.py"
  ],
  theme: {
    
    extend: {
      colors: {
        'black-dark': '#00000050',
        'dull-white':'#FFFFFF83',
        'white-light':'#FFFFFF30',
        'white-medium':'#FFFFFF40',
        'neon-blue':'#2F88FF',
      }
    },
  },

  plugins: [],
}
