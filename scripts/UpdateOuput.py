import os
import shutil

def recursive_copy(start_path, target_base,relative=""):
	for item in os.listdir(start_path + "\\" + relative):
		if os.path.isdir(start_path + relative + "\\" + item):
			if not os.path.isdir(target_base + relative + "\\" + item):
				os.mkdir(target_base + relative + "\\" + item)
				print("Created dir" + target_base + relative + "\\" + item)
			recursive_copy(start_path, target_base,relative+"\\"+item)
		elif item.split(".")[-1] == "pdf" and not os.path.exists(target_base + relative + "\\" + item):
			print("Coppied " + item)
			shutil.copyfile(start_path + relative + "\\" +item, target_base + relative + "\\" + item)

os.chdir("F:\\School\\L6\\Maths\\ALevelFurtherMathsNotes\\src")
recursive_copy(".\\","..\\Output")
