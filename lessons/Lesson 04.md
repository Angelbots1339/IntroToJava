Java is an Object Oriented Programming language. Object Oriented Programming or OOP is a way of thinking about code that lends itself to writing larger applications. It is also the hardest for new programmers to wrap their mind around. This lesson will be a long lesson and will cover the very basics of OOP.

Once you're able to wrap your head around these concepts, you unlock an entirely new chapter as far as abilities go. Many self taught developers write "procedural" code, where you start from the top, run through your code, and end at the bottom. Code will still run and work like that, but OOP offers more flexibility when writing code, making it easier to reason with large structures.

I have seen many developers take this step and I know that it may be difficult to grasp. It is a big step, but I know you can make it through. Just take your time, process at your own pace, and ask questions.

Let's dive in.

## Classes and Instances
In the context of school, a "class" is a period where an instructor spends time going over some content in the hopes of teaching it to you. In programming, a "class" is an entirely different beast, so please don't try to compare the two even though the name is the same. When you see the word class, unless specified otherwise, you should read that as "class in the context of OOP".

A class is a schematic that describes how an object is built. You can "instantiate" a class to get an instance of that class. Note that "instance" and "object" or more or less used interchangeably UNLESS I am talking about the special class called `Object` where I'll use a capital `O` and format it as `Object`. To attempt to reduce confusion, I will use `instance` where possible to describe something made using the class.

These schematics are extremely powerful, because you can instantiate multiple copies of the same class. For example, you might have a `Fruit` class, but an `apple`, `pear`, or `orange` instance. Each of those instances have their own data related to them.
### The Fruit class
Let's look at what creating the `Fruit` class would look like:
```java
package org.angelbotics.i2j;

public class Fruit {
	public String name;

	public Fruit(String name) {
		this.name = name;
	}
}
```

Okay, so that's a lot. Let's break it down bit by bit.
```java
package org.angelbotics.i2j;
```

This is called the package declaration. Every single class in Java must be part of a package. All of your assignments have been in the package `org.angelbotics.i2j`. I will not specify the package in each example, but it is required to be at the top of every file. It's also required to match the folder structure. The file for this class would be in the directory `org/angelbotics/i2j` relative to whatever your source directory is. In our assignments, the full path would be `src/main/org/angelbotics/i2j`.

Next up, we have `public class Fruit {`. The name of this class is `Fruit`. Notice the capital `F` in `Fruit`. Classes use Pascal Case which is similar to Camel Case except the first letter is capitalized.
- Pascal case: `MyClassName`
- Camel case: `myVariableName`

Other than that, the rest of the naming conventions for variables apply to classes as well (ie no leading digits, no symbols except `$` and `_`, etc.)

Because the class is named `Fruit`, it has to be in a file called `Fruit.java`. This is very very important and your compiler will throw a fit if you get it wrong. Many editors are nice enough to automatically change the file name for you if you change the class name, but keep it in mind just in case your editor isn't so nice to you.

You'll notice the `public` at the beginning of this line. `public` is not your only option here, you could write `class Fruit {` instead, omitting the `public`. Using `public` means "any class can access me and instantiate me". Omitting it means "only classes in the same package as me can instantiate or use me" and is called "package private". 99% of the time, you will include `public` here. We'll cover package private related things at a later time. The braces `{` here are the boundaries of the class. Everything within the matching `}` brace at the end is part of the `Fruit` class.

So much text and we've only talked about 2 lines of code. Let's make it 3:
```java
	public String name;
```

Aside from the `public` keyword here, this almost looks like a variable declaration. And honestly, that's exactly what it is. This is called a "field" in the context of a class. Each instance has its own copy of this field and can do whatever it wants to it, without affecting any other instance of the same class. The `public` keyword affects who can access this field. There are 4 options: `public`, `private`, `protected`, and omitting an access modifier. I will explain two of them:
- `public` Any code can access and modify this field on an instance of a class.
- `private` Only code inside this class can access and modify this field.

Next up, we have what's called the `constructor`. The constructor is a method that is run every time a new instances is created and does the actual construction of our schematic. Let's take a look at the constructor for our `Fruit` class:
```java
	public Fruit(String name) {
		this.name = name;
	}
```

Everything within the matching braces here is part of the constructor's body and is run every time a new instance is created.

