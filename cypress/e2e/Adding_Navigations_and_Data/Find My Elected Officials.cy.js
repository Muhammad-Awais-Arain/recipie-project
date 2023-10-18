/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
  cy.Login();
  cy.open_Navigation();
  cy.add_Navigation('T.Find My Elected Officials', 'Find My Elected Officials')
  cy.find_navigation('T.Find My Elected Officials')

   

  
})
 