# Lesson 03: Comments, Arrays, and Strings

This lesson is a bit packed with content that doesn't all mesh perfectly well together. Most of that has to do with this being the final set of things I want to cover before jumping into some more advanced and useful topics.
## Comments
I'm just gonna be honest with you. Comments are controversial. When to use comments, what they should say, etc. is all controversial. There's several arguments for and against their usage and we'll get into that.

Comments are parts of the source code that are not executed and are used to describe the code, the intentions behind it, or document resources needed to understand the code. There's 2 types of comments we'll be concerned about in Java: Implementation and Documentation.
### Implementation comments
There's a couple of formats that implementation comments can take. The simplest and most common is two forward slashes, `//`. For example:
```java
// This is a comment
```

The forward slashes are the start of the comment. Everything from that point on to the end of the line becomes a comment, meaning you can't add code after the fact. For example, this code won't print anything:
```java
// This is not really code: System.out.println("I'm not a real print statement");
```

And with that, you can finally understand one of my favorite [XKCD comics](https://xkcd.com/156/).

You can write comments in a different way as well that is suited for multiple line comments:
```java
/*
* This comment
* spans
* multiple lines
*/
```

Technically, only the beginning and end comment tags:
```java
/*
This comment
spans
multiple lines
*/
```

Many people like reading with the asterisks in front of each line, and sometimes your editor will automatically insert them for you.

One interesting caveat of this format is you can actually have code after them:
```java
/* This code will actually print */ System.out.println("I'm a real printer!");
```

This is usually done more rarely as it becomes harder to read. An alternative is to just use a comment on the line before it:
```java
// This code will actually print
System.out.println("I'm a real printer!");
```

The important thing to note here is the flexibility comments provide. As long as it aids in the readability or understandability of the code, it's fair game.
### Documentation comments
You'll see the term "Javadoc" used a lot. It's short for "Java Documentation" and it uses a special type of comment and special annotations to generate documentation. This documentation is very useful for you as a developer and you will learn to navigate it as a Java developer.

For now, the important thing to see is what it looks like compared to other comments:
```java
/**
* This is a Javadoc comment
*/
public static void myFunction() {
}
```

There's two things to notice here. The first is that it's similar to one of the implementation comments. The difference here is just one `*` at the beginning. Javadoc `/** */` vs implementation comment `/* */`. The second thing to notice is that it goes before something like a function or method. When we get into classes and functions more, you'll get to see more of this. For now, just knowing it exists is enough.

### When to use comments
You ever hear the phrase "never read the comments"? They're usually referring to the comments section of YouTube videos and blog articles where people can be really mean. In our case, commenting our code can be super helpful but never read the comments on blog articles talking about comments in code. People have OPINIONS. Frankly, I think any discipline has people with opinions on the "right" way to do something. For programmers, comments in code is just one of those things with very strong opinions for and against.

For me, I like building things. Arguing about those things means I have less time to build things so I try to avoid it. I'm going to talk about my experience with comments, since I've gone back and forth on their usefulness over the years.

One argument against comments you'll hear is "the code should be self-documenting". This means that the code should be so understandable that you can quickly read the code and understand what it's doing. This is actually a very appealing sentiment and I firmly believe code should be written to be easily scanned and understood. Sometimes that's a little difficult, so you can write a comment that gives more insight into "what" the code is doing. There's lots of little tricks here though. Say you've got some really complicated math formula:
```java
System.out.print((-b + sqrt(pow(b, 2) - 4 * a * c)) / 2a);  // Positive quadratic result
System.out.print((-b - sqrt(pow(b, 2) - 4 * a * c)) / 2a);  // Negative quadratic result
```

You could also just make variables with those names:
```java
double positiveQuadraticResult = (-b + sqrt(pow(b, 2) - 4 * a * c)) / 2a;
double negativeQuadraticResult = (-b - sqrt(pow(b, 2) - 4 * a * c)) / 2a;
System.out.println(positiveQuadraticResult);
System.out.println(negativeQuadraticResult);
```

I like this technique and honestly as far as the compiler is concerned, this is basically a negligible difference. In some cases, the compiler may generate the exact same code.

One argument for comments I really like is that comments should describe the "why" not the "how". What this means is that reading the code and understanding why it was written a specific way is more important to document in comments than how the code actually achieves its goal. This is one of my favorite uses of comments, but it can sometimes be hard to explain to new programmers. In general, I would say those comments answer the "business case" of the code. "Why was this code written? It was written to accomplish this goal." Because this is more nebulous, this is harder to decide on when to write such a comment, but you'll get a feel for it as you progress.

Another argument against comments is that they become stale. Code is often written and rewritten again and again. Sometimes, a comment that did apply to the code it was around no longer applies and becomes "stale" or wrong. The opposition to this argument is actually pretty simple in concept but harder in practice: You should treat your comments as being just as important as your code.

One last use of comments that I really like: resource documentation. Often times, I'll be struggling to figure out the concepts behind some code I need to write, especially in math heavy sections. If I find a resource that I think is particularly useful in helping me to understand that code, I will paste the link to get back to that resource. There is the caveat here that the server could go down and that link itself becomes "stale". It's unfortunate, but happens rarely enough that I don't generally consider it a good enough reason not to do it. If a resource is important enough, download it and save it in another location that your team can access.
## Arrays
It can sometimes be useful to store multiple values of the same type in a single variable. This is where arrays come in. Let's show what arrays look like in Java:
```java
int[] myGrades = {98, 100, 73, 85, 92, 89};
```

Notice that we use `int[]` to mean "array of int" instead of just "int". On the right side, we have an initializer for an array. Notice that we use braces, `{` and `}`, here as part of that initialization. While they use the same character, this is a separate meaning from the braces you would see in something like an if statement. Don't worry, the compiler will know the difference.

Inside those braces, we have comma separated `int`s that make up our array's value. These all have to be the same type as the array is specified. i.e. you cannot do something like put a floating point value in that list when your array is of type `int`.

Array's are also constant sized. You cannot resize an array after it has been created. There is a field on the array, `length`, that can give you the size/length of the array (note, some code uses `size` and others `length`, but for most things it means the same thing):
```java
System.out.println(myGrades.length);  // Will print 6
```

What if you need to grab an individual item from the array? To do that, we use a notation called "subscript" and it is represented by putting a number in brackets `[` and `]`. For example:
```java
int myMathGrade = myGrades[0];
```

This will grab the first element in the array, which is `98` in our case. Arrays start with "index" `0`. The term "index" just means what number item you're grabbing. The last index will always be the array's length minus one, in our case `5`.

At this point, you're probably wondering why it starts with `0`. Well, the actual answer involves how memory is laid out and how a computer access that memory. I don't want to get into that here, but I did want to point out that there is a reason. Starting with `0` may feel weird at first, but I promise it'll feel normal to you in no time flat.

With just the `length` and subscript, we can easily loop through an array with a for loop:
```java
for(int i = 0; i < myGrades.length; i++) {
	System.out.println(myGrades[i]);
}
```

Notice how we used a variable as the index for the subscript. Programming is so powerful because of building blocks such as this. This technique of starting with the first element and going through every element is called "iterating" through the array.

You do have to be careful though, you can crash your program if you ask for an index outside of the bounds of the array. If you ask for index `-1` or `6`, for example, you'll get what's called an `ArrayIndexOutOfBoundsException`. We'll talk about exceptions at a later time. For now, just be careful to keep your array indexes in bounds.

### Another for loop notation: for-each
I want to be clear that the for loop above is perfectly fine to use. There's absolutely nothing wrong with it whatsoever. There is, however, another way to write a for loop with an array if all you want to do is iterate through the array:
```java
for(int grade : myGrades) {
	System.out.println(grade);
}
```

This does the exact same thing as the for loop in the previous section, except it's more concise and readable. Both are perfectly valid ways to write for loops and I want you to have this in your back pocket. While this does use the `for` name, most programming languages and programmers will call this a "for each" loop. That can also be written as "for-each" and "foreach". In fact in some languages, `foreach` is the word used to write the loop, but not in Java. We just reuse `for` for both cases. That's not confusing.... right?

While it is readable, I am going to go over a few things here just to make sure we're all on the same page. In the for loop declaration, we have a single colon `:`, unlike two semicolons `;` in the other form. On the right side of that colon is the array. On the left side, we have what looks like a variable declaration. In fact, that's exactly what that is! We are declaring a variable called `grade` and making it the same type as our array, `int`. 

You may be wondering why we would ever want to use the regular `for` loop with an index. Well, if you need to know what the index is for the element you're currently working with, you cannot do that with the for each loop. Say we want to add 1 to each of your grades:
```java
for(int i = 0; i < myGrades.length; i++) {
	myGrades[i]++;
}
```

Doing the increment operator with the for-each loop would affect the variable inside the loop, but would not affect the array itself:
```java
for(int grade : myGrades) {
	grade++;
}
```

Let's talk about modifying the array to understand why.
### Modifying the array
You can't modify the size of the array, but you can modify individual elements. Say you suddenly did better in math:
```java
myGrades[0] = 100;
```

Excellent! Keep in mind how primitive variables work here too. With primitive variables, every assignment "copies" the value. This code would not modify the second element of the array:
```java
int myEnglishGrade = myGrades[1];
myEnglishGrade = 95;
// As of right now, myEnglishGrade is 95, but myGrades[1] is STILL 100.
```

This is why the for-each code did not modify the array. Every loop iteration, the value at that array position is "copied" into the variable `grade` and then that copy is modified.

While you can't change the size of the array, you can re-assign the whole thing:
```java
myGrades = {98, 100};
```

Now `myGrades.length` will return `2`.

### When to use and when not to use arrays
Arrays are a very useful feature, but you want to be careful when and how to use them. Sometimes, your code may become less readable because of it. Let's look at an example:
```java
int[] hitPoints = {10, 3, 3, 3, 3};  // hitPoints[0] is player's hit points
```

We're making a game and the player has 10 hit points. All of the enemies have 3 hit points here and there are 4 of them. Let's say you're writing the code for an attack that affects all enemies:
```java
for(int i = 0; i < hitPoints.length; i++) {
	hitPoints[i]--;
}
```

First off, `--` is called the "decrement" operator and works just like `++` except it subtracts one instead of adding one. And secondly, you may have noticed that we just damaged ourselves. We defined `hitPoints[0]` to be the player's hit points, but we started our for loop with `0` meaning we decremented our own hit points!

Here's the thing. We could just tell ourselves "that was a silly bug, we should always start at `1`" and write this code:
```java
for(int i = 1; i < hitPoints.length; i++) {
	hitPoints[i]--;
}
```

Now that would fix the code, but the stumbling block is still there. It's a one character difference and it's REALLY hard to notice it. That makes it hard to find when you're searching for problems. It's also something that you as the programmer have to constantly keep in the back of your mind. The more "cognitive burden" you have (ie the more you have to keep up with to write correct code), the more likely you are to make a mistake. And in this case, even though we had a comment on our array initialization, a lot of code can happen between that initialization and actual use as your code grows. So don't expect a comment like that to save you.

Let's take a different approach:
```java
int playerHitPoints = 10;
int[] enemyHitPoints = {3, 3, 3, 3};
```

Perfect! Now we can loop through our enemies and decrement their hit points! And because we're now writing safer code, we get a 3x bonus on our attack!
```java
for(int i = 0; i < enemyHitPoints.length; i++) {
	enemyHitPoints[i] -= 3;
}
```

Total K.O.! Huzzah! Another benefit here is our name change. It's much easier to think through our logic and reason with our code with descriptive names like `playerHitPoints` and `enemyHitPoints`. The difference in type also helps us a bit with safety too. If you tried to put `playerHitPoints` in the for loop above, the subscript operator wouldn't work. It doesn't, however, prevent you from making mistakes such as this:
```java
for(int i = 0; i < enemyHitPoints.length; i++) {
	playerHitPoints--;
}
```

Oops, you're at `6` hit points now. But if someone finds an issue while playing your game, this code might stand out. They could wonder "Why are we iterating through `enemyHitPoints` but affecting `playerHitPoints`?" and then fix the code. This is also a great example of where comments, might be useful, if that code was actually intentional:
```java
for(int i = 0; i < enemyHitPoints.length; i++) {
	playerHitPoints--; // Player is "confused", loses 1 HP per enemy
}
```

That comment changes your understanding of the code. It answers the "why" instead of the "how".

## Strings
If you've been reading straight through, you might want to stand up and stretch your legs for a second. I know I'm going to do that. I'll just be riiiiight back...

Okay I'm back. Let's talk about strings. A string is just a collection of characters, surrounded by double quotes:
```java
String message = "Hello World!";
```

We've actually been using strings for a bit now in various assignments and lessons. It's very useful to use for printing text that a human will read, but I didn't want to get into the details of it until now. They are ubiquitous enough that they are very close to being a foundational building block, but they are NOT a primitive type.

In the previous example, `String` is the name of the type. You'll notice that it has a capital first letter as opposed to all of the primitive types which are all lowercase. This is because classes are Pascal case. We'll go into both classes next lesson. `message` here is the variable name and then we have the initial value on the right of the equals sign, `Hello World!`.

You can think of a string as an array of characters. It doesn't work with the subscript notation before, so writing something like `message[1]` will not return the letter `e`. Instead, you have to use the `charAt` method: `message.charAt(1)`. We'll go into methods more deeply next lesson as well.

For now, let's go over some string basics. We won't cover everything here, but we'll cover just enough to have you start to feel comfortable with their basic usage.

### Concatenation
With primitives like `int` and `float`, you can add them with the `+` character. Strings can actually be added together as well, except they're "concatenated". That's just a fancy word meaning to put or link something together. Here's an example:
```java
String message = "Hello" + " " + "World!";
```

We could have written this as just the literal itself, but concatenation is fantastic when you have variables:
```java
String name = "Bob";
int age = 57;
String message = "Hello " + name + ", you are " + age + " years old!";
```

Our `message` variable here would have the contents "Hello Bob, you are 57 years old!". It's important to see that when you add an `int` or another primitive to a String, the String automatically converts that primitive to a String. e.g.:
```java
System.out.println("20" + 10);
```

This would print `2010` to the screen, NOT `30`. 
### Comparison
When comparing two primitive types, we can use `==` to compare them. With strings, and objects (more in the next lesson) in general, that gets a little harder. Let's look at an example:
```java
String message = "Hello World!";  
String hello = "Hello";  
String world = "World!";  
String message2 = hello + " " + world;  
  
System.out.println(message == message2);  
System.out.println(message.equals(message2));
```

This would print "false" and then "true". The reason here has to do with memory and object allocation, so I'm going to ENTIRELY ignore it and not explain it right now. The important thing to keep in mind is that strings are compared with `equals` instead of `==`.
### Formatting
String formatting is something I could spend hours and hours and HOURS on if I were to write it myself. To be honest, the formatting itself is very powerful but it's in the category of things where I know it exists and that's enough. You'll find a lot of things like that in programming. There will be techniques and skills that you learn exist but don't have memorized. Here, I'll just give and explain a simple example:
```java
String name = "Bob";
int age = 57;
String message = String.format("Hello %s, you are %d years old!", name, age);
```

The `%s` in the formatting string above means "replace this with another string". The `%d` means "replace this with a decimal". Every argument after the first one is assigned in order to these placeholders. In our case, this is the same string as above in the concatenation section, but it's easier to read the intent this way and adds flexibility.

Like I said, this is a really simple example to show that the functionality exists. Feel free to research all the ways this can be used on your own time.
### Escape characters
You may have had a question in the back of your mind for some time now. "How do you add a quote `"` to your String?"

This is where escape characters come into play:
```java
System.out.println("My name is \"Bob\"");
```

This would print `My name is "Bob"` to the screen. The backslash `\` character is called the escape character. There are certain symbols and letters that you can use to represent the backslash:

| Escape Character | Output    |
|------------------|-----------|
| \\"               | \"         |
| \\\\               | \\         |
| \\t               | (tab)     |
| \\n               | (newline) |

Fun fact, Markdown apparently also uses escape characters so that may look strange if you're looking at the Markdown source instead of a generated preview. There are also other escape characters that exist and some of those are really fun rabbit holes to find yourself in, but for now those are sufficient and useful to know.

## Conclusion
We just went over a lot of content and it wasn't all cohesive. You should feel comfortable reviewing any sections you didn't fully understand or revisiting a section as you do assignments. As always, please feel free to ask questions in the discord.