# Lesson 10: Lambdas
A lambda in Java is a shorthand notation for writing a method. Much like any other method, it takes parameters in, has a body, and can either have a return type or return nothing.

Let's look at a method:
```java
public static int square(int x) {  
    return x * x;  
}
```

It's pretty simple overall. It takes a single `int` parameter in called x and returns an `int` that is the value of `x` squared. We can call it by passing an `int` into the method. e.g. `square(2)` would return 4.

Lambdas are very similar, but return an instance of `Function`. Let's look at a lambda:
```java
Function<Integer, Integer> square = x -> x * x;
```
The `Function<Integer, Integer>` is just the type of the `square` variable. The `x -> x * x` is the lambda. The `x` on the left side of the `->` (arrow) is our parameter. You may be wondering how we know what type the `x` is as a parameter. The answer is in the first generic argument of `Function`: `Integer`. Remember that we can't have a primitive type in a generic, but due to autoboxing, we can use `Integer` instead of `int`.

The cool part to see here is that Java figured out what the parameter and return type should be simply from the variable declaration, not from the lambda itself. This is an extremely powerful technique and means you can can use lambdas in all sorts of places. For more info about how this works in Java's type system, see the previous lesson and the generic wildcards section.

The `x * x` is the body of the lambda, just like the body of our `square` method. Notice there's no return statement here. Since `x * x` produces a value, Java just assumes we meant to return that value from our `lambda`.

To call our function, we call the `apply` method on it. e.g. `square.apply(2)` would return 4.
## A lambda is really an anonymous class implementation of an interface
Alright I'm going to get the big lie out of the way now. Lambda's in Java are actually anonymous classes that implement an interface with a single method. It's one of the few places where I feel the implementation details actually help erode some of the mystery.

To explain this, I'm going to take each piece of this one step at a time.
### Anonymous classes
In Java, an anonymous class is one without a name. Sometimes classes are so... focused on handling one particular thing that it doesn't even make sense to name them. Let's make an interface called `HasTwoMethods`:
###### HasTwoMethods.java
```java
public interface HasTwoMethods {  
    void methodA();  
    int methodB();  
}
```
###### Main Method
```java
HasTwoMethods instance = new HasTwoMethods() {  
    @Override  
    public void methodA() {  
        System.out.println("I'm an anonymous class");  
    }  
  
    @Override  
    public int methodB() {  
        return 5;  
    }  
};
```

Okay, so remember when I said you can't instantiate interfaces? I didn't lie, exactly. What we're doing here is creating an anonymous class. Everything is just like a class with a couple of exceptions. The first is we have `new HasTwoMethods()` instead of `class SomeClassName implements HasTwoMethods`. Note that `SomeClassName` is just an example. Because it's an anonymous class, it has no name. The second is we have a semicolon at the end of the class, because we're finishing the assignment statement.

Now, if we run `instance.methodA()`, it will print "I'm an anonymous class" and if we run `instance.methodB()`, it will return `5`.

Anonymous classes also "capture" variables declared in the same context they're declared in, but that is a little more complicated to understand so I'm going to skip over it for now.
### Single method interfaces
Let's look at a new interface and main method.
###### HasSingleMethod.java
```java
public interface HasSingleMethod {  
    void doAThing();  
}
```
###### Main Method
```java
HasSingleMethod instance = new HasSingleMethod() {  
    @Override  
    public void doAThing() {  
        System.out.println("I did a thing!");  
    }  
};
```

Okay, so we can make an instance that implements the `HasSingleMethod` interface. If we executed `instance.doAThing()`, we'd see "I did a thing!" printed to the screen.

Now, the second you write the code for that main method, your IDE may suggest something like "Anonymous new HasSingleMethod() can be replaced with lambda". If you did agree with that suggestion, the code would look like:
```java
HasSingleMethod instance = () -> System.out.println("I did a thing!");
```

The `()` is just an empty parameter list. In fact, only a single parameter can do without the parenthesis there. If doing no parameters or more than one, you MUST use the parenthesis. On the right side of the arrow, we call a method that returns nothing (void return type) but prints to the screen. This all is totally fine with Java since our `doAThing` method takes no parameters and returns nothing.

### Putting it all together
Imagine you had a function in your Main file that accepted a `HasSingleMethod` instance:
```java
public static void doSomethingInteresting(HasSingleMethod hasSingleMethod) {  
    hasSingleMethod.doAThing();  
}
```

We can pass a lambda anywhere this interface is expected:
```java
doSomethingInteresting(() -> System.out.println("I did a thing!"));
```

This is actually what allows the `Function` interface to work in the first place. The important part of the interface is just this:
```java
public interface Function<T, R> {
	R apply(T t);
}
```

Since it's a single method interface, Java lets us use a lambda by creating an anonymous class under the hood that implements this interface. It's all syntactic sugar meaning it exists to make something easier to express or read.
## Multi-lined body
Sometimes, you want to run multiple lines inside a lambda. That's perfectly fine and can be done with `{` and `}` just like in a method. For example, given our `doSomethingInteresting` method earlier, we could do:
```java
doSomethingInteresting(() -> {  
    System.out.println("I did a thing!");  
    System.out.println("I did another thing!");  
});
```

Everything else stays exactly the same.
## Method reference
Sometimes you have a method on a class that already handles exactly what you want it to. Let's look at a Main file:
###### Main.java
```java
public class Main {  
    public static void main(String[] args) {  
        Function<Integer, Integer> functionSquare = Main::square;  
        System.out.println(functionSquare.apply(2));  
    }  
  
    public static int square(int x) {  
        return x * x;  
    }  
}
```

Notice we have a `square` method again that's static. When calling a static method, we'd do something like `Main.square(2)` or just `square(2)` since we're already inside the `Main` class. Using `::` is a method reference. It's just like a lambda except we're saying "we've already written something that matches the parameters and return type you expect, so here it is".

