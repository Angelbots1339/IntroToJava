# Lesson 08: Exceptions, what could go wrong?
An exception is when something... unexpected happens. An error, one that will absolutely crash your program if not handled.

Let's crash a program.
###### Main
```java
int x = 5 / 0;
```

If you run this code, you'll get a lovely crash:
```
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at org.angelbotics.i2j.Main.main(Main.java:5)
```

This is called a "stack trace". Let's break it down. The `in thread "main"` part refers to the thread that's running our code. We only have one and it's called `main`. Threads are a separate topic which we'll cover later.

`java.lang.ArithmeticException` is the fully qualified path to the exception. What comes after the colon is information about the exception. `ArithmeticException` most often happens with a divide by zero and that's what we see: `/ by zero`.

Every line after that is part of the "stack trace" as well. You'll see a bunch of lines that start with `at`.  Each of these lines is a specific method, file, and line number. `org.angelbotics.i2j.Main` is our fully qualified class name. `main` is the name of the method in that class. `(Main.java:5)` is the name of the file (which has to match the class, so not super useful in almost all cases) and the line number, in this case `5`. That means the 5th line on that file is what threw the exception.

With this information, you can try to think through how you ended up in this situation. In our case, it's pretty obvious. Stack traces can be powerful tools to navigate and figure out errors, but sometimes you need to debug things by trying different values, stepping through with a debugger, etc. There's lots of ways to debug things.
### When to use exceptions
"Exceptions should be used in exceptional circumstances". Exceptions indicate that something is really wrong. They should only be used in places where something is wrong with your code. For example, in the `Rational` class, if the user passed in a denominator, you would get a `ArithmeticException` at some point. We could have thrown that exception ourself in the constructor:
###### Rational.java
```java
public class Rational {
	public Rational(int numerator, int denominator) {
		if(denominator == 0) {
			throw new ArithmeticException("denominator cannot be 0");
		}
	}
}
```
###### Main
```java
Rational r = new Rational(1, 0);
```

If that code ran, we would get:
```
Exception in thread "main" java.lang.ArithmeticException: denominator cannot be 0
	at org.angelbotics.i2j.Rational.<init>(Rational.java:6)
	at org.angelbotics.i2j.Main.main(Main.java:5)
```

Let's look at the `throw` call first. `ArithmeticException` as a class that extends `RuntimeException` which in turn extends `Exception` which in turn extends `Throwable` which in turn implements `Serializable`. Really though we're only going to cover going down to `Throwable` in this assignment, any base classes above that don't really interest us.

We use the `new` keyword because we're making a new instance of the `ArithmeticException` class. We pass in our own string for the message we want to see in the stack trace. This should be informative enough to get the programmer started as they attempt to debug the problem.

We `throw` the instance of this class on the same line as we create the instance. Any instance of a class that extends `Throwable` can be an argument for the `throw` keyword.

In our stack trace, we see two lines now that start with `at`. The top most line is where the exception originated. In this case, we threw the exception in the `Rational` class constructor, so that is the first line. `<init>` here just means it's the constructor. The next line is our `main` method which is where we tried creating this messed up `Rational`.

These stack traces can get very VERY long. With FRC, it will be most helpful to figure out where your code is in that stack trace, since that is almost definitely where the mistake actually is.
### Checked vs Unchecked
An exception can be considered checked or unchecked. We've only shown unchecked exceptions so far. Anything that extends `RuntimeException` is an unchecked exception. A checked exception is anything else that extends `Throwable` aside from the `RuntimeException`. 

All checked exceptions have to be declared. For example, `FileNotFoundException` is an exception that can be thrown when a file isn't... found. Very descriptive. It extends `IOException` (input/output exception) which extends `Exeption`. Since `RuntimeException` isn't in there anywhere, it's a "checked" exception and we have to declare it:
```java
public void myMethod(String filePath) throws FileNotFoundException {
	// Code here that interacts with a file
}
```

If the `filePath` parameter references a file that does not exist, we can throw the `FileNotFoundException`. This will interrupt the flow of `myMethod` and will not execute anything else in that method. The calling method will have to deal with this exception by either declaring it itself (adding the `throws FileNotFoundException` to its signature) OR by using a try/catch block (described below).

In general, we try to avoid making our own exceptions that extend `RuntimeException` because you don't declare them on a method like you do on a checked exception and that declaration better helps people know what could possibly go wrong when calling your method.

### Try/Catch/Finally
Failure hurts, especially when it crashes your program. Sometimes though, it may be useful to be able to handle an exception and do something else. Let's look at two methods:
```java
public static void main(String[] args) {  
    try {  
        System.out.println("This WILL print");  
        thisWillFail();  
        System.out.println("This will never print");  
    } catch (FileNotFoundException e) {  
        System.out.println("Oh no! Something happened!");  
    } finally {  
        System.out.println("Finally, we got here!");  
    }  
    System.out.println("This will also print");  
}  
  
public static void thisWillFail() throws FileNotFoundException {  
    throw new FileNotFoundException("I didn't bother checking for a file ;p");  
}
```

Our output would look like:
```
This WILL print
Oh no! Something happened!
Finally, we got here!
This will also print
```

Follow through the output and compare it with the code to understand it a little better and understand the order that things happen in.

Some important things to note:
- Execution immediately goes to the relevant `catch` statement and skips over anything else in the `try` section.
- The `finally` section ALWAYS runs, whether there's an exception or not. Very useful if you need to make sure to clean up some state whether there was an exception or not. You can return out of the `try` or `catch` and the `finally` would still run. `finally` is optional, too.
- You can throw a new exception or the same caught exception inside a `catch` statement. For example, you could write `throw e` inside the catch statement for `FileNotFoundException` and declare `throws FileNotFoundException` on your `main` method. This can be useful when you need to do something based on an exception, but still let someone above you know.
- You can declare multiple `catch` blocks between the `try` and the optional `finally`. The first one to be the correct variable type (ie the exact same class or one of the base classes) is the one that will be run. Only one `catch` block will ever run for a given `try`. This doesn't mean you can't hit a different exception when you run through the `try` block a second time, just that it won't ever move from one `catch` to another.