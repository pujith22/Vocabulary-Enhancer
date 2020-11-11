# I am using Trie data structure to store the information and also keeping a count of the information

class Trie:
	def __init__(self):
		self.dic = {}
	def insert(self,word):
		self.dic[word]=True
	def search(self,word):
		if (self.dic.get(word)!=None):
			return True
		else:
			return False
	
from english_words import english_words_lower_alpha_set as wordList
from PyDictionary import PyDictionary
import time
from time import sleep
from os import system
class Game:
	def __init__(self,m,n,no_of_players):
		self.ROWS = m
		self.COLUMNS = n
		self.GRID = []
		self.NOP = no_of_players
		self.playerWordList = []
		for i in range(self.NOP):
			self.playerWordList.append([])
		# grid size would be m x n
		# And initializing it with "-1"
		for i in range(m):
			self.GRID.append([])
			for j in range(n):
				self.GRID[-1].append("_")
		# for already made word
		self.visitedDict = {}
		# for getting meaning of the formed word
		self.meaningDict = PyDictionary()
		# Trie for making the search each
		self.wordLadder = Trie()
		# Bulding the Trie with valid words of the language.
		for word in wordList:
			self.wordLadder.insert(word)
		self.playerScores = []
		for i in range(no_of_players):
			self.playerScores.append(0)

	def insert(self,rowIndex,colIndex,character):
		self.GRID[rowIndex][colIndex]=character
		start_index = -1
		end_index = -1
		orientation = -1
		formedWord = ""
		# for orientation 1 (i.e Horizontal)
		for startIndex in range(0,colIndex+2):
			for endIndex in range(colIndex,self.COLUMNS):
				word = ""
				for i in range(startIndex,endIndex+1):
					#if(self.GRID[rowIndex][i]!="_"):
					word += self.GRID[rowIndex][i]
				if(self.wordLadder.search(word)):
					if(len(word)>len(formedWord)):
						formedWord = word
						start_index = startIndex
						end_index = endIndex
						orientation = 1
		# for orientation 2 (i.e Vertical)
		for startIndex in range(0,rowIndex+1):
			for endIndex in range(rowIndex,self.ROWS):
				word = ""
				for i in range(startIndex,endIndex+1):
					word += self.GRID[i][colIndex]
				if(self.wordLadder.search(word)):
					if(len(word)>len(formedWord)):
						formedWord = word
						start_index = startIndex
						end_index = endIndex
						orientation = 2
		# for orientation 3 (i.e )
		return (formedWord,start_index,end_index,orientation)

	def printWelcomeScreen(self):
		import pyfiglet  
		result = pyfiglet.figlet_format("WELCOME TO VOCABULARY ENHANCER", font = "standard" ) 
		print(result) 

	def splashScreen(self):
		system("cls")
		self.printWelcomeScreen()
		sleep(2)
		system("cls")
		print("Loading...")
		sleep(2)
		system("cls")
		print("\n\n\n\t\t\t")
		self.gameLogic()
		
	def print_game_screen(self):
		print("\n\n\t\t\t")
		for i in range(self.ROWS):
			for j in range(self.COLUMNS):
				print(self.GRID[i][j],end=" ")
			print("\t\t\t")
		print("\n\n\n\n\t\tSCORES:\n")
		for i in range(self.NOP):
			print("\t\tPlayer "+str(i+1)+": "+str(self.playerScores[i])+" ")
		print("\n\t")
		print("Enter your input in the format(rowIndex,colIndex,character): ",end=" ")

	def gameLogic(self):
		self.print_game_screen()
		while(not self.isFilled()):
			for i in range(self.NOP):
				sleep(2)
				system("cls")
				self.print_game_screen()
				row,col,char = map(str,input().split())
				row = int(row)
				col = int(col)
				tup = self.insert(row-1,col-1,char)				
				word = tup[0]
				rowIndex = tup[1]
				colIndex = tup[2]
				orientation = tup[3]
				if(len(word)>=1):
					if (self.visitedDict.get(word)==None):
						self.visitedDict[word]=True
						self.playerScores[i]+=len(word)
						self.playerWordList.append(tup)
						print("\n\tWord Formed: "+word)
						print("\n\tMeaning: ")
						print(self.meaningDict.meaning(word))
						print("\n")
						print("\n\tSynonyms: ")
						print(self.meaningDict.synonym(word))
						print("\n\tAntonyms: ")
						print(self.meaningDict.antonym(word))
					else:
						print("\nSorry, the word was already made. No score this time!")
				else:
					print("\nSorry, You are unable to make any valid word. Better luck next time!")


	def isFilled(self):
		for i in range(self.ROWS):
			for j in range(self.COLUMNS):
				if(self.GRID[i][j]=="_"):
					return False
		return True


if __name__=="__main__":
	game = Game(5,5,2)
	game.splashScreen()