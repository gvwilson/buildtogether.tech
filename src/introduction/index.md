If you are an undergraduate embarking on a team software project,
this book will give you the tools you need to succeed.
Some of these are purely technical,
like version control system,
while others are social:
how to form teams,
manage people who aren't pulling their weight,
cut features when time runs short,
and understand who owns the things you produce.

Our aim is to teach you how to be a *compassionate programmer*:
one who cares as much about the well-being of their colleagues and users
as they do about their own.
This focus is not entirely altruistic—everything you do to help others
also helps your future self—but now that we know how much harm software can do,
we need to learn to build it in better ways.

## Topics

Life is short and your project is even shorter,
so this book focuses on
the things that will help you the most in the short term:

-   How to work effectively in a small team
    when you are constantly being interrupted by other tasks
    like the homework for your other courses.

-   What tools you should use to build, test, deploy, and describe software
    in less time and with less pain.

-   How to design a program (or a set of related programs)
    that will take several weeks to write.

-   How a few simple changes in your study habits
    will enable you to learn more and more quickly.

-   What legal rights you have to the software you create as a student
    (and on the job).

-   What to do when things go wrong.

We have included other material as well,
since there is a lot of variation between project courses
and even more between the people doing them.
Throughout,
we are guided by a modified version of [Dobzhansky's Rule][dobzhansky]:

> Nothing in software engineering makes sense except in the light of psychology.

Many of the hard problems in software engineering stem from the fact that
our mental capacity is limited,
which means we have to design programs so that they will fit into the space between our ears.
In addition,
we learn and work better when we are doing things that help us meet our personal goals,
which means projects will be more successful if we take motivation into account.

## Audience

Every lesson should be written with specific learners in mind.
These [%i "learner persona" %][personas][t3-personas][%/i%] describe ours:

-   Yanina is in the third year of a computer science degree.
    She worked on several volunteer projects in high school and through her mosque,
    but the "Introduction to Software Engineering" course she's about to take
    will be her first semester-long team project at university.
    This guide will help her and her teammates figure out what to do when.

-   Brad is in Yanina's classes.
    He started programming when he was nine years old,
    and as a result can do many assignments in half the time it takes other students
    (something he attributes to intelligence and aptitude
    rather than to his parents being able to afford to send him to after-school coding camps).
    He finds any discussion of what he privately called "social justice bullshit" tiresome;
    this guide will help him understand why that attitude is self-defeating.

-   Ahmadou worked as an illustrator for several years
    before doing an intensive 14-week conversion course to become a JavaScript developer.
    He has a lot of experience working in teams to meet deadlines,
    but is still often bewildered by the tools, jargon, and culture of programming.
    This guide will help him figure out what his new colleagues think is "normal".

-   Sharla teaches JavaScript at Yanina's college
    and for the conversion course that Ahmadou went through.
    They taught the "Introduction to Software Engineering" class last semester,
    and came away feeling that their students had wasted a lot of time
    on things that turned out not to be useful.
    This guide will help them give more structure to the next offering
    and set more realistic expectations.

Like these personas, readers should:

-   Be able to write multi-page programs in Java, Python, JavaScript,
    or some other modern programming language.

-   Be able to create static web sites using HTML and CSS.

-   Know how to create directories, delete files, and find things with the Unix shell.

-   Have used [Git][git] on individual projects.

This book can be read on its own or as a companion to *[Software Design by Example][stjs]*,
which teaches the basics of software design
by showing you how to build the tools you program with.
If you are looking for a project to do in a course,
adding a tool to those covered there would be fun as well as educational.

## Using and Contributing

All of the written material on this site is made available
under the [Creative Commons - Attribution - NonCommercial 4.0 International license][cc-by-nc]
(CC-BY-NC-4.0),
while the software is made available under the [Hippocratic License][hippocratic-license].
The first allows you to use and remix this material for non-commercial purposes,
as-is or in adapted form,
provided you cite its original source;
the second allows you to use and remix the software on this site
provided you do not violate international agreements governing human rights.
Please see [%x license %] for details.

If you would like to improve what we have or add new material,
please see the Code of Conduct in [%x conduct %]
and the contributor guidelines in [%x contrib %].
If you have questions or would like to chat about using this material in a course,
please file an issue in [this site's GitHub repository][bst-repo] or [send us email][email].

## Acknowledgments

This book is dedicated to [%i "Petre, Marian" %][Marian Petre][petre-marian][%/i%],
who taught me that not everything worth studying can be measured,
and to [%i "Wilkie, Tom" %]Tom Wilkie[%/i%],
who taught me how to turn a thousand words I'd written into a hundred someone would actually want to read.
I am also grateful to all of the students who have done projects with me over the years.

I have tried to base recommendations on empirical software engineering research ([%x research %])
and on the science of teaching and learning ([%x thinking %]).
Where those don't have answers,
I have drawn on the experience of the students and programmers mentioned below.
Any errors, omissions, or misunderstandings that remain are entirely our fault.

- [Bram Adams](https://mcis.cs.queensu.ca/bram.html)
- [Rohan Alexander](https://rohanalexander.com/)
- [Tavish Armstrong](http://tavisharmstrong.com/)
- [Titus Barik](https://www.barik.net/)
- [Robert Beghian](http://www.vasken.ca/)
- [Yanina Bellini Saibene](https://yabellini.netlify.app/)
- [Neil Brown](https://twistedsquare.com/)
- [Jordi Cabot](https://jordicabot.com/)
- [Silvia Canelón](https://silvia.rbind.io/)
- Francisco Canas
- [Mike Conley](https://mikeconley.ca/)
- [Michael DiBernardo](https://mikedebo.com/)
- [Isaac Ezer](http://www.isaacezer.com/)
- [Ian Flores Siaca](https://ianfs.dev/)
- [Adam Goucher](https://adam.goucher.ca/)
- [Mustafa Haddara](https://twitter.com/MustafaHaddara/)
- [Johan Harjono](http://johanharjono.com/)
- [Kate Hertweck](https://katehertweck.com/)
- [Daniel Jackson](https://people.csail.mit.edu/dnj/)
- [Jacob Kaplan-Moss](https://jacobian.org/)
- [Ritu Kapur](https://sites.google.com/view/ritu-kapur)
- [Zain Kazmi](https://zainhkazmi.github.io/)
- [Laurie MacDougall Sookraj](https://www.linkedin.com/in/lauriemacdougallsookraj/)
- [Darren McElligott](https://www.linkedin.com/in/darren-mcelligott-07689473/)
- [Kim Moir](https://kimmoir.blog/)
- [Natalia Morandeira](https://nmorandeira.netlify.app/)
- [Meiyappan Nagappan](https://cs.uwaterloo.ca/~m2nagapp/)
- [Iain Parris](https://parris.org/)
- [Elizabeth Patitsas](https://patitsas.github.io/)
- [Andrew Petersen](https://utmandrew.bitbucket.io/)
- [Andrey Petrov](https://shazow.net/)
- [Andrew Potapov](https://www.andrewpotapov.com/)
- [Lutz Prechelt](http://www.mi.fu-berlin.de/w/Main/LutzPrechelt)
- [Yim Register](https://students.washington.edu/yreg/)
- [Evan Schultz](https://evanjustevan.com/)
- [Alex Serebrenik](https://www.win.tue.nl/~aserebre/)
- [Naaz Sibia](https://www.linkedin.com/in/naaz-sibia/)
- [Andreas Stefik](https://web.cs.unlv.edu/stefika/)
- Rory Tulk
- [Blake Winton](https://bwinton.latte.ca/)
- [Andy Zaidman](https://azaidman.github.io/)
- [Andreas Zeller](https://andreas-zeller.info/)

[%b Sholler2019 Wilson2019 Irving2021 Smalls2021 %];
I'm grateful to [%i "Taylor & Francis" %][Taylor & Francis][taylor-francis][%/i%],
[%i "PLoS" %][PLoS][plos][%/i%],
and my co-authors for making available under open licenses.
I would also like to thank [%i "Graf, David" %]David Graf[%/i%] for [%i "doi2bib" %][doi2bib][doi2bib][%/i%]
and [%i "Elbakyan, Alexander" %]Alexandra Elbakyan[%/i%] for [%i "Sci-Hub" %][Sci-Hub][sci-hub][%/i%]:
this book would have been much harder to write without their idealism and hard work.

*All proceeds from this project will go to support the [Red Door Family Shelter][red-door].*
