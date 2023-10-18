/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  cy.Login();
  cy.open_Membertools_Navigation()
  cy.add_membertools('M.Web Link Test!', 'Web Link')
  cy.find_navigation('M.Web Link Test!')
  cy.add_weblinks('GOOGLE', 'https://www.google.com/' )

    //Edit functionality for weblink
    cy.edit_weblink()
})
 

