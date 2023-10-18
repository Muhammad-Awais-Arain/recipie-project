/// <reference types= "cypress"/>
it('passes', () => {
    cy.backend_link();
    cy.Login();
    cy.open_Notifications();
    cy.Fill_Notification('32145661616161','https://www.youtube.com/','5','','', 'Automation Testing is being done here.');
   cy.send_notification_button();
    cy.send_push_button();
//2
    cy.Fill_Notification('32145661616161','','','','U.Registered test 2', 'Automation Testing is being done here.');
    cy.Unregistered_members();
    cy.send_notification_button();
    cy.send_push_button();
    
       
//3
cy.Fill_Notification('32145661616161','','','nike','Registered test 3', 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur.');
cy.Registered_members();
cy.send_notification_button();
cy.send_push_button();

//4
cy.Fill_Notification('32145661616161','https://www.youtube.com/','','','Schedule Notifcation 1', 'Schedule Notification Automation Testing is being done here.');
cy.Schedule_Notification();
cy.send_notification_button();



})