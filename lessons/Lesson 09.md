# Lesson 09: Generics
Generics were introduced in Java 5 with the intention of improving code quality.

In Java, there are primitives and objects. You've seen how classes can extend from another class. One thing to note is that EVERY SINGLE CLASS in Java extends from `java.lang.Object`. Primitive types don't extend from anything but they also can't be used at all with Generics. We'll go over how you can get around that later in this lesson.

Generics are most often used with data types such as `List`. If you wanted to make your own `List` class, think about how you might implement the add method.
###### List.java
```java
public class List {  
    public void add(Object item) {  
        // Logic goes here  
    }  
}
```

This makes sense to a degree, we want our `List` to be able to support any type. Granted, it won't support primitives, but let's ignore that for now. We do have a small problem though in that a user can add objects of different types. In fact, any user of our `List` is going to need to inspect each element to make sure it's the right one before accessing the elements.

It would be very convenient if we could say "I would like a List of T type". That's exactly the problem generics aim to solve in Java.

Note: In all of these examples, I'm going to be using a class called `MyClass`. It is an empty class simply defined as:
###### MyClass.java
```java
public class MyClass {  
}
```
## ValueHolder example
Let's say we want to start with a completely useless example, the `ValueHolder` class:
###### ValueHolder.java
```java
public class ValueHolder<T> {  
    private final T instance;  
  
    public ValueHolder(T value) {  
        instance = value;  
    }  
  
    public T getInstance() {  
        return instance;  
    }  
}
```

We have all of the normal aspects of our class definition here except for the `<T>` there after the class name. This is a generic type declaration. What we're saying that ValueHolder is using the generic type `T`. From this point on, anywhere in this class, `T` can be used as a substitute for a type. Anywhere you could specify a type, you can now specify `T` instead.

We see that in a few places in the class, `T` is the type of our `instance` field. `T` is also the type of the constructor parameter `value`. And finally `T` is the return type of our `getInstance()` method.

For any given instance of `ValueHolder`, `T` will be the same throughout that instance. Once you've created an instance of `ValueHolder` with a given type, you cannot change the type for that instance. You can however create a new instance assigned to a new variable with a different type.

Let's look at an example:
```java
MyClass myClass = new MyClass();  
ValueHolder<MyClass> valueHolder = new ValueHolder<>(myClass);
```

We didn't have to create the `myClass` variable and could have just done `new MyClass()` in place of `myClass` on the second line. But I thought this read a little better.

The left side type of `valueHolder` is `ValueHolder<MyClass>`. Notice the `<` and `>` again. This time, instead of surrounding the letter `T`, they surround an actual type. For this `valueHolder`, `T` will always and forever be `MyClass`.

On the right side, we have `new ValueHolder<>(myClass)`. Java is nice in that we don't have to specify the type twice, so we just use `<>` instead of `<MyClass>` on the right side. Note that the opposite DOESN'T work. For example, you can't do:
```java
ValueHolder<> valueHolder = new ValueHolder<MyClass>(myClass);
```

Since `myClass` is an instance of `MyClass`, the `T` for this instance is `MyClass`, and the first (and only) constructor parameter for `ValueHolder` is of type `T`, then Java lets us pass `myClass` in to the `ValueHolder` constructor.

While the `ValueHolder` class type is useless in practice, it hopefully demonstrates the concept of replacing the `T` type with whatever your class type is.
## Method overloading
You do have to be a little careful with method overloads. In the event you have to methods with the same name, one with a generic type parameter and one that's "specialized" or with a specific type specified. Case in point, our `MethodOverloadExample` class:
###### MethodOverloadExample.java
```java
public class MethodOverloadExample<T> {  
    public void doStuff(T value) {  
        System.out.println("Called with value!");  
    }  
  
    public void doStuff(MyClass myClass) {  
        System.out.println("Called with myClass!");  
    }  
}
```

If in our Main method, we write this code:
```java
MyClass myClass = new MyClass();  
MethodOverloadExample<MyClass> methodOverloadExample = new MethodOverloadExample<>();  
methodOverloadExample.doStuff(myClass);
```
We'll get this lovely compiler error:
```
java: reference to doStuff is ambiguous
  both method doStuff(T) in org.angelbotics.i2j.MethodOverloadExample and method doStuff(org.angelbotics.i2j.MyClass) in org.angelbotics.i2j.MethodOverloadExample match
```

What this is telling us is that the compiler has no idea whether to call the `doStuff` method with the `T` parameter or the one with the `MyClass` parameter. It really can't tell the difference! If the type `T` was something other than `MyClass`, this would work just fine.

