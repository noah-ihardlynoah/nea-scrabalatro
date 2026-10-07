# nea-scrabalatro
AQA CompSci A-Level Non-Exam Assessment (NEA).A remake of the popular roguelite Balatro with Scrabble tiles.

To do list:
-
/1. Decide hands and scoring                                         DONE
2. Modify power-up tiles around the new hands. (aim for 150)
2a. Find images for all power-ups
3. Design power-up tiles and different skins for regular tiles.
4. Code front end in JS.
5. Add tutorial.

Hands (ascending base score):
-
-1/2/3 tiles-
High Tile           5   X   1
2L                  10  X   2
2x2L                20  X   2
3L                  30  X   3
-4/5 tiles-
Noun                30  X   4   Str
Verb                35  X   4   Flu
Adjective           40  X   4   Ful
Adverb              60  X   7   Fou
Abstract Noun       100 X   8   StrFlu
-No Secret Hands-

Power-up Tiles:
-
1. C Jimbo                +4 mult

2. C Jolly                +8 mult if word contains a 2L
3. C Zany                 +12 mult if word contains a 3L
4. C Mad                  +10 mult if word contains 2x2L
5. C Crazy                +12 mult if word contains Noun
6. C Droll                +10 mult if word contains Verb

7. C Sly                  +50 points if word contains a 2L
8. C Wily                 +100 points if word contains a 3L
9. C Clever               +80 points if word contains 2x2L
10. C Crazy               +100 points if word contains Noun
11. C Crafty              +80 points if word contains Verb

