# Lesson 01: Context, primitives variables

## Context

Context is... important. The dictionary defines context as:

> the circumstances that form the setting for an event, statement, or idea, and in terms of which it can be fully understood and assessed.

A lot of teaching about code is presented as "here's what code looks like and all the individual pieces". I'm not a huge fan of it, but you have to start somewhere and that's what we're going to do here.

As we go through the lessons and build on things, I'm going to try to teach you to understand the context that you're working on. Once you truly understand context in a programming language, and can switch between them with ease, your skill as a programmer goes way up.

## Primitives

A primitive in Java is a predefined type that's built into the language. There are 8 primitive types. They are:
- byte
- short
- int
- long
- float
- double
- char
- boolean

These are your basic building blocks and everything you design, build, or work with, will use these blocks.

Of course, the question you may be asking yourself is "when do I know which one to use!". That's a great question. Let's group the primitive types into similar buckets and go over them.

### Primitive Types: byte, short, int, and long
These are `whole numbers`. In mathematics, the term `integer` and `whole number` are generally used interchangeably. In programming, the term `integer` will be used to describe this collection of types and `int` will be used to describe one option for a type of integer. However, sometimes people will also use them interchangeably. int is a very common default option if you're not sure what size to go with.

We can further break think about integers in mathematics as `positive` or `negative` integers. For example, the numbers 1, 3, and 5 are all positive integers. The numbers -1, -3, and -5 are all negative integers. In programming, we have `unsigned` and `signed` integers. `unsigned` simply means that it can represent a value starting at 0 and going up util it hits a certain limit. That limit is dictated by the size of the integer.

`signed` means that it can represent a positive or negative integer. In general, signed integers have half the maximum value of an unsigned integer of the same size, with the tradeoff that they can represent negative numbers. Java ONLY has signed integers.

For practical purposes, the range of values you can represent with each type:
- byte: -128 to 127
- short: -32768 to 32767
- int: -2147483648 to 2147483647
- long: -9223372036854775808 to 9223372036854775807

Something that will trip people up is what happens when you get to the end of that limit. For example, if you have a byte with a maximum value of `127`, then adding 1 to that value doesn't give you 128, it gives you -128. Similarly, subtracting 1 from -128 doesn't give you -129 but instead gives you 127.

If you understand binary, you can research more about `two's compliment` which is how these numbers are stored in the computer. Otherwise, just keep the ranges in mind.

### Primitive Types: float and double
These are decimal numbers. I won't go into them too heavily at this time. They use the IEEE 754 specified formula, for which there's a good video down below. However, it very much helps if you understand binary. Feel free to pause it if you want to spend some time thinking through what he says, it's a very informative 20-minute video.

For now, there's a few things I want to point out. The first is that the further away from zero, the less accurate a floating point number is. The second is that there are some special values for floating point values, such as positive infinity (usually represented as `+inf`), negative infinity (`-inf`) and Not a Number (`NaN`). You can also have a positive zero and a negative zero which is not something you can do with integers.

In Java, double is actually the default. If you write `0.3` in Java, the compiler will assume you want a double. To get a floating point number, you have to write `0.3f`. Notice the `f` after the value of `0.3`.

`double` is just double the size of a float. 

Here's the range for float and double:
- float: 1.40239846e-45f to 3.40282347e+38f
- double: 4.94065645841246544e-324 to 1.79769313486231570e+308

### Primitive Types: boolean
Has anyone ever asked you a yes or no question? Wait, I just did. Sorry. :'(

In programming, we use `true` for `yes` and `false` for `no`. It's pretty simple, and you can think of a boolean as only having those two options. When we cover things like loops and if statements, we will often ask ourselves "is this statement true" or "is this statement false".

### Primitive Types: char
`char`, short for `character` essentially represents a letter. It's value range is from 0 to 65535. Notice that that's an entirely positive range which would make it "unsigned" and I said above that Java doesn't have unsigned integers. That's because this technically isn't an integer. We'll go over this more in a future lesson.

## Variables
A variable, put simply, is something that can change. Of course, we're absolutely going to introduce variables that cannot change later, but like many things it's easier to introduce by lying just a little about the details.

Think of variables like a box with a name. That box can hold a value in it, and we can refer to that value by name. We can update that value by referencing the name, use it to make decisions, or many other things.

Let's look at an example:

```java
int a = 30;
```

You can think of this as putting the value of `30` into the box `a`. You may also notice we put `int` before the `a` above. That is the variable's type. We'll go into that in a bit. The last thing to notice is the `=` in the middle and the `;` at the end.

A single `=` is an assignment. It "assigns" whatever is on the right into whatever is on the left. The `;` or semicolon is put at the end of the statement. This is what separates one statement from another. As you learn, keep an eye on where a semicolon is needed and where it is not. For this statement, it is very much needed. We'll go over `==` or "equal comparison" down below.

### Declaration vs Definition