It doesn't matter here that `square` accepts an `int` and returns an `int`, but `Function` uses the `Integer` generics, once again due to autoboxing.

This also works on an instance of a class. Let's look at the new `MyNumber` class and a new main method:
###### MyNumber.java
```java
public class MyNumber {  
    private final int value;  
  
    public MyNumber(int value) {  
        this.value = value;  
    }  
  
    public int multiply(int otherValue) {  
        return this.value * otherValue;  
    }  
}
```
###### Main Method
```java
MyNumber number = new MyNumber(3);  
Function<Integer, Integer> functionSquare = number::multiply;  
System.out.println(functionSquare.apply(2));
```

This would print out `6`. Notice that you can use any fields inside the class, which makes this a powerful technique. Also note that instead of using the class name like before, we use the variable `number` in the method reference.
## Function/Supplier/Consumer
We've gone over `Function` and shown what that interface looks like. I'd like to go over a few more now.
### Supplier
As the name says, it supplies a value. It takes no parameters and returns a value of some type. The interface looks like:
```java
public interface Supplier<T> {
	T get();  
}
```

Suppliers are used a lot in FRC programming as a way to separate the code that generates certain data (such as desired robot heading) from the code that needs that information. The code that needed the values could have an instance of `Supplier`. By calling the `get()` method, they know they're going to get a value back of the specified type.
### Consumer
The consumer consumes a value and returns nothing. It looks like this:
```java
public interface Consumer<T> {
	void accept(T t);
```

This can be useful for the inverse, where you have some data you want to give to someone else, but you don't want to know much about them. If they provide to you an instance of `Consumer`, you can call the `accept()` method and give them whatever data you have as a parameter.

Consumer and Supplier are two sides of the same coin and which one you use really just depends on if the data is updated whenever requested (Supplier) or as new data comes in (Consumer).
## Advanced: Variable capture
I mentioned earlier that anonymous classes do something called variable capture. Let's revisit a slightly modified main method example from earlier:
###### Main Method
```java
int x = 5;  
HasTwoMethods instance = new HasTwoMethods() {  
    @Override  
    public void methodA() {  
        System.out.println("We have " + x);  
    }  
  
    @Override  
    public int methodB() {  
        return x;  
    }  
};
```

Notice the `x` up top? Well we're using it in our anonymous class. This means that `x` was "captured" by the anonymous class. One thing to note is that `x` becomes `final` effectively.

Let me explain "effectively" there. If you added `x = 6` to the end of that code, you wouldn't see that line light up with an error since `x` isn't actually final. However, the `x` captured inside the anonymous class of `HasTwoMethods` really doesn't like that you can just modify `x` out from under it. The error you'll get is "Variable 'x' is accessed from within inner class, needs to be final or effectively final".

The `inner class` part just refers to the fact that we're defining one class inside another (in this case the anonymous class inside the `Main` class). If we were to change the first line to `final int x = 5;`, then our error would move to the `x = 6` line as expected. This is what "effectively final" refers to. When we didn't modify `x` anywhere, the Java compiler was fine with just assuming `x` was final. When we tried modifying it anyway, it decided to complain.

This does change a little when your captured variables are fields. Let's look at an example with a static field:
###### Main.java
```java
public class Main {  
    static int x = 5;  
  
    public static void main(String[] args) {  
        HasTwoMethods instance = new HasTwoMethods() {  
            @Override  
            public void methodA() {  
                System.out.println("We have " + x);  
            }  
  
            @Override  
            public int methodB() {  
                return x;  
            }  
        };
		instance.methodA();  
		x = 6;  
		instance.methodA();
    }  
}
```

This would output:
```
We have 5
We have 6
```

This doesn't make a ton of sense at first, but has a lot to do with how variables are referenced and their lifecycle. Essentially, the Java compiler can always guarantee it will be able to access this field so it lets you do whatever you want with it.

This also works with non-final non-static fields.
###### MyDemo.java
```java
public class MyDemo {  
    public int value;  
    public HasTwoMethods instance;  
  
    public MyDemo(int otherValue) {  
        this.value = otherValue;  
        instance = new HasTwoMethods() {  
            @Override  
            public void methodA() {  
                System.out.println("We have " + value);  
            }  
  
            @Override  
            public int methodB() {  
                return value;  
            }  
        };  
    }  
}
```
###### Main Method
```java
MyDemo demo = new MyDemo(5);  
demo.instance.methodA();  
demo.value = 6;  
demo.instance.methodA();
```

This would give us the same output as above. Notice that we made the constructor parameter value for `MyDemo` to be named `otherValue` instead of `value`. If it was just `value`, then the `value` that would have been captured by the anonymous class would be the parameter named `value` and not the field named `value`.

## Advanced: Accessing the outer class `this`
Let's look at `MyDemo` again, this time slightly modified:
```java
public class MyDemo {  
    public int value;  
    public HasTwoMethods instance;  
  
    public MyDemo(int value) {  
        this.value = value;  
        instance = new HasTwoMethods() {  
            @Override  
            public void methodA() {  
                System.out.println("We have " + MyDemo.this.value);  
            }  
  
            @Override  
            public int methodB() {  
                return MyDemo.this.value;  
            }  
        };  
    }  
}
```

Now, we kept the parameter name as `value`. To make sure we're referencing the field `value` inside our anonymous class, we use `MyDemo.this.value`. This special syntax only works inside an inner class, which is what anonymous classes are. If we just used `this`, it would refer to the `this` of the anonymous inner class. If we use `MyDemo.this`, we're referring to the `this` of the `MyDemo` class instance we're currently being defined inside.

Confusing? A little. But hey, that's why it's in an advanced section.