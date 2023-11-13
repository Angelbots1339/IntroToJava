# Lesson 05: Object Oriented Programming part 2

OOP opens up a lot of possibilities in how to organize your code. We're going to cover a few more things related to classes in this and the next lessons. They won't be directly related to each other, so treat each section as its own thing instead of treating it as flowing from one section to the next.

## Chaining constructors
In the previous lesson we covered method overloading. Make sure to review that section if you're still a little rusty on it. While the constructor is a unique method in that it helps to insatiate a class, the same rules for method overloading actually apply here as well. Let's look at an example using the `Rational` class in assignment 06. We have three constructors:
```java
class Rational {
	public final int numerator;
	public final int denominator;

	public Rational() {
		this.numerator = 0;
		this.denominator = 1;
	}

	public Rational(int numerator) {
		this.numerator = numerator;
		this.denominator = 1;
	}

	public Rational(int numerator, int denominator) {
		this.numerator = numerator;
		this.denominator = denominator;
	}
}
```

If you think about it, all 3 constructors do similar functionality. They all assign to the numerator and denominator. You could create three instances with the same values for the numerator and denominator like this:
```java
Rational a = new Rational();
Rational b = new Rational(0);
Rational c = new Rational(0, 1);
```

What if we could call one constructor from another? This way, we could re-use code instead of re-writing it inside every different constructor. Let's look at the same example as above, but using what's known as "constructor chaining".
```java
class Rational {
	public final int numerator;
	public final int denominator;

	public Rational() {
		this(0);
	}

	public Rational(int numerator) {
		this(numerator, 1);
	}

	public Rational(int numerator, int denominator) {
		this.numerator = numerator;
		this.denominator = denominator;
	}
}
```

Let's look at the creation of `a` above again:
```java
Rational a = new Rational();
```

Inside the empty argument constructor, we call `this(0)`. This is just like any other method call, except it only applies to constructors. The compiler knows we have a single argument constructor that takes a single `int`. That's the `Rational(int numerator)` constructor to be specific. `this(0)` calls that constructor with a value of `0` for the `numerator` parameter.

It's very important to understand that as long as execution hasn't returned from the original constructor that's called, we're still creating the same new object. We don't create a second object by chaining constructors this way.

Inside the `Rational(int numerator)` constructor, we have another chained constructor call: `this(numerator, 1)`. This calls our `Rational(int numerator, int denominator)` constructor with whatever `numerator` was passed in and with `1` for our `denominator`.

There's several benefits to this approach. The first is that we have an easier time of making sure everything is instantiated correctly. This approach can also reduce duplication. For example, we have `this.denominator = 1` in two places with our example that doesn't use constructor chaining. We only use the value of `1` a single time, when calling `this(numerator, 1)`. For simple values, this may not seem worthwhile, but as programs get more complicated, this technique can be extremely valuable. Keep it in mind.

## Static methods and fields
So far, you've seen examples of fields and methods on instances. However, you can also put fields and methods on the class itself. These are called `static` methods and fields. Essentially you can think of them as being shared by all instances of the class. Let's look at an example:
```java
class StaticExample {
	public static int staticField = 5;  
  
	public void print() {  
	    System.out.println(staticField);    
		staticField = 10;
	}
}
```

Let's create two instances (ie in our `main` method):
```java
StaticExample a = new StaticExample();
StaticExample b = new StaticExample();
```

Note: You may be wondering how we created an object without defining a constructor. By default, if no constructor is defined then an empty no-argument constructor is defined for you that does nothing.

Now check out this code:
```java
a.print();
b.print();
```

When `a`'s print method is called, we execute `System.out.println(staticField);`. Since `staticField` started with the value of `5`, this prints out `5`. We then change the value of the static field to be `10` and exit the `print` method that was called on `a`. Next up, we call the same method, but on the instance `b`. Now, when we execute `System.out.println(staticField);`, `staticField` has a value of `10` since it's shared between the two objects. We then update it again to have a value of `10`, though that doesn't do much since it's already at `10`. Finally we're done with `b`'s print method.

The important thing to note here is that the `static` keyword on the field made them shared between all instances of the object.

You can also access the field `staticField` outside of the class. For example, you can do:
```java
System.out.println(a.staticField);
```

This does work and prints the value of the field as expected, but the "more correct" way to do this is via the class name:
```java
System.out.println(StaticExample.staticField);
```

Of course, the same thing applies to static methods:
```java
class StaticExample2 {
	public static void print() {
		System.out.println("I'm in a static method!");
	}
}
```

And outside of that code:
```java
StaticExample2.print();
```

This would print `I'm a static method!` as expected.

Please note that static methods cannot access non-static fields or methods. This is because there's no instance for them to actually access the non-static fields or methods on. This is true even if you use the less favored technique of calling a static method or field on an instance of a class.

The opposite does work, however. You can call static methods or access static fields from an instance. It's just important to remember that they're shared by every instance of that class in your program. Any changes to static fields will remain until they're changed again or your program ends, even if your program doesn't have any instances of the class at all.
### Public Static Void Main (PSVM)
FINALLY! After all this time, I can finally explain the Java code at the start of every assignment:
```java
class Main {
	public static void main(String[] args) {
		// Your code goes here
	}
}
```