## Generic Methods
Sometimes, you don't want a generic to work on an entire class but only inside a particular method. You can actually apply a generic type to only a single method instead of an entire class.
###### GenericMethodExample.java
```java
public class GenericMethodExample {  
    public <T> void genericMethod(T instance) {  
        // Do something with the instance  
    }  
}
```
###### Main Method
```java
MyClass myClass = new MyClass();  
GenericMethodExample genericMethodExample = new GenericMethodExample();  
genericMethodExample.genericMethod(myClass);
```

First things first, you'll notice that the `GenericMethodExample` class does not have the `<T>` meaning it's not using generics. Instead, the method `genericMethod` has the `<T>` in front of the return type (in this case `void`, but we can actually return type `T` there as well) and has the `T` type as the parameter for the method.

The second thing to notice is that our main method code doesn't have any `<` or `>`. The `genericMethodExample` variable has no generic type because the `GenericMethodExample` class itself doesn't specify it needs one with `<T>` after the class name in the class definition. We also don't need it when calling the method, because Java infers the type for us.

Being able to do this may not seem super useful, but it can become extremely powerful. The easiest way to see this is if our `genericMethod` actually needed two arguments with two rules:
- We don't care what the types are
- We need them to be the same type

With generic methods, that's easy:
###### GenericMethodExample.java
```java
public class GenericMethodExample {  
    public <T> void genericMethod(T first, T second) {  
        // Do something with first and second
    }  
}
```

### Static Generic Methods
If the generic is on the class, you cannot use the generic type in a static method. For example, this is invalid:
###### BadStaticMethodExample
```java
public class BadStaticMethodExample<T> {  
    public static void genericMethod(T instance) {  
        // Do something with the instance  
    }  
}
```

It also comes with a lovely error message on the `T` type for the `instance` parameter in `genericMethod`:
```
'org.angelbotics.i2j.BadStaticMethodExample.this' cannot be referenced from a static context
```

Basically, it's telling you that there's no way to reference `T` because that only  makes sense on instances of a class and using a `static` method on an instance doesn't really make sense. In summary, it just doesn't let you.

You can, however, have generic methods be static if the generic is defined on the method itself:
```java
public class GenericMethodExample {  
    public static <T> void genericMethod(T instance) {  
        // Do something with the instance  
    }  
}
```

And using it works just like any other generic or static method:
```java
MyClass myClass = new MyClass();  
GenericMethodExample.genericMethod(myClass);
```

## Bounded Generics
Generic types are useful in a lot of data structure contexts, where you want to specify you have a data structure of some type. Sometimes it's helpful to be able to restrict what types you're willing to work with, however.

In this section, I'm going to introduce two knew interfaces: `CanDrive` and `CanFly`. They are defined as follows:
###### CanDrive.java
```java
public interface CanDrive {  
    void drive();  
}
```
###### CanFly.java
```java
public interface CanFly {  
    void fly();  
}
```

### Runway Example
If we had a `Runway` class whose purpose was to let an aircraft takeoff, we could define it like this:
```java
public class Runway {  
    public <T extends CanFly> void takeoff(T aircraft) {  
        aircraft.fly();  
    }  
}
```

Instead of our normal `<T>`, we have `<T extends CanFly>`. You may be thinking "wait a second, `CanFly` is an interface and we use `implements` with interface!" and you'd be absolutely correct. Literally everywhere but here, that is. In specifying a generic type, you use `extends` whether it's an interface or another class. Why? Uh. Reasons. Unfortunately it's in the category of "please accept it and move on". Sorry. :(

We still specify the `T` type as the `aircraft` parameter. Notice how we can say `aircraft.fly()` in the method body. This is because Java knows that anything we pass in MUST implement the `CanFly` interface. Since `CanFly` has a `fly()` method, we're allowed to call that method inside our `takeoff` method.

Notice we're using the generic method version here instead of the generic class. This is entirely based on how this class might get used. If we had a Runway dedicated to each type of aircraft we might have, it might make sense to use the generic class. Here, we're going to have one runway instance. Maybe we're writing code for a small airpot and it doesn't have the room for one airport per type. The point is, there's no hard and fast rule on why I used this particular version here, it just made the most sense for this example.

### Flying Car Example
For years, science has failed in providing us with flying cars. Luckily as programmers we can just make our own:
###### FlyingCar.java
```java
public class FlyingCar implements CanDrive, CanFly {  
    @Override  
    public void drive() {  
        System.out.println("VROOM VROOM!");  
    }  
  
    @Override  
    public void fly() {  
        System.out.println("I can FLY!");  
    }  
}
```

Notice that we implement two interfaces in this class, both `CanDrive` and `CanFly`. They're separated by commas here. If we had an instance of `FlyingCar`, we could pass it to the `takeoff` method of our `Runway` since an instance of `FlyingCar` is guaranteed to implement `CanFly`.
### Multiple Bounds
What if our runway only supported flying cars. Well, we could do this in one of two ways. The first is by having our generic type `T` extend `FlyingCar`:
```java
public class Runway {  
    public <T extends FlyingCar> void takeoff(T flyingCar) {  
        flyingCar.drive();  
        flyingCar.fly();  
    }  
}
```

