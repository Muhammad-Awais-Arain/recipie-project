/// <reference types= "cypress"/>
it('passes', () => {
  cy.backend_link();
  cy.Login();
cy.open_Notifications();
//1 Registered
cy.Fill_Notification('','https://www.youtube.com/','0','',' URL Test Registered', 'Automation Testing is being done here.');
cy.Registered_members();
cy.send_notification_button();
cy.send_push_button();

//2 UnRegistered
cy.Fill_Notification('','','','','Test Unregistered', 'Automation Testing is being done here.');
cy.Unregistered_members();
cy.send_notification_button();
cy.send_push_button();

//3 All Notification
cy.Fill_Notification('','','','nike.png','Test Notification ', 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur.');
cy.send_notification_button();
cy.send_push_button();

//4  Intelligent Delivery
cy.Fill_Notification('','','','',' Intelligent Delivery Test ', 'SQA Automation Testing is being done here.');
cy.Registered_members();
cy.Intelligent_delivery()
cy.send_notification_button();
cy.send_push_button();


//5 Schedule Notification
cy.Fill_Notification('','https://www.youtube.com/','2','','', 'Schedule Notification Automation Testing is being done here.');
cy.Schedule_Notification();
cy.send_notification_button();
cy.send_push_button();

//5 target by zip
cy.Fill_Notification('6276272','','','','Schedule push', 'Automation Testing is being done here.');
   cy.send_notification_button();
    cy.send_push_button();
    
})
 