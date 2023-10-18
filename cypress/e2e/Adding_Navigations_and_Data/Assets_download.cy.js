/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
cy.Login();
cy.get('.kt-subheader__toolbar > .btn').click()
cy.get('[wizard-step="2"] > .kt-wizard-v4__nav-body').click()
cy.get('#kt_user_avatar_1 > .download_image').click()
cy.get('#kt_user_avatar_2 > .download_image').click()
cy.get('#kt_user_avatar_3 > .download_image').click()
cy.get('#kt_user_avatar_4 > .download_image').click()
cy.get('#kt_user_avatar_5 > .download_image').click()
cy.get('#kt_user_avatar_12 > .download_image > .la').click({force: true})
})
 