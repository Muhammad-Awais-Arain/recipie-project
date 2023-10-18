/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
  cy.Login();
cy.open_Notifications();
//////

for (let i = 0; i < 20; i++) {
  cy.Fill_Notification('','','','','Test Notification counter', 'Automation Testing is being done here for counter.');
  cy.send_notification_button();
  cy.send_push_button();
}
})
 