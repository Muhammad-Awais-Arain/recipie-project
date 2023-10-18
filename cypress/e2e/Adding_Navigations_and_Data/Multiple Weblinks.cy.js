/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
 cy.Login();
 cy.open_Navigation();
 cy.add_Navigation('T.Multiple Web Links!', 'Multiple Web Links')
 cy.find_navigation('T.Multiple Web Links!') 

 cy.add_weblinks('GOOGLE', 'https://www.google.com/' )

 
 cy.clone_weblink()

 cy.add_weblinks('Twitter', 'https://twitter.com/' )
 cy.add_weblinks('Facebook', 'https://www.facebook.com/')
cy.add_weblinks('LinkedIn', 'https://www.linkedin.com/login' )
// To edit
cy.edit_weblink()

//For Clone
cy.clone_weblink()
})
 