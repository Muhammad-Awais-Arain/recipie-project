/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    
  cy.Login();
cy.open_Notifications();

//1
cy.Fill_Notification('','https://www.youtube.com/','5','','', 'Automation Testing is being done here.');
cy.send_notification_button();
cy.send_push_button();

//2
cy.Fill_Notification('','','','','Test Notification', 'Automation Testing is being done here.');
cy.send_notification_button();
cy.send_push_button();

//3
cy.Fill_Notification('','','','nike','Test Notification 2', 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur.');
cy.send_notification_button();
cy.send_push_button();

//4 Schedule.
cy.Fill_Notification('','https://www.youtube.com/','','','Schedule Notifcation test', 'Schedule Notification Automation Testing is being done here.');
cy.Schedule_Notification();
cy.send_notification_button();




})
 