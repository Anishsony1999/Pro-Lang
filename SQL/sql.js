
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

    // Drop : drop the column from the table
        // Syntax :
        // Alter Table tablename Drop columnname;

        // Example :
        // Alter Table employee Drop salary;


// Alter Column Constraints :
    // adding primary key
        // Syntax :
        // Alter Table tablename Add Primary Key (columnname);

        // Example :
        // Alter Table employee Add Primary Key (empid);

    // adding foreign key
        // Syntax :
        // Alter Table tablename Add Foreign Key (columnname) References tablename(columnname);

        // Example :
        // Alter Table employee Add Foreign Key (deptid) References department(deptid);
    
    // adding default value
        // Syntax :
        // Alter Table tablename alter columnname set default value;

        // Example :
        // Alter Table employee alter salary set default 0;


// Rename Table by Database :
    // oracle :
        // Syntax :
        // Rename Table tablename to newtablename;

        // Example :
        // Rename Table employee to emp;

    // mysql :
        // Syntax :
        // Rename Table tablename to newtablename;

        // Example :
        // Rename Table employee to emp;

    // postgresql :
        // Syntax :
        // Alter Table tablename Rename To newtablename;

        // Example :
        // Alter Table employee Rename To emp;

// DDL Commands :
    // Grant : grant the permission to the user
        // Syntax :
        // Grant permission on tablename to username;

        // Example :
        // Grant all on employee to admin;

    // Revoke : revoke the permission from the user
        // Syntax :
        // Revoke permission on tablename from username;

        // Example :
        // Revoke all on employee from admin;

// TCL Commands :
    // Commit : commit the transaction
        // Syntax : 
        // Commit;

    // Rollback : rollback the transaction
        // Syntax :
        // Rollback;

    // Savepoint : save the transaction
        // Syntax :
        // Savepoint savepointname; 