12. C Half                +20 mult if word contains 3 or fewer tiles
13. U Stencil             X1 mult for each empty Power-up slot, incl. Stencil (currently X5)
14. U Mime                Retrigger all tile held in hand abilities
15. C Credit Card         Go up to -$20 in debt
16. U Ceremonial Dagger   When round is selected, destroy Power-up tile to the right and add double its sell value to this mult.
17. C Banner              +30 points for each remaining exchange.
18. C Mystic Summit       +15 mult when 0 exchanges remaining
19. U Marble              Adds one Stone tile to bag when round is selected
20. U Loyalty Card        X4 mult every 6 words played (5 remaining)
21. C Egg                 Gains $3 of sell value at end of round
22. C Misprint            +n mult (import time?)
23. U Dusk                Retrigger all played tiles in final word of round
24. C Raised Fist         Adds double the points of lowest scoring tile held in hand to mult
25. C Chaos               1 free Reroll per shop
26. U Space               1 in 4 chance to upgrade level of played word type.
27. C Night Vowel         Played ##vowels## give +30 points when scored
28. C Abstract            +3 mult for each Power-up tile (currently +0 mult)
29. C Delayed Gratification Earn $2 per exchange if no exchanges used by end of round
30. U Hack                Retrigger each played ##H, A, C or K##
31. U Perceptual Epenthesis All tiles are considered ##vowels##
32. C Gros Michel         +15 mult, 1 in 6 chance this tile is destroyed at end of round.
33. C Cavendish           X3 mult, 1 in 1000 chance this card is destroyed at end of round
34. U Limited Vocabulary  X3 mult if played word type has already been played this round
35. C Supernova           Adds the number of times word type has been played this run to mult
36. U Burglar             When round is selected gain +3 words and lose all exchanges.
37. C Runner              Gains +15 points if played word contains a Noun
38. C Ice Cream           +100 points, -5 points for every word played.
39. R DNA                 If first word of round is a High Tile, add a permanent copy to bag and draw to hand
40. C Splash              Every played tile counts in scoring
41. C Blue                +1 point for each remaining tile in bag (currently +100 points)
42. U Thixth Thenth       If first word of round is a single S, dethtroy it and create a Thpectral card. (Muth have room)
43. U Constellation       This Power-up gains X0.1 mult every time a Planet card is used.
44. U Hiker               Every played tile permanently gains +5 points when scored.
45. C Green               +1 mult per word played, -1 mult per exchange (currently +0 mult)
46. C To Do List          Earn $4 if word is a ____, word type changes each round.
47. C Red Tile            This Power-up gains +3 mult when any Booster Pack is skipped (currently +0 mult)
48. U Madness             When Round 1 or Round 2 is selected, gain X0.5 mult and destroy a random Power-up.
49. C Square              This Power-up gains +4 points if played word has exactly 4 tiles (currently 0 points)
50. U Séance              If word played is an Abstract Noun, create a random Spectral card.
51. C Riff-Raff           When round is selected, create 2 Common power-ups
52. U Vampire             Gains X0.1 mult per scoring Enhanced tile played, removes tile Enhancement (Currently X1 mult)
53. U Hologram            This Power-up gains X0.25 mult every time a tile is added to your bag (currently X1 mult)
54. R Vagabond            Create a Tarot card if word is played with $4 or less
55. R Chastit-E           Each E held in hand gives X1.5 mult
56. U L Skills            Earn $1 for each L in your full bag at end of round. (Currently $0)
57. U Rocket              Earn $1 at end of round. Payout increases by $2 when Boss is defeated.
58. R Obelisk  This Power-up gains X0.2 Mult per consecutive word played without playing your most played word type (Currently X1 mult)
59. U Midas Mask All played vowels become Gold cards when scored
60. U Luchador Sell this card to disable the current Boss's ability.
61. C Photograph First played vowel gives X2 mult when scored
62. U Gift Card Add $1 of sell value to every Power-up tile and Consumable at end of round.
62. U Turtle Bean +5 hand size, reduces by 1 each round.
63. U Erosion +2 mult for each tile below 100 in your full bag.
64. C Reserved Parking Each vowel held in hand has a 1 in 2 chance to give $1.
65. C Mail-In Rebate Earn $5 for each discarded __, letter changes every round.
66. U To the Moon Earn an extra $1 of interest for every $5 you have at end of round.
67. C Hallucination 1 in 2 chance to create a Tarot card when any Booster Pack is opened.
68. C Fortune Teller +1 Mult per Tarot card used this run.
69. C Juggler +1 hand size
70. C Drunkard +1 discard each round
71. C Golden Earn $4 at end of round.
72. U Lucky Cat This Power-up gains X0.25 Mult every time a Lucky tile successfully triggers (Currently X1 Mult)
73. R Baseball Card Uncommon Power-ups each give X1.5 mult
74. U Bull +2 points for each $1 you have (Currently +0 points)
75. U Diet Cola Sell this card to create a free Double Tag
76. U Trading Card If first exchange of round has only 1 tile, destroy it and earn $3.
77. U Flash Card This power-up gains +2 mult per reroll in the shop
78. C Popcorn +20 mult, -4 mult per round played.
79. U Spare Trousers This Power-up gains +2 mult if played hand contains a 2x2L (Currently +0 mult)
80. U Ramen X2 mult, loses X0.01 mult per card discarded
81. C Walkie Talkie Each played 10 or 4 gives +10 points and +4 mult when scored
81. U Seltzer Retrigger all tiles played for the next 10 words.
82. C Smiley Face Played vowels give +5 mult when scored.
83. U Mr Bones Prevents death if points scored are at least 25% of required points, self destructs
84. U Acrobat X3 mult on final word of round
85. U Joey Ramone Retrigger all played vowels.
86. C Swashbuckler Adds the sell value of all other owned Power-ups to Mult. (Currently +0 mult)
87. U Troubadour +2 hand size, -1 word each round.
88. U Certificate When round begins, add a random letter tile with a random seal to your hand.
89. U Throwback X0.25 mult for each round skipped this run (Currently X1 mult)
90. C Hanging Chad Retrigger first played tile used in scoring 2 additional times
91. U Showman    Power-up, Tarot, Planet, and Spectral cards may appear multiple times
92. R Blueprint Copies ability of Power-up to the right
93. U Oops! All 6s Doubles all listed probabilities (e.g. 1 in 3 -> 2 in 3)
94. U Matador Earns $8 if played hand triggers the Boss's ability.
95. R Mini Phagocyte X2 mult if played 5-letter word contains a 2L. 
96. R Phagocyte X3 mult if played 5 letter word contains a 3L. 
97. R Mega Phagocyte X4 mult if played 5-letter word contains a 4-letter word.
98. R Brainstorm Copies left-most power-up
99. R Driver's license X3 mult if you have at least 17 enhanced tiles in full bag.
100. U Cartomancer Create a Tarot card when round is selected.
101. U Astronomer, all Planet cards and Celestial Packs in the shop are free.
102. R Burnt Joker Upgrade the level of the first discarded word type each round.
103. R Campfire This Power-up gains X0.25 mult for each card sold, resets when Boss is defeated.

-
LEGENDARIES
1. Canio this Power-up gains X1 mult when a vowel is destroyed.
2. Yorick This Power-up gains X1 mult every 23 tiles discarded (Currently X1 mult)
3. Chicot Disables effect of every boss blind.
4. Perkeo Creates a negative copy of one random consumable card in your possession at the end of the shop




-
NOT USED:
Greedy, Lusty, Wrathful, Gluttonous (+3 mult for each suit, hard to replicate suits)
Four Fingers (can be 4 letters anyway)
Scholar (4/20)
Ride the Bus (doable, but not with vowels)
8 Ball
Fibonacci
Business Card
Blackboard
Faceless Joker
Superposition
Even Steven
Odd Todd
Shortcut
Ancient Joker
Castle
Campfire
Smeared
Flower Pot
Wee Joker
Bootstraps
L - Triboulet
