/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
  cy.Login();
  cy.open_Navigation();
  cy.add_Navigation('T.Web Link!', 'Web Link')
  cy.find_navigation('T.Web Link!') 
  cy.add_weblinks('GOOGLE', 'https://www.google.com/' )

  //Edit functionality for weblink
  cy.edit_weblink()
})
 