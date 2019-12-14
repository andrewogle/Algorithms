#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = None 
    check_ing = 0
    for i in recipe:
      if i in ingredients:
        check_ing = ingredients[i] // recipe[i]
      
        if batches == None:
          batches = check_ing
        elif batches > check_ing:
          batches = check_ing
      else:
        return 0
    return batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))