We know what a class is at this point, it's just a container for data and operations on that data. In this case, we call our class `Main` mostly out of convention. It has a method called `main`.

The `main` method has the `public` modifier which means it's available outside of the `Main` class. We definitely want that because this is the entry point into our application. In other words, whether this is running in GitHub actions, in GitHub codespaces, VSCode, etc., SOMETHING has to call this method for us so it has to be `public`.

Next up is `static`. Whatever calls our code doesn't create an instance of the `Main` class. Instead, it calls the `main` method directly.

You're familiar with `void` as well, it's the return type that means "this method doesn't return anything".

Finally, we have `String[] args`. This is a parameter declaration. In this case, it's an array of `String` instances. We call that array `args`. This allows someone from outside your program to pass in arguments into your program, much like you would pass in arguments when calling a method.

### Singletons
Singletons are a bit of a hat trick. They're useful to know, great for high society conversations around Java, but personally I try to avoid them. There's a LOT that can go wrong with them, several drawbacks I don't want to get into, and there's almost always a better way to implement the same functionality.

We've assembled all of the pieces required for them, so let's dive in:
```java
public class SingletonExample {  
    private static SingletonExample instance;  
      
    private SingletonExample() {  
          
    }  
      
    public SingletonExample getInstance() {  
        if(instance == null) {  
            instance = new SingletonExample();  
        }  
          
        return instance;  
    }  
}
```

We have a field here called `instance` and it's of the same type as the class that it's in. In the singleton pattern, having the field be called `instance` and the method to get the instance of the class be called `getInstance` is very very common.

We have a constructor to create an instance of the class. Ours is empty, and we could have left it out completely if not for that `private` modifier. We don't want anyone else to be able to create an instance of our class.

Next up is our `getInstance` method. It's the meat of the Singleton pattern. It checks to see if the static `instance` field is `null`. If it is, then we have yet to create an instance of our class. In other words, this is the first time `getInstance` has been called on this class since the program began running. We then assign that static field to be the result of calling our constructor. This is the one and only time the constructor will be called. The next time we call `getInstance`, our field will have been set already and we just return its value.

As I said before, I don't recommend this pattern. However, it's useful to understand how it works when people talk about it or to quickly identify the pattern if you ever see it in someone else's code. I'll leave understanding "why singleton's are bad" to your best Google searches. :)

## Enums
Enum's in Java are very very cool. I think Java is one of my favorite implementations of this programming concept. Let's look at an example:
```java
public enum Level {  
    LOW,  
    MEDIUM,  
    HIGH  
}
```

Okay, a few things to notice. Instead of `class`, we have `enum`. The name of this `enum` follows the same camel case rules of classes. In this case, we're representing the `Level` of something and we have 3 options: `LOW`, `MEDIUM`, and `HIGH`. These are the only instances of this `enum` that are possible. That's part of the power of the `enum`, when you have a specific set of values you want to represent. Notice that they are comma separated and there's no semicolon at the end. I put one per line for readability and to more easily see when changes are made, but that's just a convention you can choose whether to follow or not.

You can still use them in any of the ways you'd use a class. For example, you can assign it to a variable:
```java
Level myLevel = Level.HIGH;
```

Or use it as a method parameter:
```java
public void myMethod(Level myLevel) {
	System.out.print(myLevel);
}
```

If we called that method, it would print out the name of the enum value:
```java
myMethod(Level.MEDIUM);
```

That would print `MEDIUM` to the screen.

### Naming Convention
The convention for enum values is all capital snake case. e.g. `THIS_IS_AN_EXAMPLE_OF_ALL_CAPS_SNAKE_CASE`. Snake case just means each word is separated by an underscore. This convention is used for any constant values, which I haven't explained because the`const` modifier is its own thing that I don't want to get into.

It's also contentious as a naming convention, so much so that people will use both pascal and camel case in its place. They really did go for every option here. Most classically trained programmers tend to use "all caps snake case" so that's what I'll use in all of the examples.
### values()
You do get some extra goodies on top of a normal class with an enum. Among those, you get a `values()` method that returns an array that is the `enum`'s type. The array is the same size as the number of enum elements you have. In our `Level`, example, `Level.values()` would return an array of 3 elements. You can use this in any of the same ways you'd use an array. For example, you can print the values in a for-each loop:
```java
for (Level level : Level.values()) {  
    System.out.println(level);  
}
```
### Comparison
Enum comparison's are also super neat. Let's look at this specific bit of code:
```java
Level myLevel = Level.MEDIUM;  
System.out.println(myLevel.equals(Level.MEDIUM));  
System.out.println(myLevel == Level.MEDIUM);
```

Both of these evaluate to `true`. Normally for instances of classes, you want to use the `equals` method. However, in the case of the `enum`, they're the same exact instance. Even using a separate variable called `myLevel`, that doesn't make a new copy of the `Level.MEDIUM` instance, it IS the same instance. We'll get into the `equals` method in the next lesson, for now just know that you can use `==` to compare instances of an `enum`.
### Constructor
This is the part of an enum in Java that I think Java handles better than other languages. We can actually make a custom constructor for the `enum`. Let's look at an example:

