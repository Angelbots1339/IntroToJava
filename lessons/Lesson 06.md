# Lesson 06: Inheritance and Polymorphism
What a title. I will warn you that this is a longer and complicated topic. Take it slow. Ask questions. Let's get into it!
## Inheritance
You may know the term inheritance in the context of a parent passing away. In that case, the possessions of the parent are given to the children. Inheritance in Java has a similar parent/child relationship in that the child gets fields and methods from the parent as if it were their own. As with any metaphor, it breaks down eventually. One big breakdown is that an instance of the child class IS an instance of the parent class.

Let's look at a `Parent` and `Child` class for now. I'm going to give these small section headers that refer to the file name. However, I won't specify the package or import statements inside the code unless it's needed to demonstrate a specific concept. Hopefully this helps you keep better track of where code is. Unless otherwise specified, they're all located in the same package and in the same directory. Also, I'll add a header for code that would be run inside our `main` method as `Main` instead of saying `Main.java` as well as marking output to the console as `Output`
###### Parent.java
```java
class Parent {
	public int parentField = 10;

	public void parentMethod() {
		System.out.println("I'm defined on the parent class!");
	}
}
```

###### Child.java
```java
class Child extends Parent {
	public int childField = 5;

	public void childMethod() {
		System.out.println("I'm defined on the child class!");
	}
}
```

#### Creating and using the Parent class
We can use the `Parent` class exactly like we'd use any class we've seen so far.
###### Main
```java
Parent parent = new Parent();  
System.out.println(parent.parentField);  
parent.parentMethod();
```

###### Output
```
10
I'm defined on the parent class!
```

#### Creating and using the child class
Creating an instance of the `Child` class also works exactly the same as every other class we've seen. Notice, though, that we can access the `Parent` class's `parentField` and `parentMethod`. We don't need an instance of `Parent` to call those methods because an instance of `Child` IS an instance of `Parent`.
###### Main
```java
Child child = new Child();  
System.out.println(child.parentField);  
System.out.println(child.childField);  
child.parentMethod();  
child.childMethod();
```
###### Output
```
10
5
I'm defined on the parent class!
I'm defined on the child class!
```

#### Using Child where Parent is expected
If we have a method, that accepts an instance of the `Parent` class, we can pass in an instance of the `Child` class as well. This is because an instance of `Child` IS an instance of `Parent`. It is important to note that we cannot access `childField` or `childMethod` on the `object` that is passed into `myMethod`, even though it is an instance of `Child`. The reason is actually a little obvious when you think about it. Someone could create a `Parent` instance and pass it into `myMethod` at which point we wouldn't have `childField` or `childMethod`.
###### Main.java
```java
public class Main {  
    public static void main(String[] args) {  
        Child child = new Child();  
        myMethod(child);  
    }  
  
    public static void myMethod(Parent object) {  
        object.parentMethod();  
    }  
}
```
###### Output
```
I'm defined on the parent class!
```

#### Creating an instance of Child and assigning it to a Parent type
Much like passing an instance of `Child` into a method that accepts a `Parent`, we can also assign an instance of the `Child` class to a variable of type `Parent`. This is because an instance of `Child` IS an instance of `Parent`. The same rules apply to passing it in the method, however, in that we can no longer access `childField` or `childMethod` on the variable `object`.
###### Main
```java
Parent object = new Child();  
object.parentMethod();
```

Output
```
I'm defined on the parent class!
```

#### instanceof and explicit casting
Let's look at another example with `myMethod`. Just like before, we accept an instance of the `Parent` class as a parameter. The `main` method is creating an instance of the `Child` class. Much like before, we can call `parentMethod` on the `object` variable inside of `myMethod`.

The only difference here is we have a check `object instanceof Child`. The `instanceof` part here is just a special java keyword. On the left you put a variable name and on the right you put a class name. It will evaluate to `true` if that variable is an instance of the class and `false` if it isn't. Right after that, we do an explicit cast of `object` to be an instance of the `Child` class. We know we're allowed to do this because we just checked that it was an instance of that class.

