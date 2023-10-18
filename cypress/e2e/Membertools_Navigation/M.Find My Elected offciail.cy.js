/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
    
  cy.Login();
  cy.open_Membertools_Navigation()
  cy.add_membertools('M.Find My Elected Officials!', 'Find My Elected Officials')
  cy.find_navigation('M.Find My Elected Officials!')

})
 


 