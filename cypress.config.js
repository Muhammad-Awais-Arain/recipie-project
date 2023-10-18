const { defineConfig } = require("cypress");

module.exports = defineConfig({


  chromeWebSecurity: false,
  pageLoadTimeout: 150000,
  redirectionLimit: 50,
  projectId: '2chgy2',
  //viewportWidth: 1280,
  //viewportHeight: 720,
  //animationDistanceThreshold: 0,
  "video": false,
  defaultCommandTimeout: 60000,

  
 
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },

  experimentalWebKitSupport: true,

  component: {
    devServer: {
      framework: "nuxt",
      bundler: "webpack",
    },
  }, 

  component: {
    devServer: {
      framework: "nuxt",
      bundler: "webpack",
    },
  },
  
});

