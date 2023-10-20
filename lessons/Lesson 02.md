# Lesson 02: Control structures
## Welcome to pseudocode
Pseudocode is "fake" code. It is code that a compiler would not accept used to demonstrate a simple concept. Many times we will pretend variables or functions exist here that have not been defined or declared. This can be a little confusing at first while you're learning the syntax, but I will try to specify when I use pseudocode. Most pseudocode examples are pretty straightforward to read, but feel free to ask if you have any issues with one of them.

Sometimes we will use actual Java code but not include some of the features needed to actually run the program such as the `main` function. More on that later.
## if statements
`if` statements are the bread and butter of any program. You make decisions every day many times during the day, but your brain usually handles them a bit differently.

Let's think about how you get ready for school. At some point, you have to throw on some clothes. Hopefully there's a quick mental check for "do I have clean clothes" that takes place in your brain. If you do, great, just throw them on and head on out. If not, well maybe you have time to wash them really quickly. You can sort of play out how long it would take for you to do the laundry and decide based on that timing what action you should take.

Program's don't have that luxury most of the time. They're very linear. A program might start with a simple check like we would (the following is all pseudocode):
```java
if(iHaveCleanClothes) {
	wearThem();
}
```

If we have clean clothes, we `wearThem()`. The parenthesis there after the name mean that it's a function call. I'm not going to go into what that all means just yet, so for now you can just read it as "you wear the clothes". Think of it as an action you take. It's also helpful to notice the braces `{` and `}` that wrap the `wearThem();` code. Everything inside those braces will run `if` the variable `iHaveCleanClothes` evaluates to `true`. Notice also that statements inside the `if` statement need to have a semicolon `;` but the `if` statement itself does not need one at all. Everything inside those braces, we call the "body" of the `if` statement.

If we don't have clean clothes, what do we do? Well, we could always wear them:
```java
if(iHaveCleanClothes) {
	wearThem();
} else {
	wearThem();  // Eww, dirty clothes
}
```

Yeah that's kinda gross. Let's see if we have time to wash them:
```java
if(iHaveCleanClothes) {
	wearThem();
} else if(iHaveTimeToWashThem) {
	washThem();
	wearThem();
} else {
	wearThem();  // Eww, dirty clothes
}
```

Perfect, in 2 out of our 3 cases, we'll have clean clothes. Just to reiterate, we start from the top. If we have clean clothes, we wear them. If not, but we have time to wash them, we wash and then wear them. That's what the "else if" does above. `iHaveCleanClothes` was `false`, so we ignored that section. Then we checked if `iHaveTimeToWashThem` is `true`. If it is, great! We'll wash and then wear them. Finally, we get down to our `else`. This section runs if nothing else before it is `true`. Which, in our case, means wearing dirty clothes.

As a note, you'll see the bodies inside the `if`, `else if`, and `else` sections sometimes called the "branches" of the `if` statement.

> Note: If none of that made sense to you or you read through it quickly, re-read it and ask questions until it does make sense before continuing.

### Simplifying if statements
Now let's think about our if statement here. One thing to notice is that we always call `wearThem()` no matter what AND we always call it as the last statement. That means we can remove that and put it at the end outside of our `if` statement:
```java
if(iHaveCleanClothes) {
} else if(iHaveTimeToWashThem) {
	washThem();
} else {
}
wearThem();
```

That code is functionally equivalent to the one above. One oddity is that we now have some empty if statements. Our `else` block can go away entirely now, it's no longer needed:
```java
if(iHaveCleanClothes) {
} else if(iHaveTimeToWashThem) {
	washThem();
}
wearThem();
```

The `if` and `else if` are a little bit harder. If we just removed the `if` checking `iHaveCleanClothes`, we would end up with this pseudocode:
```java
if(iHaveTimeToWashThem) {
	washThem();
}
wearThem();
```

This presents a bit of a problem though! We will ALWAYS wash our clothes if we have time before school. Instead we need to check if they're also dirty which is another way of saying `not` clean. We do that with a `!` symbol. The `also` can be read as `and` and is represented by `&&` below.
```java
if(! iHaveCleanClothes && iHaveTimeToWashThem) {
	washThem();
}
wearThem();
```

