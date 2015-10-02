# intrsutction

meteor run to start the app locally

apparently anything in client with ANY valid extension will be rendered on ANY path not in public.
Why it works this way is an absolute mystery, there is no default routing in meteor? 
should be ok for this project, but if needed look at iron router`
also, there is no import function is js. wtf. really?

we are using iron router now. idk if that is saved somewhere inside the setting of meteor

# issues

ok time to restructure the database. i think we want each player to have all of its data.
actually this is a tough problem. i would like to keep the database compatible with multiplayer, but it needs serious simplification.
maybe games and players are collections? then rounds are part of games? hmm, very tough call

build some kind of data analysis, dumping mongo is a bit hard, and will require working in an unfamiliar environment. Could dump the whoel thing to a csv, but im not sure that is easier than working in js. maybe one pass with js, then generate a csv for R (or whatever)

Fuck, adding the user everytime is a bit annoying. I guess we can filiter based on existence of name
07. How are Tokens going to be incorporated? - food for thought
    - maybe some of the dice can become Tokens at times?
    - instructions should be clear on when it is time to take Tokens (or it is up to 
      the player to choose Tokens or not. Tokens can appear randomly at different 
      rounds and player may or may not choose it)
08. How is "winner" determined? Or will there be a winner at all?
    - if the below monster avatar will be incorporated then when played alone
      the too skinny monsters will lose and fat enough monsters will win???
09. Show a monster on the empty area of the game page and make it shrink/enlarge 
    depending on the calories consumed (range should be from 0/negative? up to 6000~
    7000 calories 

10. NEW NEW NEW
    I think for rounds, when each round is over the top highest caloric items should be
    REVEALED so that the player can learn which ones were the highest!!!!!!
    GOOD GOOD GOOD GOOD??????????????????

11. NEW SUGGESTION
    Have the food cards be revealed when selected for all players instead of #10

  