The very first line is our constructor's signature. I will explain method/constructor signatures down below in more detail. For now, let's break this one down further:
```java
	public Fruit(String name) {
```
Here we have `public` again. This means that any other code can create an instance of this class. The constructor (and all methods really) have the same access options as a field does. You may be wondering why you'd use anything other than `public`.  Without showing a bunch of examples, that's surprisingly harder to explain. Another question you may be asking is "why would the class access and constructor access differ?" and I'm afraid that's once again a harder question to answer without examples. We'll go into it later.

We also have the class name again here. This is the method's name. If the method's name is the same as the class, then that method is called a `constructor`. That really is the only thing that makes it special and its what tells the Java compiler to treat it special.

In parenthesis, we have what is known as the "parameters" to the method. In this case, we have one parameter. It is of type String and we are calling it `name`. Something VERY VERY important to understand here is that we are only calling it `name` within the context of the constructor. Any code calling our code doesn't need to call their variable `name` as well. Even if they did, it doesn't matter as they are different depending on the context. You'll see more what I mean later if that didn't fully make sense.

Next up, we have the line:
```java
		this.name = name;
```
`this` is a special keyword inside of a class. It means "the current instance I am acting on". This (joke intended) can be a very confusing concept. You have to understand `this` in the context of the instance it is working on. For example, in our `apple` instance, `this` would only refer to the data for `apple`, and would not refer to any data for `pear` or `orange`.  In this case, we are assigning the field `name` that we declared above the value of the parameter `name` that we passed into our constructor. Using `this.name` on the left side here is important. If you had just written `name = name;`, then Java would assume this statement does nothing because it would assume that the `name` on the left is referring to the parameter passed in.

You should note that you could actually change the name of the parameter passed in, or the field name, and you would not need to use `this`:
```java
	public Fruit(String fruitName) {  
	    name = fruitName;  
	}
```

This may seem like really weird behavior, but it follows a specific set of rules. These rules are called "scoping" rules. We'll go over them later. For me, I don't mind the requirement to use `this` for something simple like the `name` of the fruit. Using `fruitName` as the parameter just feels clunkier to me. Use what works and will be understandable when another human looks at your code.

#### Instantiating the Fruit class
FINALLY let's make our instances:
```java
Fruit apple = new Fruit("Apple");
Fruit pear = new Fruit("Pear");
Fruit orange = new Fruit("Orange");
```

I'm so glad we did that, because I've been hungry this whole time and... ah crap we don't have a way to eat these. Okay, stay calm, we'll just add that feature in a little bit. For now let's explain this code.

Just like other variables, we have the declaration as the type and then the variable name: `Fruit apple` meaning a variable called `apple` of type `Fruit`.  On the right side, we create a `new` instance. The `new` keyword tells Java that you want to create an instance of the class you specify on the right side. After the `new` keyword comes the constructor. Here, we're not defining the constructor but we're `calling` it. In the `apple` instance, we pass the `String` "Apple" in as the first `argument`. Inside our constructor, the `name` has a value of "Apple" while this instance is being constructed.

Keep in mind the nomenclature:
- `Parameter` is used in the definition of a method/constructor and is named what we'd like it to be named inside that method.
- `Argument` is what is "passed into" the method from the outside.

The arguments must match the types of the parameters and be passed in the order the method expects them. We'll talk more about method signatures later. The important thing to understand here is the different perspective of "code that is calling the constructor" and "code that is inside the constructor". They're two separate contexts.

That's it for instantiation. We can use the instances like so:
```java
System.out.println("I would like to eat an " + apple.name);
System.out.println("I would like to eat an " + pear.name);
System.out.println("I would like to eat an " + orange.name);
```

This would print:
```
I would like to eat an Apple
I would like to eat an Pear
I would like to eat an Orange
```

This is because each instance has its own name. We passed in the name we wanted into the constructor as an argument when we created the instance: `new Fruit("Apple");`. Then, inside the constructor the `Fruit` constructor assigned it to the field `name`. So when we write `apple.name`, we're just getting back the parameter we passed in in the first place.

You can also use a class type anywhere you could use a primitive, for example in an array:
```java
Fruit[] fruits = {apple, pear, orange};  
  
for (Fruit fruit : fruits) {  
    System.out.println("I would like to eat an " + fruit.name);  
}
```

