/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./builders_admin/templates/builders_admin/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#f6b61b",
        secondary: "#1c2436",
      },
      screens: {
        ssm: "420px",
        xsm: "460px",
        midsm: "560px",
        midssm: "692px",
        xxxl: "1200px",
        xxl: "1300px",
      },
      maxWidth: {
        maincontent: "1800px",
      },
      boxShadow: {
        "top-left-bottom": "-6px -3px 31px -13px rgba(0,0,0,1)",
      },
    },
  },
  plugins: [],
};