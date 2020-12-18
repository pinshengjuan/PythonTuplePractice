
def main():
	word = 'echo'
	t = ()
	count = 3

	for i in range(len(word)):
		for j in range(count):
			t = t + (word[i:], )
	print(t)

	return

if __name__ == '__main__':
    main()	