That if statement can be read by a human as `if I do NOT have clean clothes AND I have time to wash them`. While the `!` means `not` and has to go in front of the variable, it is usually read differently by the human programmer. This means you want to be careful how you name your boolean variables. For example, if you named it `iHaveNotCleanClothes`, then that would make it harder to read `! iHaveNotCleanClothes`. As a human, you'd read that as `I have not not clean clothes` and you'd have to think harder to realize that just means `I have clean clothes`.

The `&&` above means `and`, meaning both sides have to be `true` for the statement to be `true`. If either side evaluates to `false`, then the whole statement is `false`.

I have not used this yet, but you can do the same thing for `or` and that is represented as `||`. In programming `or` can be `true` if the left or right side is `true`. If they're both `true`, the statement is also `true`. 

### Evaluation order
One last tidbit about `and` and `or` that are helpful to keep in the back of your mind. They are always evaluated left to right and then parenthesis inside to out. Given the example (a, b, and c are all boolean values):
```java
a || (b && c)
```

Let's look at a few cases. If `a` is `true` here, the whole statement is `true`. We don't need to actually know what `b` and `c` are and in fact the program will not even bother checking or evaluating `b` or `c`. The second it sees that `a` is true, it says "pack it up, we're good here" and evaluates to `true`.

How about a different set of values. If `a` is false, then the program cannot immediately know whether the statement is `true` or `false`. That depends entirely on how `(b && c)` evaluate. If `b` is `false`, then the program knows `(b && c)` is false and therefore the whole statement is `false`.

Final test, if both `a` and `b` are `true`, then the entire statement hinges on `c`. If `c` is false in this example then the whole statement is `false`. If `c` is `true`, then the whole statement is `true`.

Make sure you work a few of these out yourself to try and get an intuition about what will be checked with different values for `a`, `b`, and `c`. When we get more into functions, this is extremely powerful to know. For now, keep it in the back corner of your mind.

## while loops
`while` is our first introduction to what is known in programming as a `loop`. In programming, a `loop` is something that continues until a specified condition is met. Of course, `specified condition` is just fancy human speak for "something changes from `true` to `false` or from `false` to `true`".

Let's look at a simple example (Note that this is not pseudocode):
```java
int x = 0;
while(x < 5) {
	System.out.print("Na");
	x++;
}
System.out.println("Batman!!!");
```

Whoa, okay that was a decent bit of new code. Let's break it down. You should already be familiar with assigning a variable. In this case, we create a variable called `x`, give it the `int` type and assign it the value of `0`.

Now we've got our `while` loop. You'll notice it's just like an `if` statement with those braces. Everything inside those braces will run `while` the expression `x < 5` evaluates to `true`. 

Inside the braces, you'll notice a hopefully familiar function, the `print` function. Don't worry about the details with `System.out` yet, that will all be explained later. Because we're using `print` instead of `println` (print with new line), all of those "Na" prints will be on the same line.

While still inside the braces, you'll notice `x++`. The `++` means "Increment this variable by 1". It is equivalent to `x = x + 1;`

And finally, outside of the braces, we print "Batman!!!" with a new line after it. The "new line" stuff is just like if you pressed the enter key on your keyboard.

Let's think about the execution of the above code. We'd start out with `x` being `0` and passing our test of `x < 5` since `0 < 5`. One thing to note here is that we test before we ever get into the loop. This means the loop could entirely skip running if our test evaluates to `false`. We print out one "Na":
```
Na
```

Next up, we increment `x` and it now has a value of `1`. We're at the bottom of the while loop and so we run our check again. `1 < 5` so we run through our loop again. Another "Na" is printed:
```
NaNa
```

And then `x` is incremented and has the value of `2`. We keep going in this fashion until we've printed 5 "Na"'s and `x` has the value of `5` at the bottom of the loop:

```
NaNaNaNaNa
```

Since we're evaluating `x < 5` and the statement `5 < 5` is false, we exit our loop, finally printing "Batman!!!":
```
NaNaNaNaNaBatman!!!
```

A while loop is very flexible as the condition can be based on anything. You can have a boolean variable and then decide in your loop whether that variable should be `true` or `false`. If that is the condition your `while` loop is testing, then it will only leave the loop when that variable is `false`.

