
//DDl Commands :

// Create:
    // Table 
    // Database

    // User : Creating sub-users in the DB server
    
        // Syntax :
        // Create User username identified by 'password';

        // Example :
        // Create User admin identified by 'admin';
    
    // view: Creating virual tables in the DB server

        // Syntax :
        // Create View viewname as select statement;

        // Example :
        // Create View emp as select * from employee;

        // Select * from emp;

// Drop: delete the data from the DB server
    // Table : 
        // Syntax :
        // Drop Table tablename;

        // Example :
        // Drop Table employee;
    // Database :
        // Syntax :
        // Drop Database databasename;

        // Example :
        // Drop Database pyy;
    // User :
        // Syntax :
        // Drop User username;

        // Example :
        // Drop User admin;
    // View:
        // Syntax :
        // Drop View viewname;

        // Example :
        // Drop View emp;

    // Truncate: delete the data from the table but not the table itself
        // Syntax :
        // Truncate Table tablename;

        // Example :
        // Truncate Table employee;


        // Truncate vs Drop
        // Truncate : delete the data from the table but not the table itself
        // Drop : delete the data from the table and the table itself
        // Truncate is faster than Drop
        // Truncate is not reversible
        // Drop is reversible

// Alter : modify the table
    // Add : add a column to the table
        // Syntax :
        // Alter Table tablename Add columnname datatype;

        // Example :
        // Alter Table employee Add salary int;

    // Modify : modify the column data type
        // Syntax : 
        // Alter Table tablename Modify columnname datatype;

        // Example :
        // Alter Table employee Modify salary varchar(20) null;
    
    // rename : rename the table
        // Syntax :
        // Alter Table tablename Rename To newtablename;

        // Example :
        // Alter Table employee Rename To emp;

        