Here we create an array of `Fruit`. Since our `apple`, `pear`, and `orange` or all of the `Fruit` type, we can create this array with them. Next we have our for-each loop. It works exactly the same way here as it did in the previous lesson with the `int` type. Inside this loop `fruit` is the name of the variable we're using to represent whichever element of the array we're currently on. And because the `Fruit` class has a `name` field, and the `fruit` variable is a `Fruit` type (ie an instance of the `Fruit` class), we can access the `name` field for our respective fruits.

All that is a long winded way of saying the output will be the same as when we addressed them individually above.

#### Overwriting field values
We do have a slight problem here. While anyone can see our name, they can also go in and update it without calling any code inside the `Fruit` class:
```java
apple.name = "Pumpkin";
```

This isn't ideal. We can address this in a few different ways. If we NEVER need to change the `name` field, either internally or external to the `Fruit` class, we could add the `final` modifier:
```java
package org.angelbotics.i2j;

public class Fruit {
	public final String name;

	public Fruit(String name) {
		this.name = name;
	}
}
```

This is quite literally the exact same class as above except `public final string name;` instead of `public String name;`. That's the only difference. Now the compiler wouldn't even let the `apple.name = "Pumpkin"` code compile. The tradeoff here is that no code in the `Fruit` class, outside of the constructor, can modify the `name` field. Once you leave the constructor code, that field is set in stone.

Another way is using "getters and setters" which we'll cover below in the encapsulation section.

## Methods and method signatures
A `method` (sometimes I'll also use the term `function`. There's not a difference in Java) is a group of code that operates on a class and its data. Let's add a method to our `Fruit` class:
```java
public class Fruit {
	public final String name;

	public Fruit(String name) {
		this.name = name;
	}

	public void eat() {
		System.out.println("I ate a/an " + name);
	}
}
```

We can now call the `eat` method on a fruit instance:
```java
apple.eat();
```

This would output:
```
I ate a/an Apple
```

You can actually call this method multiple times across multiple instances:
```java
apple.eat();
apple.eat();
pear.eat();
```

Which outputs:
```
I ate a/an Apple
I ate a/an Apple
I ate a/an Pear
```

A method's "signature" is made up of the name of the method and the parameters it takes. In the case of our `eat` method, the name is `eat` and we accept no parameters. The reason understanding method signatures is important is because of a concept called `overloading`. And overloaded method is one where the same name is used, but the parameters are different.

As an example, say we wanted to pair eating our delicious fruit with a drink. We could add another eat method:
```java
public class Fruit {
	...

	public void eat(String drink) {
		System.out.println("I ate a/an " + name + " paired with a nice " + drink);
	}
}
```

Please note that the `...` here is NOT some special Java syntax. It's merely to save screen space and typing. What it means is "the rest of the code you've already seen is here, I just didn't type it out".

Because the parameters are different, we can call them and Java will know which method to call based on the parameters:
```java
apple.eat();
apple.eat("Coffee");
```

This would output:
```
I ate a/an Apple
I ate a/an Apple paired with a nice Coffee
```

The last thing to point out here is the `void` in the method signature. This is the method's "return type". `void` simply means that we don't return anything. We'll see an example later where we do.

Also if you've read this far, find me and out of earshot of other students tell me you read this lesson and say "I prefer Pumpkin paired with Hot Chocolate". I'll give you candy. :) Don't let the other students hear you though because otherwise people will get candy for no work and that makes me sad. :(
### Pass by reference vs value
One thing I do need to bring up is "pass by reference" vs "pass by value". It's honestly pretty simple. All primitive types are passed by value, meaning they are copied into your function. For example:
```java
public static void main(String[] args) {
	int myVariable = 10;
	function(myVariable);
	System.out.println(myVariable);  // This will still print 10
}

public void function(int anotherVariableName) {
	anotherVariableName = 5;  // Only changes the value inside this function
}
```

Whereas the same thing passing in a class name would change the instances itself. Imagine our `Fruit` class before we added the `final` modifier to `name`:
```java
public static void main(String[] args) {
	Fruit apple = new Fruit("Apple");
	function(apple);
	System.out.print(apple.name);  // This would now print Pumpkin
}

public void function(Fruit fruit) {
	fruit.name = "Pumpkin";
}
```

This is what is meant by "passed by reference".

