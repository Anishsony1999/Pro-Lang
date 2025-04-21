import java.beans.JavaBean;

@JavaBean
public class BeanClass {
    
    private String name;
    private int age;
    private String email;

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }    
    public void setAge(int age) {
        this.age = age;
    }
}
