# wedding

Invitation and RSVP website for weddings (or anything else you would want to use it for)
Built with python 3.4 and Django 7.1 with xlsxreader package and mandrill package

This project has 3 main features:

1. The Invitation - A unique webpage per person/group invited. On the page the invitation is displayed
   and there is an RSVP section. 
   In the RSVP section the user can indicate if they are coming and any additional details can be added
   for instance: Food restrictions and allergies, message to the couple, etc.
   
2. The Admin Page - Django's admin page, In which the event holder can input and manage invitations, 
   send automatic email invitations and reminders and export all invitations to an Excel.
   
3. The Statistics page - a webpage which displays all of the RSVP responses and statistics on the RSVP responses.
   Exports the information into an excel worksheet. 
   Displays additional information that was added into the invitation such as: messages, diet information, 
   ride information, etc.

The project uses the default SQLite database That's built into Django.