One thing to note though is assignment doesn't override the passed in parameter:
```java
public static void main(String[] args) {
	Fruit apple = new Fruit("Apple");
	function(apple);
	System.out.print(apple.name);  // This would still print Apple because apple itself still refers to the instance above
}

public void function(Fruit fruit) {
	fruit = new Fruit("Pumpkin");  // fruit is now this instance for the rest of this method
}
```

This behavior actually leads to an interview question I find particularly annoying. The interviewer will ask "is an object passed by reference or by value into a method". Just answer "The reference to the variable is passed by value on the stack but the object itself is stored on the heap". If they ask you to explain what that means, excuse yourself to go use the restroom and instead run away, vowing never to return. I find it annoying because you absolutely do not need to know it in any practical sense. It's supposed to be a test of how well you know the language but it doesn't do a good job of that. Just keep in mind this behavior and you'll do fine. Frankly, you'll get the hang of it as you go and play around with classes and instances.

### Naming
Action vs noun.
## Encapsulation
Alright, last big term of this lesson: encapsulation

Encapsulation in computer science is bundling data together with a way to operate on that data. Big word, fancy sounding definition, and the perfect way to wrap up a lesson on OOP.

Let's make a `Person` class:
```java
public class Person {  
    private String firstName;  
    private String lastName;  
  
    public Person(String firstName, String lastName) {  
        this.firstName = firstName;  
        this.lastName = lastName;  
    }  
  
    public void setFirstName(String firstName) {  
        this.firstName = firstName;  
    }  
  
    public void setLastName(String lastName) {  
        this.lastName = lastName;  
    }  
  
    public String getFullName() {  
        return firstName + " " + lastName;  
    }  
}
```

And we can create an instance of that person:
```java
Person somebody = new Person("John", "Doe");
```

Just like before, we create an instance of our class, though our constructor takes two parameters this time, a `firstNme` and a `lastName`. We also have a method we can call to get the full name:
```java
System.out.println("My name is " + somebody.getFullName());
```

Internally, this takes our firstName and our lastName, concats them together with a space in between, and returns it. You'll notice we have `String` in place of `void` for the return type. Because we said we're going to return a `String`, the compiler will make sure that we do no matter what. It will not compile without that `return` statement. Luckily, concatenating a `String` together just makes another `String`, so we've satisfied the type requirements and Java will compile this. In the end, what's printed to the screen is:
```
My name is John Doe
```

One thing to notice inside the `getFullName` method is that we didn't use the `this` keyword on either `firstName` or `lastName`. This has to do with the scoping rules mentioned before that we'll go over below. `this` is not required here and would be pretty obvious to another programmer that they're fields (many editors will highlight/color them differently), but if it were less obvious I would have included the `this` keyword:
```java
    public String getFullName() {  
        return this.firstName + " " + this.lastName;  
    }
```

What happens if we try to change the `firstName` on our variable `somebody`:
```java
somebody.firstName = "Jane";
```

Uh oh, the compiler won't like that one bit. That's because we declared the `firstName` field to be `private` so we can't modify that field outside of that class. Luckily, there's a method called `setFirstName` that we can call:
```java
somebody.setFirstName("Jane");
```

In the context of the `setFirstName` method, we CAN edit the `firstName` field and we assign it to the `firstName` that is passed in. Now if we printed our name again, we would get:
```
My name is Jane Doe
```

You may be wondering now why you would have firstName and lastName private if you can just overwrite their values with a method. There can be several reasons for that. In our case, our set methods are very simple, but you might have more complicated code that needs to run in order to keep your code from breaking. For example, say your code had a requirement that the letter `Q` never be used in a name. If you just gave everyone `public` access to your `firstName` and `lastName`, then they could absolutely update it to have a name WITH the letter `Q` in it. If they are forced to go through your method, then you can do things like remove all `Q`'s before storing it to your field.

The other thing making `firstName` and `lastName` private does is make it so no one can read them in code, they can only get the full name through the `getFullName` method. This is part of encapsulation, where you hide information you don't want others to see.
#### Getters and Setters

One method of accessing `private` or `protected` variables in Java is through `public` "getters" and "setters". The `setFirstName` and `setLastName` methods above are "setters" and the `getFullName` method is a "getter". There's nothing really special about them and in fact, some would argue that `getFullName` isn't a real getter because we're not getting a field called `fullName`. Really, as long as you can describe what you're doing successfully and the code accomplishes what you want it to, you're good.