Once we have a new variable that's of type `Child`(`childObject`), we can call `childMethod` on it.
###### Main.java
```java
public class Main {  
    public static void main(String[] args) {  
        Child child = new Child();  
        myMethod(child);  
    }  
  
    public static void myMethod(Parent object) {  
        object.parentMethod();  
  
        if (object instanceof Child) {  
            Child childObject = (Child) object;  
            childObject.childMethod();  
        }  
    }  
}
```
###### Output
```
I'm defined on the parent class!
I'm defined on the child class!
```

### Nomenclature: superclass/baseclass and subclass
People will often use "parent" and "superclass" or "base class" interchangeably. They will also use "child" and "subclass" interchangeably. Hi, it's me, I'm people. But you'll definitely want to make sure you're familiar with the terms though because I'm not the only one who swaps those terms out.

### Access Modifiers
Okay, let's wipe the slate clean with the `Parent` and `Child` class we defined earlier. Let's make some new ones.
###### Parent.java
```java
class Parent {
    public int publicField;
    private int privateField;
}
```
###### Child.java
```java
class Child extends Parent {  
    public void print() {
        System.out.println(publicField);  
        // System.out.println(privateField);
    }  
}
```

You've seen `public` used a lot, it just means external classes can access it as well as subclasses. It is the most permissive version available.

`private` means it ONLY belongs to the class that defines it. That means the `Child` class can't access it at all. As a note, the `Child` class could define its own variable called `privateField` and give it whatever access modifier it wanted but it would not be the same `privateField` as the one on the `Parent` class even though it had the same name. Private is good for storing internal data or methods you don't want anyone to be able to access even if they subclass your class.

There are a couple of other options for access modifiers, but I won't explain them just yet. Also keep in mind that the `public` and `private` modifier can be used on methods as well and have the same behavior as they do on fields.

### Preventing subclassing
There is a way to prevent someone from subclassing a class you've made and that is by adding the `final` keyword in front of the `class` keyword. Normally, `final` means "do not let this be re-assigned" but when used in front of the `class` keyword it means "do not let this be subclassed". Example:
###### FinalClassExample.java
```java
final class FinalClassExample {  
    // No one can subclass me!  
}
```

### Abstract classes
In all of the examples above, you could instantiate both the `Parent` and the `Child` class. Sometimes, you want to make a class that has specific functionality but only when someone else comes along and fills in the blanks. Let's look at an example:
###### Animal.java
```java
abstract class Animal {  
    abstract String animalSound();

    public void speak() {
        System.out.println("This animal says: " + animalSound());
    }
}
```
###### Dog.java
```java
class Dog extends Animal {
    @Override
    String animalSound() {
        return "Bark";
    }
}
```
###### Main
```java
Dog dog = new Dog();
dog.speak();
```
###### Output
```
This animal says: Bark
```

Wow that was a lot. Okay, let's go through them one by one. In our `Animal` class, we have added the `abstract` modifier before the `class` keyword. Here it means "you cannot instantiate this class" which makes it the opposite of using the `final` keyword there. That also means that the two of them are not compatible.

Next up we have the line `abstract String animalSound();`. Notice the `abstract` keyword here again as well as the lack of method body. Instead, we end this method with a semicolon right after the parenthesis. There is no `{` or `}` for the method body. This is called an "abstract method". An `abstract` method is one that a non-abstract subclass must implement.

If you have any abstract methods, you must have the `abstract` keyword on the class as well. This makes sense if you think about it. You should not be able to instantiate a class that does not have a definition for a method. What would happen when you called that method? There's nothing to do there and that doesn't make any sense at all! So the compiler helpfully prevents you from doing the wrong thing.

Our animal class has a non-abstract method called `speak` that uses the `String` returned from the `animalSound` method. Notice how we can call this method even though it's not defined. The reason is because we are guaranteed to have it be defined on any subclass that can also be instantiated. This is the culmination of the last 4 paragraphs. The `animalSound` method WILL be defined at some point, so we can use it as if it already is.

