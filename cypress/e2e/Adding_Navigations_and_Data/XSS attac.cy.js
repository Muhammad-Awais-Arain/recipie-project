/// <reference types= "cypress"/>
/*describe('Accessibility Tests', () => {
  it('should pass accessibility tests', () => {
    cy.visit('https://desibook.web.linkedunion.live/');
    cy.get('.ms-auto > .MainNavbar_menu_dropdown__3ZsNU').click()
    cy.get('[href="/report-workplace-violation/report/1017373"]').click()
    cy.wait(10000)
    cy.injectAxe();
   // cy.checkA11y();
    cy.customcheckAlly()
  });
});

describe('Login page', () => {
    it('Should not allow XSS injection in login form', () => {
      cy.visit('https://desibook.web.linkedunion.com/') // replace with the actual URL of your login page
      cy.get('.mobile-v-h-inner-menu > .nav-link').click()
      cy.get('#generalSearch').type('<script>alert("XSS injection detected");</script>')
      cy.get('.mb-1 > .topline-in > .kt-input-icon > .form-control').type('henry')
      //cy.get('input[name="email"]').type('<script>alert("XSS injection detected");</script>')
     // cy.get('input[name="password"]').type('password')
      //cy.get('.kt-checkbox > span').click()
      //cy.get('#kt_login_signin_submit').click()
      cy.get(':nth-child(6) > .btn').click()
      // Check that the login was unsuccessful and the XSS script was not executed
      cy.location('pathname').should('not.eq', '/dashboard')
      cy.get('body').should('not.contain', 'XSS injection detected')
    })
  })
  


describe('Login page', () => {
    it('Should not allow XSS injection in login form', () => {
      cy.visit('https://desibook.admin.linkedunion.com/') // replace with the actual URL of your login page
    
      cy.get('input[name="email"]').type('<script>alert("XSS injection detected");</script>')
      cy.get('input[name="password"]').type('password')
      cy.get('.kt-checkbox > span').click()
      cy.get('#kt_login_signin_submit').click()
       //Check that the login was unsuccessful and the XSS script was not executed
      cy.location('pathname').should('not.eq', '/dashboard')
      cy.get('body').should('contains', 'XSS injection detected')
    })
  })
  */
/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
      
    cy.Login();
    //cy.open_Navigation();
    //cy.add_Navigation('T.Multiple News!', 'Multiple News')
    cy.find_navigation('T.Multiple News!')
    
    cy.get('a > .btn').should('be.visible').click()
cy.get(':nth-child(2) > .col-lg-10 > .form-control').type('<script>setTimeout(function(){alert("XSS attack executed after 5 seconds!");}, 100000);</script>',{ parseSpecialCharSequences: false })
cy.get(':nth-child(3) > .col-lg-10 > .form-control').type('<script>setTimeout(function(){alert("XSS attack executed after 5 seconds!");}, 100000);</script>',{ parseSpecialCharSequences: false })
cy.get('iframe.cke_wysiwyg_frame').then($iframe => {
    const $editable = $iframe.contents().find('.cke_editable')
    cy.wrap($editable).type('<script>setTimeout(function(){alert("XSS attack executed after 5 seconds!");}, 10000);</script>',{ parseSpecialCharSequences: false })
})
//cy.get('#kt_dropzone_1').attachFile('<script>alert("XSS attack")</script>', { subjectType: 'drag-n-drop' });
cy.get('.col-lg-4 > .btn').click()
 //Check that the login was unsuccessful and the XSS script was not executed
 cy.location('pathname').should('not.eq', '/dashboard')
 cy.get('body').should('contains', 'XSS injection detected')
    
  })
   