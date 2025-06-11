# hack_assembler
Python implementation of the nand2tetris HACK assembler.

This contains the following modules:

Other ideas:
* File Managing
  * Object for the read file
  * Object for the file to save

* Parser
  * Handles turning the lines of code into chunks based on instruction
  * A-instruction
    * most significant bit set to 0
    * the rest equivalent to the number in the address
  * C-instruction
    * most significant bit set to 1
    * Two next bits are 1
    * 6-bits for computation
    * 3-bits for destination
    * 3-bits for jump
  * Label
    * starts with either () or @
* Translator (code in original docs)
  * Handles translating the instructions into its binary parts
* SymbolTable
  * Turns any labels and pre-given symbols to the correct number
* Main
  * Orchestrates the process