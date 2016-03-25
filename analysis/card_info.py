bad_cards = ["Boar Cookie"
            ,"Walrus Pretzels"
            ,"Rooster Potato Chips"
            ,"Fox Chocolate Bar"
            ,"Wolf crackers"
            ,"Donkey Popsicle"
            ,"Hedgehog PB cup"
            ,"Cougar Popcorn"
            ,"Tiger Protein Bar"
            ,"Bear tortilla chips"
            ,"Beaver Brownie"
            ,"Pig Candy"]
ok_cards = ["Fox Cookie"
            ,"Penguin Pretzels"
            ,"Rabbit Potato Chips"
            ,"Eagle Chocolate Bar"
            ,"Duck crackers"
            ,"Reindeer Popsicle"
            ,"Elk PB cup"
            ,"Owl Popcorn"
            ,"Squirrel Protein Bar"
            ,"Owl tortilla chips"
            ,"Monkey Brownie"
            ,"Leopard Candy"]
good_cards = ["Cow Cookie"
            ,"Zebra Pretzels"
            ,"Panther Potato Chips"
            ,"Moose Chocolate Bar"
            ,"Lion crackers"
            ,"Goat Popsicle"
            ,"Bear PB cup"
            ,"Sheep Popcorn"
            ,"Elephant Protein Bar"
            ,"Orangutan tortilla chips"
            ,"Panda Brownie"
            ,"Hen Candy"]

fake_cards = ok_cards+bad_cards+good_cards

if (len(ok_cards)!=len(good_cards) or len(bad_cards)!=len(good_cards)):
  sys.exit("bad card input lengths")