```java
public enum FanSpeed {  
    LOW(100),  
    MEDIUM(200),  
    HIGH(400);  
  
    public final int rotationsPerMinute;  
  
    FanSpeed(int rotationsPerMinute) {  
        this.rotationsPerMinute = rotationsPerMinute;  
    }  
}
```

Let's go over a few things. The first thing to notice is that instead of something like `LOW`, we have `LOW(100)`. Java will turn this into a constructor call for us. The second thing to notice is that unlike above with our `Level` enum, we have to put a semicolon after the last value, `HIGH`. You could have put a semicolon there the entire time, but most IDEs will show a warning that it's redundant.

Next up, we have a field definition: `public final int rotationsPerMinute;`. This definition works the same as any other field definition for a class. One thing to note is that it's not required the field be `public` or `final`, but both are pretty common. If you change the value of a field in an `enum` instance, it'll be changed across the entire codebase since it shares that instance. In other words, if this field wasn't `final`, then executing the code `FanSpeed.MEDIUM.rotationsPerMinute = 5` would make it have the value of `5` everywhere, but `FanSpeed.LOW.rotationsPerMinute` would still be 100 and `FanSpeed.HIGH.rotationsPerMinute` would still be 400. There's not usually a good reason to want this behavior, so `final` is recommended.

Finally, we have our constructor itself. It's exactly the same as any constructor for a class. You can have multiple of them, do constructor chaining, etc. Its purpose is to initialize the enum's instances. The only difference is that it is `private` by default. You cannot add any other modifier there and adding the `private` modifier is redundant. 

In FRC code, I use this technique to define motors:
```java
public enum Motor {
	ELEVATOR(10),
	WRIST(20);

	public final int motorId;

	Motor(int motorId) {
		this.motorId = motorId;
	}
}
```

You can also have other methods on there just like a class. Once you get a grasp on the use of `enum`'s, it becomes clear just how amazingly powerful it is.
### Switch/Case
One last thing that makes `enum`'s powerful is the switch/case statement. This statement works on any primitive type and any `enum`. It also works on the `String` class after Java version 7 (read, any Java version you are ever going to use). Let's get into it by using a simple `int` variable.

```java
int myVariable = 1;
switch(myVariable) {
	case 0:
		System.out.println("That's a big fat zero!");
		break;
	case 1:
		System.out.println("Woo! We're number 1!");
		break;
	case 2:
		System.out.println("Gonna be honest, just needed another entry");
		break;
	default:
		System.out.println("Everything else goes here");
		break;
}
```

This code would print `Woo! We're number 1!`.

Let's go over the individual pieces. Unlike an `if` statement, we don't put an expression that evaluates to a `boolean` inside the parentheses. We have to put a variable that is of one of the types specified above (primitive, enum, or String) instead. Inside, you have the `case` statements. These are kind of a weird syntax because basically nothing else works like this.

We have `case <value>:` for each value we want to compare against. The `<value>` here is just a placeholder for that value and it has to be of the same type as whatever is in the parentheses of the switch statement. In our case, `myVariable` is an `int`, so all of the values we compare against are of the `int` type. 

Java will match the first one it finds and run the code inside. Notice how there's no brackets for the case statements but there is for the switch statement holding it all. This is one of the oddities about it. At the end of each case statement, there's a `break;`. This is just like a break in a loop, but it's a break out of the switch statement. Let's look at an example without break:

```java
int myVariable = 1;
switch(myVariable) {
	case 0:
		System.out.println("That's a big fat zero!");
	case 1:
		System.out.println("Woo! We're number 1!");
	case 2:
		System.out.println("Gonna be honest, just needed another entry");
	default:
		System.out.println("Everything else goes here");
}
```

This would print:
```
Woo! We're number 1!
Gonna be honest, just needed another entry
Everything else goes here
```

This is called "falling through" a case statement. You can even do multiple case statements this way:

```java
String headsOrTails = "t";
switch(headsOrTails) {  
    case "h":  
    case "H":  
        System.out.println("You picked heads!");  
        break;  
    case "t":  
    case "T":  
        System.out.println("You picked tails!");  
        break;  
    default:  
        System.out.println("That is not valid input");  
}
```

This would print `You picked tails!`.

The last thing to point out is the `default` case. This is, by convention, always the last item in the switch statement. It's what gets called if nothing else matches. It's not required, but it is generally encouraged.

Just for completeness, this is how we'd use it with our fan speed enum:
```java
FanSpeed fanSpeed = FanSpeed.HIGH;  
switch(fanSpeed) {  
    case LOW:  
        System.out.println("Low and slow, just a nice breeze");  
        break;  
    case MEDIUM:  
        System.out.println("Middle of the road huh?");  
        break;  
    case HIGH:  
        System.out.println("Going turbo speed!");  
        break;  
}
```

A switch case statement is powerful and a more condense way to write some `if` statements to make them easy to read once you're used to the syntax. It's definitely not something to use everywhere.