Next up is our `Dog` class. It extends the `Animal` class just like our `Child` class extended the `Parent` class. Since the `Dog` class isn't `abstract`, we're forced to implement the `animalSound` method. And in our case, we just return the String "Bark", but you could do anything here that you wanted to really, just like any other method.

Now you'll notice I skipped over that little `@Override` bit. The `@` there means it's an annotation. I don't really want to explain annotations yet, so I'll just say that the `@Override` annotation is a requirement on any method in a subclass that replaces a method in the parent class. In our `abstract` example here, we're not really replacing the `animalSound` method since it's abstract and has no body.

We could, however, override the `speak` method. Let's rewrite our `Dog` class:
###### Dog.java
```java
class Dog extends Animal {  
    @Override  
    String animalSound() {  
        return "Bark";  
    }  
  
    @Override  
    public void speak() {  
        System.out.print("I'm a dog. ");  
        super.speak();  
    }  
}
```

With the same `Main` as above in this section, we get this output:
```
I'm a dog. This animal says: Bark
```

We have the `@Override` annotation on the `speak` method now. Now when someone calls `speak` on an instance of `Dog`, they're calling the method defined inside the `Dog` class instead of the one in the `Animal` class. However sometimes you still want to be able to call the parent's method. We do that using the `super` keyword. This is not a requirement, we could have just said "The dog says woof" or whatever we wanted.

### Multiple Inheritance
One thing you cannot do in Java is "multiple inheritance". All of the examples I've shown you so far extend a single class. Sometimes you may want to extend multiple classes. Well you can't, it's impossible. And not like in the "negative numbers aren't real" impossible that your math teacher tells you, no no like actually impossible. 

### Polymorphism
While you cannot inherit from multiple classes, you can have multiple classes inherit from the same base class. This is called `polymorphism`. `poly` meaning "many" and `morphism` meaning forms. In the FRC world we deal with motors, for example. You can imagine a `Motor` base class that has several helper methods but needs specific subclasses to fill in the details. You could have a subclass for each different motor type. Then whenever a method expects a `Motor`, you could pass an instance of any of the specific subclasses and it would work.

### Final thoughts on simple inheritance
Inheritance is a complicated subject but it's one of the more powerful aspects of OOP. You'll probably have to actually play with various classes and write a bunch of code to fully solidify this, so feel free to come back and review this section at any time.

Also be sure to take a break before jumping into the next section on interfaces.
## Interface
An interface in Java is often referred to as a contract. You declare what methods that need to be implemented inside your interface. Anyone who implements your interface has to implement the methods. This sounds a lot like abstract classes with abstract methods, but there's a couple of key differences. The first is that a class `implements` an interface, it `extends` a class. The second is that you can implement multiple interfaces. And finally, you cannot have any constructor in the interface.

To be honest, interfaces are more powerful than I'm going to do them justice here, but I think having the basics here is good enough. You can always look up more information online about them if you need to.

Let's look at an example of a `Robot` interface
###### Robot.java
```java
public interface Robot {  
    void driveForward();  
    void turnRight();  
}
```
###### SwerveRobot.java
```java
public class SwerveRobot implements Robot {
    @Override
    public void driveForward() {
	    // Complicated math goes here
    }

    @Override
    public void turnRight() {
	    // Complicated math goes here
    }
}
```
###### ConsoleRobot.java
```java
public class ConsoleRobot implements Robot {
    @Override
    public void driveForward() {
        System.out.println("I'm driving forward!");
    }

    @Override
    public void turnRight() {
        System.out.println("I'm turning right!");
    }
}
```

Here's where the "contract" part comes in handy. Any other class or method that accepts a `Robot` as a parameter knows that it at a minimum has the `driveForward` method and the `turnRight` method. It doesn't care whether that instance is `SwerveRobot` or a `ConsoleRobot`, it just knows it satisfies the "contract" of implementing the `Robot` interface.

## Advanced: SOLID
SOLID is an acronym that's used a lot when discussing inheritance and interfaces. The acronym is somewhat interesting and I'll go into some detail about it, but there's so much nuance here that the only way really to do it justify is practice coding and find out what feels right, learning from your mistakes as you go.