The problem comes when our code gets more complicated. Someone may want to implement `CanFly` and `CanDrive`, but they may NOT want to extend from your `FlyingCar` class. We can specify we want a type that implements both interfaces like this:
```java
public class Runway {  
    public <T extends CanDrive & CanFly> void takeoff(T flyingCar) {  
        flyingCar.drive();  
        flyingCar.fly();  
    }  
}
```

This is the answer to the problem presented by interface segregation presented in Lesson 06. It's totally okay to separate interfaces if you can specify that we accept a type that implements all of those interfaces. This isn't used super often, but it's sort of the perfect tool for the job when it's needed.
## Autoboxing
Remember when I said you couldn't use generics with primitive types? I didn't lie per say. I just didn't mention that there are classes that match the primitive types. For example, the primitive type `int` has a class `java.lang.Integer` that represents basically the same thing.

Let's look at a `Main` class:
###### Main.java
```java
public class Main {  
    public static void main(String[] args) {  
        doStuff(5);  
        doStuff(5.3);  
    }  
  
    public static <T> void doStuff(T value) {  
        System.out.println(value.getClass());  
        System.out.println(value);  
    }  
}
```

When run, this would output:
```
class java.lang.Integer
5
class java.lang.Double
5.3
```

Note that `getClass()` returns the type `Class<?>` which requires understanding wildcard generics to fully understand. You don't need to understand that at this time, we're just using it to print the type out.

We get the `java.lang.Integer` type when we passed `5` in. But wait, `5` as an `int` not an `Integer`. Well, Java does something called "autoboxing". When converting from a primitive to a class that matches (eg from an `int` to an `Integer`) we are "boxing". When converting back, it's "unboxing".

Autoboxing allows us to do things like pass in the primitive type directly into a method that accepts a generic type. It will automatically box and unbox as necessary, though this incurs a small performance hit.

This is how we can use primitive types with generic classes, such as our `ValueHolder` from earlier:
```java
ValueHolder<Integer> myValueHolder = new ValueHolder<>(42);
```
## Multiple Generic Types
We can also specify we want multiple Generic Types too:
```java
public class Map<K, V> {
}
```

Here both `K` and `V` are types just like `T` in the examples before. This just means that our class uses two generics. We create it just like before, just specifying the types as comma separated.
```java
Map<Integer, MyClass> myMap = new Map<>();
```

Everything else we've gone over such as binding the types works with specifying multiple generic types.
## Generic names
We've been mostly using `T` for the "Type" in a generic, but really it just follows the same rules as a class name. There's a list of suggestions on this page https://docs.oracle.com/javase/tutorial/java/generics/types.html

- E - Element (used extensively by the Java Collections Framework)
- K - Key
- N - Number
- T - Type
- V - Value
- S,U,V etc. - 2nd, 3rd, 4th types

These are helpful to know but you shouldn't feel required to memorize them. They're more or less guidelines to quickly communicate to other programmers your intent.

## Advanced: Wildcard generics
Wildcards are probably the most complicated to understand. If you're very very lost, don't try to read this section yet. Give the other time stuff to make sense inside your brain. They're used inside the Java framework sometimes so it's helpful to recognize them, but it's not often I've found that they're actually required.

Let's start by using our `ValueHolder`, `CanFly`, and `FlyingCar` classes from earlier and look at this main class:
```java
public class Main {  
    public static void main(String[] args) {  
        FlyingCar flyingCar = new FlyingCar();  
        ValueHolder<FlyingCar> flyingCarValueHolder = new ValueHolder<>(flyingCar);  
        doStuff(flyingCarValueHolder);  
    }  
  
    public static void doStuff(ValueHolder<CanFly> aircraftHolder) {  
        aircraftHolder.getInstance().fly();  
    }  
}
```

If we try to compile this, we'll get an error. This is because while `FlyingCar` implements `CanFly`, this does not mean `ValueHolder<FlyingCar>` is of the type `ValueHolder<CanFly>` or that it's a subclass of that type. There's several reasons for this, the main one being that it might allow unexpected mixing of classes. If you want to allow this, you can replace the `doStuff` method in one of two ways.

The first, you may already be able to guess at:
```java
public static <T extends CanFly> void doStuff(ValueHolder<T> aircraftHolder) {  
    aircraftHolder.getInstance().fly();  
}
```

The second is where wildcards come into play:
```java
public static void doStuff(ValueHolder<? extends CanFly> aircraftHolder) {  
    aircraftHolder.getInstance().fly();  
}
```

