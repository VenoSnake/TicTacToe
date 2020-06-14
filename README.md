# TicTacToe

**Author** : Nikhil Dandamudi

**Specialization** : Gaming, Reinforced Machine Learning(soon)

**Description** : Artificial Neural Networks Have Been A Breakthrough In Many Sectors, And Gaming Is One Of Them. This Present Repository Aims At Delivering A Never Lose AI Model (Worst Case Outcome Being A Draw). The Whole TicTacToe Game With A GUI Has Been Coded In Python From Scratch.

**Note : Currently Only The TicTacToe Game Has Been Coded, Although This Projects Aim To Deliver An AI Bot Soon, Due To Limited Time Availability And Due To The Transition From Working Under A Keras Framework To PyTorch It Would Be Taking A Bit Longer Than Expected**

# Algorithm & Architecture: 
  
## TicTacToe Game :

1) The GUI Of The TicTacToe Game Has Been Designed Through The PyGame Framework, The Screen Class In Screen.py Takes Care Of Everything Under Designing A GUI. (A Player Move Is Made By Comparing The Distance Between The Location Of Mouse Clicked And The Various Locations Of Centroid's Each Block, The One With Mininmum Distance Is Selected As The Player Move's Block)

2) The Game Logic Is Present In The TicTacToe Class In TicTacToe.py, Most Of The Logic Can Be Easily Understoon As I Did My Best To Reformat My Python Program With Proper Comments, Although I Didnt Explain About The Winning Logic In The Comments. The GameState Class In TicTacToe.py Holds The State Of The Game During Various Moves Made By The Two Opposition Parties (i.e, NAUGHT and CROSS).

3) **The Win/Draw Logic** : It Is Carried Out By Giving A WIN_CHECK_DIRECTORY (Since For Winning A Game One Of The Blocks At 0, 1, 2, 3, 6 Must Be Filled), With A Direction Vector Which Gives All The Possible States To Take A Step In That Direction And Continued To Reach The End Of The Board (For Each Tuple In The List Of Tuples), Check If In The Direction Carried Out All The Three Blocks Consist Of A Player Of Same Side. 

## Algorithm And Architecture Used In Creating The AI Bot :

**Coming Soon**

# Program In Action:

## TicTacToe Game:
