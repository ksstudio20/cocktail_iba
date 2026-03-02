#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from typing import Dict, List

COCKTAILS: List[Dict] = [
  {
    "name": "Alexander",
    "base": "Brandy",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml Cognac",
      "30 ml Crème de Cacao (Brown)",
      "30 ml Fresh Cream"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker filled with ice cubes.",
      "Shake and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Americano",
    "base": "Unknown",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml Bitter Campari",
      "30 ml Sweet Red Vermouth",
      "A splash of Soda Water"
    ],
    "steps": [
      "Mix the ingredients directly in an old fashioned glass filled with ice cubes.",
      "Add a splash of Soda Water. Stir gently."
    ]
  },
  {
    "name": "Angel Face",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml Gin",
      "30 ml Apricot Brandy",
      "30 ml Calvados"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker filled with ice cubes.",
      "Shake and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Aviation",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Gin",
      "15 ml Maraschino Luxardo",
      "15 ml Fresh Lemon Juice",
      "1 Bar Spoon Crème de Violette"
    ],
    "steps": [
      "Add all ingredients into a cocktail shaker.",
      "Shake with cracked ice and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Bee’s Knees",
    "base": "Gin",
    "taste": "New Era",
    "ingredients": [
      "52.5 ml Dry Gin",
      "2 teaspoons Honey Syrup",
      "22.5 ml Fresh Lemon Juice",
      "22.5 ml Fresh Orange Juice"
    ],
    "steps": [
      "Stir honey with lemon and orange juices until it dissolves, add gin and shake with ice. Strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Bellini",
    "base": "Sparkling Wine",
    "taste": "Contemporary Classics",
    "ingredients": [
      "100 ml Prosecco",
      "50 ml White Peach Puree"
    ],
    "steps": [
      "Pour peach puree into the mixing glass with ice, add the Prosecco wine.",
      "Stir gently and pour in a chilled flute glass.",
      "NOTE:\nPuccini – Fresh Mandarin Orange Juice;\nRossini – Fresh Strawberry Puree;\nTintoretto –  Fresh Pomegranate Juice."
    ]
  },
  {
    "name": "Between the Sheets",
    "base": "Rum",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml White Rum",
      "30 ml Cognac",
      "30 ml Triple Sec",
      "20 ml Fresh Lemon Juice"
    ],
    "steps": [
      "Add all ingredients into a cocktail shaker.",
      "Shake with ice and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Black Russian",
    "base": "Vodka",
    "taste": "Contemporary Classics",
    "ingredients": [
      "50 ml Vodka",
      "20 ml Coffee Liqueur"
    ],
    "steps": [
      "Pour the ingredients into the old fashioned glass filled with ice cubes.",
      "Stir gently. strain ingredients into old fashioned glass filled with ice.",
      "NOTE:\nWHITE RUSSIAN – Float fresh cream on the top and stir in slowly."
    ]
  },
  {
    "name": "Bloody Mary",
    "base": "Vodka",
    "taste": "Contemporary Classics",
    "ingredients": [
      "45 ml Vodka",
      "90 ml Tomato Juice",
      "15 ml Fresh Lemon Juice",
      "2 dashes Worcestershire Sauce",
      "Tabasco, Celery Salt, Pepper (Up to taste)"
    ],
    "steps": [
      "Stir gently all the ingredients in a mixing glass with ice, pour into rocks glass.",
      "NOTE:\nIf requested served with ice, pour into highball glass."
    ]
  },
  {
    "name": "Boulevardier",
    "base": "Whiskey",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Bourbon or Rye Whiskey",
      "30 ml Bitter Campari",
      "30 ml Sweet Red Vermouth"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes.",
      "Stir well. Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Bramble",
    "base": "Gin",
    "taste": "New Era",
    "ingredients": [
      "50 ml Gin",
      "25 ml Fresh Lemon Juice",
      "12.5 ml Sugar Syrup",
      "15 ml Crème de Mûre"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker except the Crème de Mûre, shake well with ice, strain into chilled old fashioned glass filled with crushed ice, then pour the blackberry liqueur (Crème de Mûre) over the top of the drink, in a circular motion."
    ]
  },
  {
    "name": "Brandy Crusta",
    "base": "Brandy",
    "taste": "The Unforgettables",
    "ingredients": [
      "52.5 ml Brandy",
      "7.5 ml Maraschino Luxardo",
      "1 Bar Spoon Curacao",
      "15 ml Fresh Lemon Juice",
      "1 Bar Spoon Simple Syrup",
      "2 Dashes Aromatic Bitters"
    ],
    "steps": [
      "Mix together all ingredients with ice cubes in a mixing",
      "glass and strain into a prepared slim cocktail glass."
    ]
  },
  {
    "name": "Caipirinha",
    "base": "Unknown",
    "taste": "Contemporary Classics",
    "ingredients": [
      "60 ml Cachaça",
      "1 Lime cut into small wedges",
      "4 Teaspoons White Cane Sugar"
    ],
    "steps": [
      "Place lime and sugar into a double old fashioned glass and muddle gently.",
      "Fill the glass with cracked ice and add Cachaça. Stir gently to involve ingredients.",
      "Note:\nCaipiroska – Instead of Cachaça use Vodka;\nCaipirissima – Instead of Cachaça use Rum.\nCaipirão – Instead of Cachaça use Licor Beirão."
    ]
  },
  {
    "name": "Canchanchara",
    "base": "Unknown",
    "taste": "New Era",
    "ingredients": [
      "60 ml Cuban Aguardiente",
      "15 ml Fresh Lime Juice",
      "15 ml Raw Honey",
      "50 ml Water"
    ],
    "steps": [
      "Mix honey with water and lime juice and spread the mixture on the bottom and sides of the glass.",
      "Add cracked ice, and then the rum.",
      "End by energetically stirring from bottom to top."
    ]
  },
  {
    "name": "Cardinale",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "40 ml Gin",
      "20 ml Dry Vermouth",
      "10 ml Bitter Campari"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes. Stir well.",
      "Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Casino",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "40 ml Old Tom Gin",
      "10 ml Maraschino Luxardo",
      "10 ml Fresh Lemon Juice",
      "2 Dashes Orange Bitters"
    ],
    "steps": [
      "Pour all ingredients into cocktails shaker, shake well with ice, strain",
      "into chilled rocks glass with ice."
    ]
  },
  {
    "name": "Champagne Cocktail",
    "base": "Brandy",
    "taste": "Contemporary Classics",
    "ingredients": [
      "90 ml Chilled Champagne",
      "10 ml Cognac",
      "2 dashes Angostura bitters",
      "Few drops of Grand Marnier (optional)",
      "1 sugar cube"
    ],
    "steps": [
      "Place the sugar cube with 2 dashes of bitters in a large Champagne glass, add the cognac.",
      "Pour gently chilled Champagne."
    ]
  },
  {
    "name": "Chartreuse Swizzle",
    "base": "Unknown",
    "taste": "New Era",
    "ingredients": [
      "45 ml Green Chartreuse",
      "30 ml Fresh Pineapple Juice",
      "22.5 ml Fresh Lime Juice",
      "15 ml Falernum"
    ],
    "steps": [
      "Pour all ingredients into a tall glass, add pebble ice.",
      "With the help of a swizzle stick (or cocktail spoon) mix vigorously, complete by filling the glass with more pebble ice."
    ]
  },
  {
    "name": "Clover Club",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Gin",
      "15 ml Raspberry Syrup",
      "15 ml Fresh Lemon Juice",
      "Few Drops of Egg White"
    ],
    "steps": [
      "Pour all ingredients into cocktails shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Corpse Reviver #2",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "30 ml Gin",
      "30 ml Cointreau",
      "30 ml Lillet Blanc",
      "30 ml Fresh Lemon Juice",
      "1 dash Absinthe"
    ],
    "steps": [
      "Pour all ingredients into shaker with ice.",
      "Shake well and strain in chilled cocktail glass."
    ]
  },
  {
    "name": "Cosmopolitan",
    "base": "Vodka",
    "taste": "Contemporary Classics",
    "ingredients": [
      "40 ml Vodka Citron",
      "15 ml Cointreau",
      "15 ml Fresh Lime Juice",
      "30 ml Cranberry Juice"
    ],
    "steps": [
      "Add all ingredients into cocktail shaker filled with ice.",
      "Shake well and strain into large cocktail glass."
    ]
  },
  {
    "name": "Cuba Libre",
    "base": "Rum",
    "taste": "Contemporary Classics",
    "ingredients": [
      "50 ml White Rum",
      "120 ml Cola",
      "10 ml Fresh Lime Juice"
    ],
    "steps": [
      "Build all ingredients in a highball glass filled with ice."
    ]
  },
  {
    "name": "Daiquiri",
    "base": "Unknown",
    "taste": "The Unforgettables",
    "ingredients": [
      "60 ml White Cuban Ron",
      "20 ml Fresh Lime Juice",
      "2 Bar Spoons Superfine Sugar"
    ],
    "steps": [
      "In a cocktail shaker add all ingredients. Stir well to dissolve the sugar.",
      "Add ice and shake. Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Dark ‘N’ Stormy",
    "base": "Gin",
    "taste": "New Era",
    "ingredients": [
      "60 ml Goslings Rum",
      "100 ml Ginger Beer"
    ],
    "steps": [
      "In a highball glass filled with ice pour the ginger beer and top floating with the Rum."
    ]
  },
  {
    "name": "Don’s Special Daiquiri",
    "base": "Rum",
    "taste": "New Era",
    "ingredients": [
      "30 ml Gold Jamaican Rum",
      "15 ml Cuban Rum",
      "15 ml Passion Fruit Syrup",
      "15 ml Fresh lime juice",
      "15 ml Honey Syrup"
    ],
    "steps": [
      "Blend for a few seconds in a milkshake mixer with  crushed ice and pour into a footed copo glass.",
      "Fill the glass with more crushed ice."
    ]
  },
  {
    "name": "Dry Martini",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "60 ml Gin",
      "10 ml Dry Vermouth"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes. Stir well.",
      "Strain into chilled martini cocktail glass."
    ]
  },
  {
    "name": "Espresso Martini",
    "base": "Vodka",
    "taste": "New Era",
    "ingredients": [
      "50 ml Vodka",
      "30 ml Kahlúa",
      "10 ml Sugar Syrup",
      "1 strong Espresso"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Fernandito",
    "base": "Unknown",
    "taste": "New Era",
    "ingredients": [
      "50 ml Fernet Branca",
      "Fill up with Cola"
    ],
    "steps": [
      "Pour the Fernet Branca into a double old fashioned glass with ice, fill the glass up with Cola. Gently stir."
    ]
  },
  {
    "name": "French 75",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "30 ml Gin",
      "15 ml Fresh Lemon Juice",
      "15 ml Sugar Syrup",
      "60 ml Champagne"
    ],
    "steps": [
      "Pour all the ingredients, except Champagne, into a shaker.",
      "Shake well and strain into a Champagne flute.",
      "Top up with Champagne.",
      "Stir gently."
    ]
  },
  {
    "name": "French Connection",
    "base": "Brandy",
    "taste": "Contemporary Classics",
    "ingredients": [
      "35 ml Cognac",
      "35 ml Amaretto"
    ],
    "steps": [
      "Pour all ingredients directly into old fashioned glass filled with ice cubes.",
      "Stir gently."
    ]
  },
  {
    "name": "French Martini",
    "base": "Vodka",
    "taste": "New Era",
    "ingredients": [
      "45 ml Vodka",
      "15 ml Raspberry Liqueur",
      "15 ml Fresh Pineapple Juice"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Garibaldi",
    "base": "Unknown",
    "taste": "Contemporary Classics",
    "ingredients": [
      "45 ml Bitter Campari",
      "120 ml Freshly Squeezed Orange Juice"
    ],
    "steps": [
      "Build all ingredients in a highball glass filled with ice."
    ]
  },
  {
    "name": "Gin Basil Smash",
    "base": "Gin",
    "taste": "New Era",
    "ingredients": [
      "60ml Gin",
      "22.5 ml Freshly Squeezed Lemon Juice",
      "22.5 ml Sugar Syrup",
      "10 pcs Italian Basil leaves"
    ],
    "steps": [
      "Add all ingredients into shaker with ice.",
      "Shake vigorously and pour into chilled cocktail glass."
    ]
  },
  {
    "name": "Gin Fizz",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Gin",
      "30 ml Fresh Lemon Juice",
      "10 ml Simple Syrup",
      "Splash of Soda Water"
    ],
    "steps": [
      "Shake all ingredients with ice except soda water.",
      "Pour into thin tall Tumbler glass , top with a splash soda water.",
      "NOTE:\nServe without ice."
    ]
  },
  {
    "name": "Grand Margarita",
    "base": "Tequila",
    "taste": "New Era",
    "ingredients": [
      "45 ml Tequila 100% agave",
      "30 ml  Grand Marnier",
      "15 ml Fresh Lime Juice"
    ],
    "steps": [
      "Rim the rock glass with good quality sea salt. Pour the ingredients into the  shaker.",
      "Add ice to both glass and shaker.",
      "Shake hard for 10 seconds. Strain the drink into the glass."
    ]
  },
  {
    "name": "Grasshopper",
    "base": "Unknown",
    "taste": "Contemporary Classics",
    "ingredients": [
      "20 ml Crème de Cacao (White)",
      "20 ml Crème de Menthe (Green)",
      "20 ml Fresh Cream"
    ],
    "steps": [
      "Pour all ingredients into shaker filled with ice.",
      "Shake briskly for few seconds. Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Hanky Panky",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml London Dry Gin",
      "45 ml Sweet Red Vermouth",
      "7.5 ml Fernet"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes. Stir well.",
      "Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Hemingway Special",
    "base": "Rum",
    "taste": "Contemporary Classics",
    "ingredients": [
      "60 ml Rum",
      "40 ml Grapefruit Juice",
      "15 ml Maraschino Luxardo",
      "15 ml Fresh Lime"
    ],
    "steps": [
      "Pour all ingredients into a shaker with ice.",
      "Shake well and strain into a large cocktail glass."
    ]
  },
  {
    "name": "Horse’s Neck",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "40 ml Cognac",
      "120 ml Ginger Ale",
      "Dash of Angostura Bitters (optional)"
    ],
    "steps": [
      "Pour Cognac and ginger ale directly into highball glass with ice cubes.",
      "Stir gently.",
      "If preferred, add dashes of Angostura Bitter."
    ]
  },
  {
    "name": "IBA Tiki",
    "base": "Unknown",
    "taste": "New Era",
    "ingredients": [
      "30 ml Ron Profundo Havana Club",
      "30 ml Ron Smoky Havana Club",
      "15 ml Licor Amaretto",
      "5 ml Licor Frangelico",
      "5 drops Maraschino Luxardo",
      "30 ml Passion Fruit Puree",
      "90 Fresh Pineapple Juice",
      "30 Fresh Lime Juice",
      "1 pc Gengibre Slice"
    ],
    "steps": [
      "In a cocktail shaker muddle a thin slice of Gengibre, Pour all other ingredients.",
      "Shake vigorously with ice.",
      "Strain into a chilled Tiki glass filled with pebbled ice."
    ]
  },
  {
    "name": "Illegal",
    "base": "Rum",
    "taste": "New Era",
    "ingredients": [
      "30 ml Espadin Mezcal",
      "15 ml Jamaica Overproof White Rum",
      "15 ml Falernum",
      "1 Bar Spoon Maraschino Luxardo",
      "22.5 ml Fresh Lime Juice",
      "15 ml Simple Syrup",
      "Few Drops of Egg White (Optional)"
    ],
    "steps": [
      "Pour all ingredients into the shaker. Shake vigorously with ice.",
      "Strain into a chilled cocktail glass, or “on the rocks” in a traditional clay or terracotta mug."
    ]
  },
  {
    "name": "Irish Coffee",
    "base": "Whiskey",
    "taste": "Contemporary Classics",
    "ingredients": [
      "50 ml Irish Whiskey",
      "120 ml Hot coffee",
      "50 ml Fresh cream (Chilled)",
      "1 teaspoon Sugar"
    ],
    "steps": [
      "Warm black coffee is poured into a preheated Irish coffee glass.",
      "Whiskey and at least one teaspoon of sugar is added and stirred until dissolved.",
      "Fresh thick chilled cream is carefully poured over the back of a spoon held just above the surface of the coffee.",
      "The layer of cream will float on the coffee without mixing.",
      "Plain sugar can be replaced with sugar syrup"
    ]
  },
  {
    "name": "John Collins",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Gin",
      "30 ml Fresh Lemon Juice",
      "15 ml Simple Syrup",
      "60 ml  Soda Water"
    ],
    "steps": [
      "Pour all ingredients directly into highball filled with ice. Stir gently.",
      "NOTE:\nUse ‘Old Tom’ Gin for Tom Collins."
    ]
  },
  {
    "name": "Jungle Bird",
    "base": "Rum",
    "taste": "New Era",
    "ingredients": [
      "45 ml Blackstrap rum",
      "22.5 ml Campari",
      "45 ml Pineapple juice",
      "15 ml Freshly Squeezed Lime juice",
      "15 ml Demerara sugar syrup"
    ],
    "steps": [
      "Pour all ingredients into a shaker with ice and shake.",
      "Strain into a rocks glass filled with ice."
    ]
  },
  {
    "name": "Kir",
    "base": "Unknown",
    "taste": "Contemporary Classics",
    "ingredients": [
      "90 ml Dry White Wine",
      "10 ml Crème de Cassis"
    ],
    "steps": [
      "Pour Crème de Cassis into glass, top up with white wine.",
      "NOTE:\nKir Royal – Use Champagne instead of white wine"
    ]
  },
  {
    "name": "Last Word",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "22.5 ml Gin",
      "22.5 ml Green Chartreuse",
      "22.5 ml Maraschino Luxardo",
      "22.5 ml Fresh Lime Juice"
    ],
    "steps": [
      "Add all ingredients into a cocktail shaker.",
      "Shake with ice and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Lemon Drop Martini",
    "base": "Vodka",
    "taste": "Contemporary Classics",
    "ingredients": [
      "30 ml Vodka",
      "20 ml Triple Sec",
      "15 ml Fresh Squeezed Lemon Juice"
    ],
    "steps": [
      "Pour all ingredients into a shaker with ice.",
      "Shake well and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Long Island Iced Tea",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "15 ml Vodka",
      "15 ml Tequila",
      "15 ml White rum",
      "15 ml Gin",
      "15 ml Cointreau",
      "25 ml Lemon juice",
      "30 ml Simple syrup",
      "Top with Cola"
    ],
    "steps": [
      "Add all ingredients into highball glass filled with ice.",
      "Stir gently."
    ]
  },
  {
    "name": "Mai-Tai",
    "base": "Rum",
    "taste": "Contemporary Classics",
    "ingredients": [
      "30 ml Amber Jamaican Rum",
      "30 ml Martinique Molasses Rhum*",
      "15 ml Orange Curacao",
      "15 ml Orgeat Syrup (Almond)",
      "30 ml Fresh Squeezed Lime Juice",
      "7.5 ml Simple Syrup"
    ],
    "steps": [
      "Add all ingredients into a shaker with ice.",
      "Shake and pour into a double rocks glass or an highball glass.",
      "* The Martinique molasses rum used by Trader Vic was not an Agricole Rhum but a type of “rummy” from molasses."
    ]
  },
  {
    "name": "Manhattan",
    "base": "Whiskey",
    "taste": "The Unforgettables",
    "ingredients": [
      "50 ml Rye Whiskey",
      "20 ml Sweet Red Vermouth",
      "1 dash Angostura Bitters"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes.",
      "Stir well. Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Margarita",
    "base": "Tequila",
    "taste": "Contemporary Classics",
    "ingredients": [
      "50 ml Tequila 100% Agave",
      "20 ml Triple Sec",
      "15 ml Freshly Squeezed Lime Juice"
    ],
    "steps": [
      "Add all ingredients into a shaker with ice.",
      "Shake and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Martinez",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml London Dry Gin",
      "45 ml Sweet Red Vermouth",
      "1 Bar Spoon Maraschino Luxardo",
      "2 Dashes Orange Bitters"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes.",
      "Stir well. Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Mary Pickford",
    "base": "Rum",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml White Rum",
      "45 ml Fresh Pineapple Juice",
      "7.5 ml Maraschino Luxardo",
      "5 ml Grenadine Syrup"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Mimosa",
    "base": "Sparkling Wine",
    "taste": "Contemporary Classics",
    "ingredients": [
      "75 ml Freshly Squeezed  Orange Juice",
      "75 ml Prosecco"
    ],
    "steps": [
      "Pour orange juice into flute glass and gently pour the sparkling wine.",
      "Stir gently.",
      "NOTE:\nAlso known as Buck’s Fizz."
    ]
  },
  {
    "name": "Mint Julep",
    "base": "Whiskey",
    "taste": "Contemporary Classics",
    "ingredients": [
      "60 ml Bourbon Whiskey",
      "4 fresh Mint sprigs",
      "1 tsp Powdered Sugar",
      "2 tsp Water"
    ],
    "steps": [
      "In Julep Stainless Steel Cup gently muddle the mint with sugar and water.",
      "Fill the glass with cracked ice, add the Bourbon and stir well until the cup frosts."
    ]
  },
  {
    "name": "Missionary’s Downfall",
    "base": "Rum",
    "taste": "New Era",
    "ingredients": [
      "30 ml White rum",
      "15 ml Peach Brandy",
      "15 ml Fresh lime juice",
      "30 ml Honey Mix",
      "10 pcs Mint Leaves",
      "3 to 4 pcs Pineapple Chunks"
    ],
    "steps": [
      "Blend all the ingredients with half cup of crushed ice.",
      "Serve it in a Coppa grande."
    ]
  },
  {
    "name": "Mojito",
    "base": "Unknown",
    "taste": "Contemporary Classics",
    "ingredients": [
      "45 ml White Cuban Ron",
      "20 ml  Fresh Lime Juice",
      "6 pcs Mint Sprigs",
      "2 tsp White Cane Sugar",
      "Soda Water"
    ],
    "steps": [
      "Mix mint springs with sugar and lime juice.",
      "Add splash of soda water and fill the glass with ice.",
      "Pour the rum and top with soda water. Light stir to involve all ingredients."
    ]
  },
  {
    "name": "Monkey Gland",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Dry Gin",
      "45 ml Fresh Orange Juice",
      "1 Tablespoon Absinthe",
      "1 Tablespoon Grenadine Syrup"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Moscow Mule",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "45 ml Smirnoff Vodka",
      "120 ml Ginger Beer",
      "10 ml Fresh lime juice"
    ],
    "steps": [
      "In an Mule Cup or rocks glass, combine the vodka and ginger beer.",
      "Add lime juice and gently stir to involve all ingredients."
    ]
  },
  {
    "name": "Naked and Famous",
    "base": "Tequila",
    "taste": "New Era",
    "ingredients": [
      "22.5 ml Mezcal",
      "22.5 ml Yellow Chartreuse",
      "22.5 ml Aperol",
      "22.5 ml Fresh Lime Juice"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Negroni",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml Gin",
      "30 ml Bitter Campari",
      "30 ml Sweet Red Vermouth"
    ],
    "steps": [
      "Pour all ingredients directly into chilled old fashioned glass filled with ice.",
      "Stir gently."
    ]
  },
  {
    "name": "New York Sour",
    "base": "Whiskey",
    "taste": "New Era",
    "ingredients": [
      "60 ml Rye Whiskey or Bourbon",
      "22.5 ml Simple syrup",
      "30 ml Fresh lemon juice",
      "Few Drops of Egg White",
      "15 ml Red wine (Shiraz or Malbech)"
    ],
    "steps": [
      "Pour all ingredients into the shaker. Shake vigorously with ice.",
      "Strain into a chilled rocks glass filled with ice. Float the wine on top."
    ]
  },
  {
    "name": "Old Cuban",
    "base": "Rum",
    "taste": "New Era",
    "ingredients": [
      "6/8 pcs Mint Leaves",
      "45 ml Aged Rum",
      "22.5 ml Fresh Lime Juice",
      "30 ml Simple Syrup",
      "2 Dashes Angostura Bitters",
      "60 ml Brut Champagne or Prosecco"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker except the wine, shake well with ice, strain into chilled elegant cocktail glass.",
      "Top up with the sparkling wine."
    ]
  },
  {
    "name": "Old Fashioned",
    "base": "Whiskey",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Bourbon or Rye Whiskey",
      "1 Sugar Cube",
      "Few Dashes Angostura Bitters",
      "Few Dashes Plain Water"
    ],
    "steps": [
      "Place sugar cube in old fashioned glass and saturate with bitter, add few dashes of plain water. Muddle until dissolved. Fill the glass with ice cubes and add whiskey.",
      "Stir gently."
    ]
  },
  {
    "name": "Paloma",
    "base": "Tequila",
    "taste": "New Era",
    "ingredients": [
      "50 ml 100% Agave Tequila",
      "5 ml Fresh lime",
      "A pinch of Salt",
      "100 ml Pink Grapefruit Soda"
    ],
    "steps": [
      "Poor the tequila into a highball glass, squeeze the lime juice.",
      "Add ice and salt, fill up pink grapefruit soda.",
      "Stir gently."
    ]
  },
  {
    "name": "Paper Plane",
    "base": "Whiskey",
    "taste": "New Era",
    "ingredients": [
      "30 ml Bourbon Whiskey",
      "30 ml Amaro Nonino",
      "30 ml Aperol",
      "30 ml Fresh Lemon Juice"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Paradise",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml Gin",
      "20 ml Apricot Brandy",
      "15 ml Fresh Orange Juice"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Penicillin",
    "base": "Gin",
    "taste": "New Era",
    "ingredients": [
      "60 ml Blended scotch whisky",
      "7.5 ml Lagavulin 16y",
      "22.5 ml Fresh lemon juice",
      "22.5 ml Honey syrup",
      "2-3 quarter size sliced fresh ginger"
    ],
    "steps": [
      "Muddle fresh ginger in a shaker and add the remaining ingredients except for the Islay single malt whisky.",
      "Fill the shaker with ice and shake.",
      "Fine train into a chilled Old Fashioned glass with ice.",
      "Float the single malt whisky on top."
    ]
  },
  {
    "name": "Pina Colada",
    "base": "Rum",
    "taste": "Contemporary Classics",
    "ingredients": [
      "50 ml White Rum",
      "30 ml Coconut Cream",
      "50 ml Fresh Pineapple Juice"
    ],
    "steps": [
      "Blend all the ingredients with ice in a electric blender,",
      "pour into a large glass and serve with straws.",
      "Note:\nHistorically a few drops of fresh lime juice was added to taste. 4 slices of fresh pineapple can be used instead of juice"
    ]
  },
  {
    "name": "Pisco Punch",
    "base": "Unknown",
    "taste": "New Era",
    "ingredients": [
      "60 ml Pisco",
      "22.5 ml Fresh Pineapple Juice",
      "15 ml Simple Syrup",
      "15 ml Fresh Lemon Juice",
      "30 ml Dry White Wine",
      "3 pcs Cloves"
    ],
    "steps": [
      "Gentle mash the simple syrup with the cloves, add the remaining ingredients except the wine.",
      "Shake vigorously and double strain into a large goblet.",
      "Add the wine on top and gently stir."
    ]
  },
  {
    "name": "Pisco Sour",
    "base": "Unknown",
    "taste": "Contemporary Classics",
    "ingredients": [
      "60 ml Pisco",
      "30 ml Fresh Lemon Juice",
      "20 ml Simple Syrup",
      "1 Raw whole Egg White"
    ],
    "steps": [
      "Add all ingredients into a shaker with ice.",
      "Shake and strain into a chilled goblet glass."
    ]
  },
  {
    "name": "Planters Punch",
    "base": "Rum",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Jamaican Rum",
      "15 ml Lime Juice",
      "30 ml Sugar Cane Juice"
    ],
    "steps": [
      "Pour all ingredients directly in a small tumbler or a typical terracotta glass.",
      "NOTE:\nAdd dilution up to taste, it can be given by water, ice or fresh juices."
    ]
  },
  {
    "name": "Porn Star Martini",
    "base": "Vodka",
    "taste": "New Era",
    "ingredients": [
      "50 ml Vanilla Vodka",
      "20 ml Passion Fruit Liqueur",
      "50 ml Passion Fruit Puree",
      "2 Bar Spoons Vanilla Sugar",
      "50 ml Champagne to serve on the side"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, double strain into a large chilled cocktail glass.",
      "Accompany with a shot of champagne."
    ]
  },
  {
    "name": "Porto Flip",
    "base": "Brandy",
    "taste": "The Unforgettables",
    "ingredients": [
      "15 ml Brandy",
      "45 ml Red Tawny Port Wine",
      "10 ml Egg Yolk"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Rabo de Galo",
    "base": "Unknown",
    "taste": "Contemporary Classics",
    "ingredients": [
      "60 ml Cachaca",
      "20 ml Sweet Vermouth Cinzano Rosso",
      "15 ml Cynar",
      "2 Drops Angostura (Optional)"
    ],
    "steps": [
      "Combine all the ingredients into a rocks glass, add ice and stir briefly."
    ]
  },
  {
    "name": "Remember the Maine",
    "base": "Whiskey",
    "taste": "The Unforgettables",
    "ingredients": [
      "60 ml Rye Whiskey",
      "22.5 ml Sweet Vermouth",
      "15 ml Cherry Brandy Luxardo",
      "7.5 ml Absinthe"
    ],
    "steps": [
      "Pour the absinthe into a coupe glass and swirl to completely coat the inside.",
      "Discard the absinthe and set the glass aside. Add the other ingredients to a mixing glass and fill it 3/4 full with ice. Stir until chilled, then strain into the glass rinsed with the absinthe."
    ]
  },
  {
    "name": "Russian Spring Punch",
    "base": "Vodka",
    "taste": "New Era",
    "ingredients": [
      "25 ml Vodka",
      "25 ml Fresh Lemon Juice",
      "15 ml Creme de Cassis",
      "10 ml Sugar Syrup",
      "Top up with Sparkling Wine"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker except the sparkling wine, shake well with ice, strain into chilled tall tumbler glass filled with ice",
      "and top up with sparkling wine."
    ]
  },
  {
    "name": "Rusty Nail",
    "base": "Whiskey",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Scotch Whisky",
      "25 ml Drambuie"
    ],
    "steps": [
      "Pour all ingredients directly into an old fashioned glass filled with ice.",
      "Stir gently."
    ]
  },
  {
    "name": "Sazerac",
    "base": "Brandy",
    "taste": "The Unforgettables",
    "ingredients": [
      "50 ml Cognac",
      "10 ml Absinthe",
      "1 Sugar Cube",
      "2 Dashes Peychaud’s Bitters"
    ],
    "steps": [
      "Rinse a chilled old-fashioned glass with the absinthe, add crushed ice and set it aside. Stir the remaining ingredients over ice in a mixing glass.",
      "Discard the ice and any excess absinthe from the prepared glass, strain the mixed drink into the glass.",
      "NOTE:\nThe original recipe changed after the American Civil War, Rye Whiskey substituted Cognac as it became hard to obtain."
    ]
  },
  {
    "name": "Sea Breeze",
    "base": "Vodka",
    "taste": "Contemporary Classics",
    "ingredients": [
      "40 ml Vodka",
      "120 ml Cranberry Juice",
      "30 ml Grapefruit Juice"
    ],
    "steps": [
      "Build all ingredients in a highball glass filled with ice."
    ]
  },
  {
    "name": "Sex on the Beach",
    "base": "Vodka",
    "taste": "Contemporary Classics",
    "ingredients": [
      "40 ml Vodka",
      "20 ml Peach Schnapps",
      "40 ml Fresh Orange Juice",
      "40 ml Cranberry Juice"
    ],
    "steps": [
      "Build all ingredients in a highball glass filled with ice."
    ]
  },
  {
    "name": "Sherry Cobbler",
    "base": "Unknown",
    "taste": "New Era",
    "ingredients": [
      "45 ml Amontillado sherry",
      "45 ml Palo Cortado",
      "1 tsp Superfine Sugar (or granulated)",
      "1/2  Orange Wheel",
      "1/2  Lemon Wheel"
    ],
    "steps": [
      "Combine sherry, sugar and 2 quarter wheels each of orange and lemon in a shaker with ice, shake briskly, strain into a Julep cocktail cup filled with crushed ice."
    ]
  },
  {
    "name": "Sidecar",
    "base": "Brandy",
    "taste": "The Unforgettables",
    "ingredients": [
      "50 ml Cognac",
      "20 ml Triple Sec",
      "20 ml Fresh Lemon Juice"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Singapore Sling",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "30 ml Gin",
      "15 ml Cherry Sangue Morlacco",
      "7.5 ml Cointreau",
      "7.5 ml DOM Bénédictine",
      "120 ml Fresh Pineapple Juice",
      "15 ml Fresh Lime Juice",
      "10 ml Grenadine Syrup",
      "A dash of Angostura bitters"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker filled with ice cubes.",
      "Shake well.",
      "Strain into Hurricane glass."
    ]
  },
  {
    "name": "South Side",
    "base": "Gin",
    "taste": "New Era",
    "ingredients": [
      "60 ml London dry Gin",
      "30 ml Fresh Lemon  Juice",
      "15 ml Simple syrup",
      "5/6 Mint leaves",
      "Few drops Egg white (Optional)"
    ],
    "steps": [
      "Pour all ingredients into a cocktail shaker, shake well with ice, double-strain into chilled cocktail glass.",
      "Note:\nIf egg white is used shake vigorously."
    ]
  },
  {
    "name": "Spicy Fifty",
    "base": "Vodka",
    "taste": "New Era",
    "ingredients": [
      "50 ml Vodka Vanilla",
      "15 ml Elderflower Cordial",
      "15 ml Fresh Lime Juice",
      "10 ml Monin Honey Syrup",
      "2 thin Slices Red Chili Pepper"
    ],
    "steps": [
      "Pour all ingredients into a cocktail shaker, shake well with ice, double-strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Spritz",
    "base": "Sparkling Wine",
    "taste": "New Era",
    "ingredients": [
      "90 ml Prosecco",
      "60 ml Aperol",
      "Splash of Soda water"
    ],
    "steps": [
      "Build all ingredients into a wine glass filled with ice.",
      "Stir gently.",
      "NOTE:\nThere are other versions of the Spritz that use Campari, Cynar or Select instead of Aperol."
    ]
  },
  {
    "name": "Stinger",
    "base": "Brandy",
    "taste": "The Unforgettables",
    "ingredients": [
      "50 ml Cognac",
      "20 ml White Crème de Menthe"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes. Stir well.",
      "Strain into chilled martini cocktail glass."
    ]
  },
  {
    "name": "Suffering Bastard",
    "base": "Gin",
    "taste": "New Era",
    "ingredients": [
      "30 ml Cognac or Brandy",
      "30 ml Gin",
      "15 ml Fresh Lime Juice",
      "2 Dashes Angostura Bitters",
      "Top up Ginger beer"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker except the ginger beer, shake well with ice.",
      "Pour unstrained into a Collins glass or in the original.",
      "S. Bastard mug and top up with ginger beer."
    ]
  },
  {
    "name": "Tequila Sunrise",
    "base": "Tequila",
    "taste": "Contemporary Classics",
    "ingredients": [
      "45 ml Tequila",
      "90 ml Fresh Orange Juice",
      "15 ml Grenadine Syrup"
    ],
    "steps": [
      "Pour tequila and orange juice directly into highball glass filled with ice cubes.",
      "Add the grenadine syrup to create chromatic effect (sunrise), do not stir."
    ]
  },
  {
    "name": "Three Dots and a Dash",
    "base": "Rum",
    "taste": "New Era",
    "ingredients": [
      "45 ml Rhum Martinique Agricole",
      "15 ml Blended Aged Rum",
      "7.5 ml Falernum",
      "7.5 ml Allspice Saint Elizabeth15 ml Fresh Lime Juice",
      "15 ml Fresh Orange juice",
      "15 ml Honey Syrup",
      "2 Dashes Angostura Bitters"
    ],
    "steps": [
      "Pour all ingredients in a Blender with 12 ounces of crushed ice, flash blend, pour the drink into a footed copo glass.",
      "Fill the glass with more crushed ice."
    ]
  },
  {
    "name": "Tommy’s Margarita",
    "base": "Tequila",
    "taste": "New Era",
    "ingredients": [
      "60 ml Tequila 100% agave",
      "30 ml Fresh Lime Juice",
      "30 ml Agave Nectar"
    ],
    "steps": [
      "Pour all ingredients into a cocktail shaker, shake well with ice, strain into chilled rocks glass filled with ice."
    ]
  },
  {
    "name": "Trinidad Sour",
    "base": "Whiskey",
    "taste": "New Era",
    "ingredients": [
      "45 ml Angostura Bitters",
      "30 ml Orgeat Syrup",
      "22.5 ml Fresh Lemon Juice",
      "15 ml Rye Whiskey"
    ],
    "steps": [
      "Pour all ingredients into a cocktail shaker, shake well with ice.",
      "Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Tuxedo",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml Old Tom Gin",
      "30 ml Dry Vermouth",
      "1/2 Bar Spoon Maraschino Luxardo",
      "1/4 Bar Spoon of Absinthe",
      "3 Dashes Orange Bitters"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes. Stir well.",
      "Strain into chilled martini cocktail glass."
    ]
  },
  {
    "name": "Ve.N.To",
    "base": "Unknown",
    "taste": "New Era",
    "ingredients": [
      "45 ml White Smooth Grappa",
      "22.5 ml Fresh lemon Juice",
      "15 ml Honey mix (replace water with chamomile)*",
      "15 ml Chamomile cordial",
      "Few Drops of Egg White (Optional)"
    ],
    "steps": [
      "Pour all ingredients into the shaker. Shake vigorously with ice.",
      "Strain into a chilled small tumbler glass filled with ice.",
      "NOTE:\n*If desired water can be replaced by chamomile infusion in the honey mix."
    ]
  },
  {
    "name": "Vesper",
    "base": "Gin",
    "taste": "Contemporary Classics",
    "ingredients": [
      "45 ml Gin",
      "15 ml Vodka",
      "7.5 ml Lillet Blanc"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker filled with ice cubes.",
      "Shake and strain into a chilled cocktail glass."
    ]
  },
  {
    "name": "Vieux Carré",
    "base": "Whiskey",
    "taste": "The Unforgettables",
    "ingredients": [
      "30 ml Rye Whiskey",
      "30 ml Cognac",
      "30 ml Sweet Vermouth",
      "1 Bar Spoon Bénédictine",
      "2 Dashes Peychaud’s Bitters"
    ],
    "steps": [
      "Pour all ingredients into mixing glass with ice cubes.",
      "Stir well. Strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Whiskey Sour",
    "base": "Whiskey",
    "taste": "The Unforgettables",
    "ingredients": [
      "45 ml Bourbon Whiskey",
      "25 ml Fresh Lemon Juice",
      "20 ml Sugar Syrup",
      "Few Drops of Egg White (Optional)"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker filled with ice. Shake well.",
      "Strain into cobbler glass. If served “On the rocks”, strain ingredients",
      "into old fashioned glass filled with ice.",
      "NOTE:\nIf egg white is used shake little harder to release and incorporate the foam from the egg white."
    ]
  },
  {
    "name": "White Lady",
    "base": "Gin",
    "taste": "The Unforgettables",
    "ingredients": [
      "40 ml Gin",
      "30 ml Triple Sec",
      "20 ml Fresh Lemon Juice"
    ],
    "steps": [
      "Pour all ingredients into cocktail shaker, shake well with ice, strain into chilled cocktail glass."
    ]
  },
  {
    "name": "Zombie",
    "base": "Rum",
    "taste": "Contemporary Classics",
    "ingredients": [
      "45 ml Jamaican dark rum",
      "45 ml Gold Puerto Rican rum",
      "30 ml Demerara Rum",
      "20 ml Fresh lime juice",
      "15 ml Falernum",
      "15 ml Donn’s Mix*",
      "1 tsp Grenadine syrup",
      "1 dash Angostura bitters",
      "6 drops Pernod"
    ],
    "steps": [
      "Add all ingredients into an electric blender with 170 grams of cracked ice.",
      "With pulse bottom blend for a few seconds. Serve in a tall tumbler glass.",
      "Note:\n*Donn’s Mix: 2 parts of fresh yellow grapefruit and 1 part of cinnamon syrup"
    ]
  }
]


def print_header() -> None:
    print("\n=== Cocktail Mini App (Offline) ===")
    print("1) Random cocktail")
    print("2) Filter by base spirit")
    print("3) Filter by taste")
    print("4) List all cocktails")
    print("0) Exit")


def name_line(cocktail: Dict) -> str:
    return f"--- {cocktail['name']} ---"


def show_cocktail(cocktail: Dict) -> None:
    print(f"\n{name_line(cocktail)}")
    print(f"Base: {cocktail['base']} | Taste: {cocktail['taste']}")
    print("Ingredients:")
    for item in cocktail["ingredients"]:
        print(f"- {item}")
    print("Steps:")
    for idx, step in enumerate(cocktail["steps"], start=1):
        print(f"{idx}. {step}")


def list_names(cocktails: List[Dict]) -> None:
    if not cocktails:
        print("No results.")
        return
    for idx, cocktail in enumerate(cocktails, start=1):
        print(f"{idx}. {cocktail['name']} ({cocktail['base']}, {cocktail['taste']})")


def choose_and_show(cocktails: List[Dict]) -> None:
    if not cocktails:
        print("No matching cocktail.")
        return

    list_names(cocktails)
    selected = input("\nEnter number to view details (Enter to skip): ").strip()
    if not selected:
        return

    if not selected.isdigit():
        print("Invalid input.")
        return

    idx = int(selected)
    if idx < 1 or idx > len(cocktails):
        print("Out of range.")
        return
    show_cocktail(cocktails[idx - 1])


def random_cocktail(cocktails: List[Dict]) -> None:
    show_cocktail(random.choice(cocktails))


def filter_by_base(cocktails: List[Dict]) -> None:
    bases = sorted({c["base"] for c in cocktails})
    print("\nAvailable base spirits:", ", ".join(bases))
    target = input("Type a base spirit: ").strip().lower()
    result = [c for c in cocktails if c["base"].lower() == target]
    choose_and_show(result)


def filter_by_taste(cocktails: List[Dict]) -> None:
    tastes = sorted({c["taste"] for c in cocktails})
    print("\nAvailable tastes:", ", ".join(tastes))
    target = input("Type a taste: ").strip().lower()
    result = [c for c in cocktails if c["taste"].lower() == target]
    choose_and_show(result)


def list_all(cocktails: List[Dict]) -> None:
    choose_and_show(cocktails)


def main() -> None:
    cocktails = COCKTAILS
    print(f"Loaded {len(cocktails)} cocktails (embedded offline data).")

    while True:
        print_header()
        cmd = input("Select: ").strip()

        if cmd == "1":
            random_cocktail(cocktails)
        elif cmd == "2":
            filter_by_base(cocktails)
        elif cmd == "3":
            filter_by_taste(cocktails)
        elif cmd == "4":
            list_all(cocktails)
        elif cmd == "0":
            print("Bye.")
            break
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()
