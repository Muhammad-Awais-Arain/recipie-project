/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
  cy.Login();
  cy.open_Navigation();

 cy.add_Navigation('T.Social Media Links!', 'Social Media')
  cy.find_navigation('T.Social Media Links!')
  cy.add_social_media_link('Facebook','https://www.facebook.com/')
  


  cy.add_social_media_link('Twitter','https://twitter.com/')

   //Edit functionality to edit link for social media
 cy.edit_socialmedia_link()

 

})
 