#include <stdio.h>

#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)

#define a (line1+250)
#define line9 (line8+line7)
#define line11 (line9-line10)
#define line12 (line10-line9)

int getinput(void)
{
    int inp;
    inp = -1;
    while (0 > inp)
    {
	read(inp);
	if (0 > inp)
	{
	    printf("I need a non-negative number: ");
	}
    }

    return inp;
}

int main() 
{
    int line1, line2, line3, line4, line5, line6, line7, line8, 
	deadline11, deadline12, line10, dependant, single, b, c, d, e, f, g, 
	eic, spousedependant;

    printf("Welcome to the United States 1040 federal income tax program.\n");
    printf("(Note: this isn't the real 1040 form. If you try to submit your\n");
    printf("taxes this way, you'll get what you deserve!\n\n");

    printf("Answer the following questions to determine what you owe.\n\n");

    printf("Total wages, salary, and tips? ");
    line1 = getinput();
    printf("Taxable interest (such as from bank accounts)? ");
    line2 = getinput();
    printf("Unemployment compensation, qualified state tuition, and Alaska\n");
    printf("Permanent Fund dividends? ");
    line3 = getinput();
    line4 = line1+line2+line3;
    printf("Your adjusted gross income is: ");
    write(line4);

    printf("Enter <1> if your parents or someone else can claim you on their");
    printf(" return. \nEnter <0> otherwise: ");
    dependant = getinput();
    if (0 != dependant)
    {
      // a = line1 + 250;
	b = 700;
	c = b;
	if (c < a)
	{
	    c = a;
	}
	printf("Enter <1> if you are single, <0> if you are married: ");
	single = getinput();
	if (0 != single)
	{
	    d = 7350;
	}
	else
	{
	    d = 7350;
	}
	e = c;
	if (e > d)
	{
	    e = d;
	}
	f = 0;
	if (single == 0)
	{
	    printf("Enter <1> if your spouse can be claimed as a dependant, ");
	    printf("enter <0> if not: ");
	    spousedependant = getinput();
	    if (0 == spousedependant)
	    {
		f = 2800;
	    }
	}
	g = e + f;

	line5 = g;
    }
    if (0 == dependant)
    {
	printf("Enter <1> if you are single, <0> if you are married: ");
	single = getinput();
	if (0 != single)
	{
	    line5 = 12950;
	}
	if (0 == single)
	{
	    line5 = 7200;
	}
    }

    line6 = line4 - line5;
    if (line6 < 0)
    {
	line6 = 0;
    }
    printf("Your taxable income is: ");
    write(line6);

    printf("Enter the amount of Federal income tax withheld: ");
    line7 = getinput();
    printf("Enter <1> if you get an earned income credit (EIC); ");
    printf("enter 0 otherwise: ");
    eic = getinput();
    line8 = 0;
    if (0 != eic)
    {
	printf("OK, I'll give you a thousand dollars for your credit.\n");
	line8 = 1000;
    }
    // line9 = line8 + line7;
    printf("Your total tax payments amount to: ");
    write(line9);

    line10 = (line6 * 28 + 50) / 100;
    printf("Your total tax liability is: ");
    write(line10);

    //    line11 = line9 - line10;
    if (line11 < 0)
    {
        deadline11 = 0; 
    }
    else deadline11 = 0;
    if (line11 > 0)
    {
	printf("Congratulations, you get a tax refund of $");
	write(line11);
    }

    // line12 = line10-line9;
    if (line12 >= 0)
    {
	printf("Bummer. You owe the IRS a check for $");
	write(line12);
    }
    if (line12 < 0)
    {
	deadline12 = 0;
    }
    else deadline12 = 0;

    write(line6);
    write(line9);
    write(line10);
    write(b);
    write(e);
    write(d);
    write(deadline11);
    write(deadline12);

    line6 = line10;
    line8 = 0;
    line10 = 0;
    deadline11 = b+deadline12;
    deadline12 = e+d;
    

    printf("Thank you for using ez-tax.\n");
}
