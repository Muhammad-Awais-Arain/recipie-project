/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  cy.Login();
  cy.open_Membertools_Navigation()
  cy.add_membertools('M.Work Schedule Test!', 'Work Schedule')
  cy.find_navigation('M.Work Schedule Test!')
})
 