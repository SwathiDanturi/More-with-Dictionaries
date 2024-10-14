**File**: Design.md <br>
**Design for all the scrabble_letters methods** <br>
**Developer**: Swathi Danturi <br>

## Design for the constructor of scrabble_letters
- `self` is the current instance of the class
- `scrabble_file` is the parameter to the constructor passed when the class instance is created
- `self.scrabble_letter` is the instance variable to store the letter frequency and points
- `letters_file` is a file variable use to open the file `scrabble_file` in read mode
- for `line` a string varibale in `letters_file`, iterate through the following:
    - `strip` the `line` to remove any extra spaces or new line
    - `split` the `line` using `,` as delimiter and assign it to the variables `letter`, `count` and `points`
    - if `count` and `points` are digits, do the following:
        - type `count` and `points` to integers
        - append them to a list variable `count_and_points`
    -map the value `count_and_points` list for the key `letter` in the dictionary `self.scrabble_letter`
- `self.scrabble_letter` contains letters as the keys and `count` and `points` as value in a list