### for loops
A `for` loop has more constraints on it than a `while` loop, but usually more concisely represents some loops. For example, the code above that printed "NaNaNaNaNaBatman!!!" can be written as such with a `for` loop:
```java
for(int x = 0; x < 5; x++) {
	System.out.print("Na");
}
System.out.println("Batman!!!");
```

That code can be a little bit easier to read. As you mature as a developer, this format can become a mental shortcut for you. Let's break this down into pieces and explain each part.

Just like in the `while` loop, we had to initialize a variable. In both cases, we said `int x = 0`. We do that in the parenthesis of the `for` loop as well. You'll also notice two semicolons `;` inside the parenthesis. They separate the 3 required pieces of a `for` loop: Initialization, Check, and Change. In this case, the statement `int x = 0` represents our initialization.

Following our initialization, we have our check `x < 5`. This is the only thing that was present in the `while` loop parenthesis but here it's one of three things we need.

Lastly, we have the change, here represented as `x++` meaning "increment the variable `x`".

When looking at a for loop, remember that the initialization runs ONCE at the BEGINNING of the `for` loop. Then the check is run BEFORE running the code in the braces. Finally, the change is run AFTER the code in the braces where we then run our check again.

Starting at `0` and incrementing up to a certain number is the most common for loop you'll see. It's the easiest format for a programmer to quickly see and understand. Anything else might not make sense.

## Other loop things to be aware of
### Infinite loops
An infinite loop is one that runs on forever. You can write one pretty easily in Java:
```java
while(true) {
}
```

Of course, we're being a little dramatic here. What we mean by "infinite" is that the loop will continue until you kill the program or your computer shuts down.

You can also do the same thing with a `for` loop:
```java
for(;;) {
}
```

Notice how we have our two semicolons but no initialization, check, and change? Yeah so... those are all optional. It's generally considered good practice to keep them all in there for readability, but you could absolutely be wild about it, Java will completely allow this:
```java
int x = 0;  
for (; x < 5; ) {  
    System.out.print("Na");  
    x++;  
}  
System.out.println("Batman!!!");
```

Here we have no initialization and no change code, but we do have the check. At this point, you should have just used a while loop.

Feel free to play around with this concept in your own time, but when writing code that others will read and need to understand, it's best to stick to good practices.

### continue and break
I'm almost afraid to teach this. Put this far back in the depths of your mind, far far away from your current use. These are very powerful tools but used incorrectly can make your code much harder to read and understand.

`break` means "Leave the loop". For example, we could have an "infinite" loop but `break` out from it so it's no longer infinite:
```java
int x = 0;  
while (true) {  
    if (x >= 5) {  
        break;  
    }  
    System.out.print("Na");  
    x++;  
}  
System.out.println("Batman!!!");
```

This code does the exact same thing as all of the examples, but as soon as `x >= 5`, it calls `break` which will leave the loop. Notice that the check here is the inverse of `x < 5` since we're deciding when to leave vs when to stay. You could also just use `x == 5` here.

`continue` means "don't run anything else in these braces and start from the check". It does have its uses, but they're honestly hard to show a simple case for. If you were to replace `break` in the example above with `continue`, then you would se "NaNaNaNaNa" printed and the code would then enter an infinite loop. This is because `x` would always evaluate to `>= 5` at that point and the `true` in the `while` statement is always `true`. Your program would constantly be doing those two actions again and again until you killed the program.

One use case for `continue` that I can think of is when accepting user input. If you decide the user input is not valid, you can put a `continue` inside an `if` statement. Anything past the end of that `if` statement will not run. Compare these two pieces of pseudocode:
```java
while(true) {
	int userInput = getUserInput();
	if(userInput >= 1 && userInput <= 100) {
		// Do something
	} else {
		System.out.println("That is not valid. Please enter a number [1-100]")
	}
}
```

compared to

```java
while(true) {
	int userInput = getUserInput();
	if(userInput < 1 || userInput > 100) {
		System.out.println("That is not valid. Please enter a number [1-100]")
		continue;
	}
	// Do something
}
```

Both of them are totally valid. But depending on the complexity of the code that replaces your "do something" above, the complexity of the checks to determine if the code is valid or not, etc. you may choose one option or the other.