With that being said, it has a prominent enough place that if you're feeling pretty confident with the lesson up until now, I'd like to introduce it. The long and short of it is that SOLID is a way to think about abstract classes and interfaces as well as the classes that extend/implement them. Sometimes satisfying one of the letters of the SOLID acronym make it impossible to solve another. Consider them guidelines and not hard rules though they are all phrased as "you SHOULD do X". Think of it as "the principle says I should do this, but I'm going to ignore the whole principle".
### S: Single Responsibility Principle
A class should do one thing and one thing only and it should only have one reason to change. For example, if you had a `Student` class to hold information about a student, you may not want to have the student class know how to print itself to a console. Sure, you could throw a `print` method on the `Student` class, but what if you wanted to make it print to an actual paper printer? Do you modify the `Student` class and add a new method like `printPaper`? Now `print` is ambiguous too. You could change it, but anyone who uses the `Student` class would need to change too.

One way to get around this is make a `StudentPrinter` interface with a single method called `print` that accepts a `Student` as a parameter:
```java
public interface StudentPrinter {
	void print(Student student);
}
```

Now we can have a `ConsolePrinter` or a `PaperPrinter` implement that interface. If you needed to add a new way to print a student's information, you can just define a new class. Easy peasy!

### O: Open/Closed Principle
A class should be open for extension but closed for modification. This one also relates to how people use and call your code. If someone modifies the student class and changes functionality inside it, this may break existing clients. This one is really really dependent on what your class does. For example, it's probably safe to add a field to a class, but if this changes the behavior about how your `Student` class works, it should be extended with a new class instead to avoid breaking existing code. This one is frankly hard to demonstrate because it has a lot to do with how a class is used and what you're breaking by modifying it.

### L: Liskov Substitution
This one has the best name. It's also the easiest principle to mess up and the one I tend to focus on most. The principle states that if a subclass extends some base class, anywhere that base class is used (ie parameter of a method or a field), an instance of the subclass should be valid.

Back to the FRC world, imagine a `Motor` interface that had a `rotationsPerMinute()` method. If you had a linear actuator, that's a motor as well. But not all linear actuators have a motor that spins and therefore `rotationsPerMinute()` is absolutely meaningless in that situation. That suggests that the `Motor` interface is wrong. Maybe instead you need a `SpinningMotor` interface that holds `rotationsPerMinute()` instead.

### I: Interface Segregation
This principle states that an interface shouldn't be too large. If it's too large, you tend to add a lot of methods that need to be implemented. But an implementer may not be interested in every single method and would end up breaking Liskov Substitution method. Instead, add several interfaces that do exactly what you want to.

The irony in all of this is that a type hint in a parameter or field can only have a single interface, so you can't say "I only accept a class that implements these two interfaces". There is a way to get around this (that's a little nasty IMHO) using templates, but we won't cover that until a later lesson.

### D: Dependency Inversion
Interestingly enough, people tend to follow this principle in FRC programming almost accidentally. Dependency Inversion basically means that instead of having a class define its requirements, you pass them into the constructor.

For example, in a real life `SwerveRobot` class, we may not create the specific instances of the motor we want to use inside that class, but instead pass them in as constructor parameters. This gives more flexibility. Imagine a situation where the physical motors on the robot had to change. If you write your code against a `Motor` interface instead of the specific implementation, you really only need to change the place where you create the motor. Everywhere else would still just work assuming Liskov Substitution Principle was being upheld.

## Further reading
Java inheritance is... nuanced and difficult. I'm going to link several of the W3 Schools reference pages here and hopefully their explanation will work anywhere mine failed:
- https://www.w3schools.com/java/java_oop.asp
- https://www.w3schools.com/java/java_inheritance.asp
- https://www.w3schools.com/java/java_polymorphism.asp
- https://www.w3schools.com/java/java_abstract.asp
- https://www.w3schools.com/java/java_interface.asp

Feel free to check out these links to reading more about SOLID principles as well. You'll notice a lot of Student, Car, and Mouse/Keyboard examples. Creative bunch, we programmers are.
- https://www.baeldung.com/solid-principles
- https://www.javatpoint.com/solid-principles-java