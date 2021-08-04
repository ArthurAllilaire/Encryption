# Encryption Engine (in encryption.py)
Over a two week course in Cambridge I was set teh challenge to create an encryption engine. Here is my solution to the problem.

My encryption engine has 3 steps, which are applied sequentially. To decrypt it you just pass them through the steps in the opposite direction, with the right parameters of course. The encryption engine accepts all letters (both upper and lower case), symbols and numbers, meaning there are 95 different inputs possiblities. It doesn't accept any spacing (e.g. \n or \t) apart from spaces due to formatting issues.

## Enigma 2.0 (in enigma.py)
The first encryption layer is a software representation of the German enigma machine. It follows the same steps of passing the input through a plugboard, then a series of rotors, through a reflector and then back through the rotors and the plugboard. For more information: https://www.scienceabc.com/innovation/the-imitation-game-how-did-the-enigma-machine-work.html

However, the enigma machine was crackable because a letter couldn't be enconded as itself, this was due to hardware problems. Enigma 2.0 can encrypt a letter to itself. Furthermore, enigma 2.0 is not limited to 3 rotors like the normal enigma machines, you can have as many rotors as you want, effectively making the machine have infinite possible parameters for encryption, this makes it uncrackable.

## Mirror (in mirror.py)
The second encryption layer effectively scrambles the orders of the letters. It is given a list of numbers, which represent number of times the string should be split, it then goes through each neighbouring split and swaps them round and mirrors each split, it repeats this for every number. If you pass a long enough list of numbers the letters become pseudo-randomly shuffled. However, it can easily be decrypted as long as you know the original list of numbers used.

## Substitution cypher (in changeChars.py)
This is a substitution cypher. For every letter passed in it is replaced by one of 4 randomly generated strings of from 4 to 10 letters long, seperated by as many potential dividers as wanted.

# Possible Improvements
## User friendliness
The main improvement would be to get the ability to set the parameters for the engine through a GUI instead of having to go into the code. Also have the ability to set the parameters to decode messages from a different session, currently not possible as everything is randomly generated every time the program is run.

## Key transimission
The main flaw with this encryption is that the key has to be transmitted to whoever wants to decrypt the message, and the key is also quite long. Would need to implement a public and private key for this to be a viable communication encryption engine.