Notice how we don't have the template type `T` anymore anywhere. We instead change the generic of `ValueHolder` to be `<? extends CanFly>`. That question mark means "I don't care to have this be named" and it's totally valid as long as whatever is passed in implements the `CanFly` interface.

You can also do the inverse and say that whatever is passed in must have a generic that is a base class of a specific type by using `super`, such as `? super FlyingCar`. For example, if our `doStuf` method was:
```java
public static void doStuff(ValueHolder<? super FlyingCar> aircraftHolder) {  
    aircraftHolder.getInstance().fly();  
}
```
We'd get the syntax right but our code wouldn't compile. This is because while `FlyingCar` has a `fly` method (from the `CanFly` interface), `Object` is a base class of `FlyingCar` and does not have that method.

### Advanced advanced: How super/extends wildcards can be used
One place where you'll see both of these used in the same place is when we get to functional programming in Java. For example, the `java.util.function.Function` interface is defined as `Function<T, R>`. This is just like a math function you may have seen in Algebra like `f(x)`. In Algebra, that `x` and what it evaluates to are both numbers, but in programming they can be any type. The input type, `x` in our `f(x)` case is the type `T` and `R` is the type of whatever `f(x)` evaluates to.

Let's add a method to our `ValueHolder` class called `convert`. It will convert from a holder of one type to a holder of another.
```java
public <R> ValueHolder<R> convert(Function<? super T, ? extends R> conversionFunction) {  
    return new ValueHolder<>(conversionFunction.apply(instance));  
}
```

Here we're mixing generic methods and generic classes. Our `ValueHolder` is of type `T`, and this `convert` method uses the generic type `R`. Note that this is just matching the convention and isn't exactly the same `T` and `R` in the `Function` interface.

The `? super T` part means that the input to our function must be the same class or a super class for whatever the `T` for this instance of `ValueHolder` is. If you think about it, this makes sense. We need to be guaranteed that it can work with whatever we pass in. If this was `? extends T` instead, then someone could make a `Function` that called a method on a subclass of whatever our `T` was. For example, if we had a `ValueHolder<CanFly>` and someone was allowed to pass in a function of type `Function<FlyingCar, CanDrive>`, then they could call the `drive` method because `FlyingCar` has a `drive` method. We could also have limited it to just `T` but unless there's a good reason to, it's better to give the consumers of your code more flexibility.

Next up, we have the `? extends R` part. This is useful to the consumer of our `convert` function because they can return a type and then immediately cast that to a super type or interface. This one's a little harder to explain so I'm going to use some code.
###### Main Method
```java
FlyingCar flyingCar = new FlyingCar();  
ValueHolder<FlyingCar> flyingCarValueHolder = new ValueHolder<>(flyingCar); 
Function<FlyingCar, FlyingCar> function = (fc) -> fc;
ValueHolder<CanFly> canFly =  flyingCarValueHolder.convert(function);  
ValueHolder<CanDrive> canDrive =  flyingCarValueHolder.convert(function);
```

Note that `(fc) -> fc` is a lambda which we'll be covering next lesson. For now, it's useful to know that this is an instance of `Function<FlyingCar, FlyingCar>`. With the `? super T`, part of our type hint in the `Function` parameter of the `convert` method, we satisfy it by just being the same type. ie our `flyingCarValueHolder` is a `ValueHolder<FlyingCar>`, our `T` there is `FlyingCar` and `FlyingCar` is a `FlyingCar` so it's satisfied.

With `? extends R`, it's harder to understand. The Java compiler sees that we're assigning to `ValueHolder<CanFly>` but our function returns a `FlyingCar` as its return type. If we had just type hinted `R`, Java would only let us return a `ValueHolder<FlyingCar>` and that would mean we couldn't assign it to `ValueHolder<CanFly>` or `ValueHolder<CanDrive>`. We would have been told "Incompatible equality constraint: CanFly and FlyingCar" when trying to assign it to an instance of `ValueHolder<CanFly>`.

However, by saying `? extends R`, we're giving the implementer of our `conversionFunction` more leverage. As long as whatever the `conversionFunction`'s return type is IS an `R` for the generic `R` in our `convert` method, we'll accept it.

Frankly, this is so complicated that every time I have to implement it, I have to think through it again. There's even terms related to it: Covariant, Contravariant, and Invariant. The `? extends T` is a covariant type, the `? super R` is a contravariant type, and just using `T` or `R` is invariant. And yes, I have to look those up each time.

The reality is, the actual use of this usually works out and you don't have to understand this to this level of depth. When we get to lambdas, most of the time the types will just work out without having to think too heavily on it.
## Further Reading
One thing I don't want to cover here is "type erasure". It's useful to know, but I think a little advanced for this topic.

Feel free to check out this page on Java generics for more information on type erasure and other topics covered here. https://www.baeldung.com/java-generics