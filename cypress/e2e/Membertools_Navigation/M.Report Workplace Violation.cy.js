/// <reference types= "cypress"/>
it('passes', () => {
cy.backend_link();
cy.Login();
cy.open_Membertools_Navigation()
cy.add_membertools('M.Report Workplace Violation!', 'Report Workplace Violation')
cy.find_navigation('M.Report Workplace Violation!')
})
