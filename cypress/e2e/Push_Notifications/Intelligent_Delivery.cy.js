/// <reference types= "cypress"/>
it('passes', () => {
cy.backend_link();
cy.Login();
cy.open_Notifications();
//1
cy.Fill_Notification('','','','','Intelligent Delivery Test', 'Intelligent Delivery Automation Testing is being done here.');
cy.Intelligent_delivery()
cy.send_notification_button();
cy.send_push_button();

//2
cy.open_Notifications();
cy.Fill_Notification('','https://www.youtube.com/','0','','', 'Automation Testing is being done here.');
cy.Registered_members();
cy.Intelligent_delivery()
cy.send_notification_button();
cy.send_push_button();

//3
cy.Fill_Notification('','','','nike','I Test 3', 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur.');
cy.Unregistered_members();
cy.Intelligent_delivery()
cy.send_notification_button();
 
})
   