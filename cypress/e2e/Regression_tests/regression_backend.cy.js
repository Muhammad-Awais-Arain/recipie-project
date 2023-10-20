describe('End-to-End Tests', () => {
    beforeEach(() => {
        cy.backend_link();
        cy.Login();
    })

    it('Add Navigation', () => {

        cy.open_Navigation();
        cy.add_Navigation('Test new Event!', 'Event');
        cy.open_Navigation();
        cy.add_Navigation('T.Member Discount!', 'Member Discount');
        cy.find_navigation('T.Member Discount!');
    })

     it('Member Tools Test', () => {
         cy.open_Membertools_Navigation();
         cy.add_membertools('M.Industry Events', 'Industry Events');
        cy.find_navigation('M.Industry Events');
    })
    it('Info Navigation', () => {
        cy.open_InformationSettings();
        cy.add_Info_Navigation('Info Contact Us', 'Conntact Us');
        
   })


});