Let's look at a different version of the `Person` class we made before:
```java
public class Person {  
    private String firstName;  
    private String lastName;  
    public String fullName;  
  
    public Person(String firstName, String lastName) {  
        setFullName(firstName, lastName);  
    }  
  
    public void setFirstName(String firstName) {  
        setFullName(firstName, lastName);  
    }  
  
    public void setLastName(String lastName) {  
        setFullName(firstName, lastName);  
    }  
  
    private void setFullName(String firstName, String lastName) {  
        this.firstName = firstName;  
        this.lastName = lastName;  
        fullName = firstName + " " + lastName;  
    }
}
```

We still have our `setFirstName` and `setLastName` methods as well as our `firstName` and `lastName` field. In addition to this, we have added a `fullName` field that's `public`, removed our `getFullName` method, and added a `private` method called `setFullName`. The bodies of our methods and constructor have also changed to call this new `private` method. Notice how we can call the `private` method inside the `Person` class, but cannot call it from outside the class.

Let's think about some code, line by line.
```java
Person businessPartner = new Person("John", "Doe");
System.out.println("I'm grabbing lunch with " + businessPartner.fullName);
```

Perfect, this would say `I'm grabbing lunch with John Doe` and everything seems to be in order. Next up, they might change their full name:
```java
businessPartner.fullName = "Jane Roberts";
System.out.println("I'm grabbing lunch with " + businessPartner.fullName);
```

This would of course print `I'm grabbing lunch with Jane Roberts` and we're still doing great! Finally, let's look at one last bit of code:
```java
businessPartner.setLastName("Smith");
System.out.println("I'm grabbing lunch with " + businessPartner.fullName);
```

This would print `I'm grabbing lunch with John Smith`. Wait what? How did that happen? Well, as it turns out, to make our `setFirstName` and `setLastName` functions work, we had to store the `firstName` and `lastName` as fields. When we updated the `fullName` to "Jane Roberts", the `firstName` was still "John" and the `lastName` was still "Doe". Because we allowed the consumer of our `Person` class (ie whatever code is modifying these variables) to muck about with `fullName` directly instead of making them go through a setter, we've ended up in this mess.

When `setLastName` is called with `Smith`, the `fullName` of "Jane Roberts" doesn't matter anymore, as we're overwriting it. We kept the value of `John` for the `firstName` and updated the `lastName` to be `Smith`. Then the `fullName` is updated to be `John Smith` which is what was printed out.

This is called "breaking encapsulation" and you generally want to make sure you think through how your classes are going to be used to avoid it as it is the source of a great many bugs.
#### Scoping
The last thing to cover is "scoping". I mentioned "context" in the first lesson and this is where that really begins to shine. You have to be able to switch between contexts, between the code that you're calling and what code you're calling from. Being able to do this quickly will make you a very effective programmer.

Let's look at a class:
```java
class ScopingExample {
	private int field;

	public void method(int parameter) {
		int scopedVariable;
	}
}
```

This example has 3 `int` variables: `field`, `parameter`, and `scopedVariable`. 

We have some rules to go over. The first is that you cannot re-declare parameter in the function. For example, this is invalid:
```java
class ScopingExample {
	private int field;

	public void method(int parameter) {
		int parameter;
	}
}
```

You can, however, do that with a field:
```java
class ScopingExample {
	private int field;

	public void method(int parameter) {
		int field;
	}
}
```

With a scoped variable, it is only valid on the line it is declared and every line after that WITHIN the method that it is declared. A parameter is valid on any line WITHIN the method since it is declared up top.

When referencing a variable name, Java will first check to see if that matches a parameter or another variable declared in the scope of the method. If it matches, it assumes that's the one we're using. If you want to instead use a field by the same name, you must prefix it with `this.`:
```java
class ScopingExample {
	private int field;

	public void method(int parameter) {
		int field;
		field = parameter;  // Only assigns to the `field` one line up
		this.field = parameter;  // Assigns to the `field` defined at the top of this class.
	}
}
```

## Conclusion
I know that was a lot, and honestly it may not have made a lot of sense the first read through. I've found the most effective way to help someone understand this is via practice and answering specific questions as they come up. Don't be afraid to ask specific questions you may have in the discord or during class. There's absolutely no shame in it, especially not as we get into this section. You must do your best to understand as much of this as possible before we move on to more advanced stuff.