# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
fpath = "birth_dev.tsv"
ct = 0
# shortcut: use .readlines()
for line in open(fpath, encoding='utf-8'):
	ct += 1
total, correct = utils.evaluate_places(fpath, ["London"]*ct)
if total > 0:
	print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
	print("nototal")