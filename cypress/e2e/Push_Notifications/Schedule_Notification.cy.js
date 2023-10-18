/// <reference types= "cypress"/>
it('passes', () => {

cy.backend_link();   
cy.Login();
cy.open_Notifications();
cy.Fill_Notification('','https://www.youtube.com/','','','Schedule Notifcation 1', 'Schedule Notification Automation Testing is being done here.');
cy.Schedule_Notification();
cy.send_notification_button();
//2
cy.Fill_Notification('','https://www.youtube.com/','','','Schedule Notifcation test', 'Schedule Notification Automation Testing is being done here.');
cy.Schedule_Notification();
cy.Registered_members();
cy.send_notification_button();

//3
cy.Fill_Notification('','https://www.youtube.com/','','','Schedule Notifcation test', 'Schedule Notification Automation Testing is being done here.');
cy.Schedule_Notification();
cy.Unregistered_members();
cy.send_notification_button();

})
 