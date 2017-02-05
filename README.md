## Inspiration
The Inspiration behind <b>a2b</b> was derived from an idea we had at a google case competition when we were told to come up with an idea to give back to our local community. When thinking about the larger issues that exist near Kean & Rutgers University, we realized one of the largest issues that both near by communities suffers from is lack of opportunity for the homeless. After some private research, we found that 87% of homeless people have access to flip phones - thus there is an opportunity to reach out and help via technology. 

## What it does
<b>a2b</b>'s core purpose is to allow for homeless people to reach out for directions, food, shelter, and job opportunities without needing access to the internet. By letting the homeless send texts to our server, we then can return a message that caters to their needs. 

#### Example Interaction:
```
Directions:
Rockefeller Center
Time Square
```

```
1.)  Head southwest on 5th Ave toward W 50th St

2.)  Turn right onto W 47th St

3.)  Turn left at the 2nd cross street onto 7th Ave
```

## How we built it
<b>a2b</b> was built using several different technologies: 
1. **Flask & Python**: Python Server. 
2. **HTML/CSS/JS**: Front-end of the <b>a2b</b> website that allows for companies and local services to sign up and publicize their charity.
3. **Twilio**: API that allows <b>a2b</b> to send, receive, and interact with SMS technology.
4. **Google Maps**: API that allows <b>a2b</b> to receive directions between an origin and destination.  
5. **Ngrok**: A http-tunneling service that allows for a local hosted application to be accessed from a public IP address.  

## Challenges we ran into
The first and most crippling issue was getting here 12 hours late. As for technical issues, parsing directions from a google map API encoded .json, using JS and CSS for the first time, as well as switching from Windows to Ubuntu at 3:00 AM.  

## Accomplishments that we're proud of
It actually works!

## What we learned
How to publicly host a locally hosted application via Ngrok, the google maps API, how to traverse a .json, JavaScript, and CSS.

## What's next for a2b
The next step for <b>a2b</b> is getting our name out to our local communities and companies that are aware of our communities necessities.  
