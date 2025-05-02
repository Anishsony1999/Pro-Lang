package javalang;

public class Company {
    int companyId;
    String companyName,Location;

    Company(int companyId,String companyName,String Location){
        this.companyId = companyId;
        this.companyName = companyName;
        this.Location = Location;
    }

    void companyDetails(){
        System.out.println("Company Id : " + companyId);
        System.out.println("Company Name : " + companyName);
        System.out.println("Company Location : " + Location);
    }


    public static void main(String[] args) {
        Employee e = new Employee(1, "Anish", 1, "Sony", "TVM");
        e.employeeDetails();
    }
}


class Employee extends Company{
    int employeeId;
    String employeeName;

    Employee(int employeeId,String employeeName,int companyId,String companyName,String Location){
        super(companyId,companyName,Location); // calling parent class constructor
        this.employeeId = employeeId;
        this.employeeName = employeeName;
    }

    void employeeDetails(){
        System.out.println("Employee Id : " + employeeId);
        System.out.println("Employee Name : " + employeeName);
        companyDetails();
    }
}