Once you declare a variable, you can then define it. You cannot define it before you have declared it. For example, we can write:

```java
int a;
a = 30;
```

However, we CANNOT write:

```java
a = 30;
int a;
```

The line `int a;` is the declaration and the `a = 30;` is the definition. Above, when we said `int a = 30;`, we were combining declaration and definition. Most of the time, this is going to be the format you will see, but it is sometimes helpful to know these as two separate concepts. When we get into classes later on, this becomes absolutely necessary to understand, and we will reiterate it then.

I will say, just for transparency, that I'm sort of lying here about declaration and definition. In this case, it's less that it's more complicated and more that the "official" guidelines here are different from common usage. I've presented the common usage version here and other developers will completely understand you when you use these terms as presented.

### Types

In the above sections, I used `int` in front of my `a` variable. This is called the variable's `type`. Java is what's known as a statically typed system. That means that every single variable has some type. In this case, `int` is a primitive type meaning it's built into the language with its own constraints as we discussed above. For example:

```java
int a = true;
```

If you tried to run that, you would get the lovely response `error: incompatible types: boolean cannot be converted to int`. What it's trying to tell you is that you cannot convert `true`, a boolean, into a type that will fit into the `a` box since that box is an integer. However, this would work:

```java
boolean a = true;
```

You can convert some types, however. For example:

```java
short b = 20;
int c = b;
```

This makes a variable called `b` and gives it the value of `20`. That value fits just fine in the range a short can take up. Then, it assigns that value to `c`. Notice how we're not directly storing the value of `20` into `c`, but taking whatever value is in `b` and storing it into `c`.

You must be careful with the sizes of your types, however. This will cause the compiler to error:

```java
int c = 30;
short b = c;
```

The error you will see is `error: incompatible types: possible lossy conversion from int to short` and your program won't run. This is because the `int` type is so much bigger than `short` and the compiler cannot guarantee that the value will fit in a short at the time the program will run. Sure, we as humans can see that the value of 30 would fit into a short, but the compiler doesn't work that way. It works line by line and knows it can't fit all the values of an `int` into a `short` so it won't let you.

### Scope

Scope is in many ways another word for context as presented above. You don't yet need to understand different scopes/contexts just yet, but I wanted to show you an error you may run into if you try to declare the same variable twice. Let's look at an example:

```java
int a = 30;
a = 20;
```

This is perfectly acceptable. We declared the variable `a` as an `int`, then defined it by giving it the value of `30`. On the very next line, we redefined it by giving it the value of `20`. This is perfectly acceptable.

```java
int a = 30;
int a = 20;
```

That however, is not. You'll get an error like `error: variable a is already defined in method main(String[])`. Noticed that it uses the word `defined` here. Remember when I said I was sorta lying about the definitions above? This is one of those cases. Really, the Java compiler is just telling you that you `declared` the variable `a` twice and that is what it is upset by.

### Naming

You will hear the joke "There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors."

Congratulations on learning about your first hard problem. Naming things is important. For example, in our case of `int a = 30`, you have no idea what `a` actually is. It's just... a letter. Absolutely useless. However, if we instead go with `int myIQ = 30`, you might immediately think "now wait a minute, that doesn't seem right". You did think that.... didn't you?

Variable names help you as the programmer understand more about the usage of a variable and in what contexts it might be useful. It can also help identify issues. For example:

```java
int a = 30;
int b = a;
```

This is correct code and will compile, but it doesn't make a lot of sense to read does it. If we instead wrote:

```java
int myAge = 30;
int myIQ = myAge;
```

I mean it sorta makes sense, I'm sure I get smarter as I get older right? But it should still stand out better when determining if your code is correct.

There are various naming conventions. We call the naming of variables `Camel Case`. Camel Case is when you capitalize the first letter of every word in a variable name, except the very first letter of the very first word. For example `myVeryLongVariableName` is clearly readable as the short phrase `My very long variable name`, much more readable than `Myverylongvariablename`.

You may be wondering why we don't capitalize the very first letter of the very first word. That's because if we did, it would be `Pascal Case`, and this isn't Pascal's time to shine just yet. The short answer is just "it's convention".

### Basic Operations

There are some basic operations you can do with variables such as ints and floats. Here are some of them, demonstrated with the variables `a` and `b`. These return the same type as `a` and `b`

- Addition: `a + b`
- Subtraction: `a - b`
- Multiplication: `a * b`
- Division: `a / b`
- Remainder (Modulo): `a % b`

These all return a boolean type:

- Equal comparison: `a == b`
- Not-equal comparison: `a != b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`
- Less than: `a < b`
- Less than or equal to: `a <= b`

## Further Learning
Note that these links use other number systems like binary and hexadecimal. If you don't understand those number systems, you may just want to bookmark these for later.

- (YouTube) [IEEE 754 Standard for Floating Point Binary Arithmetic](https://www.youtube.com/watch?v=RuKkePyo9zk)
- [Two's compliment](https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html)