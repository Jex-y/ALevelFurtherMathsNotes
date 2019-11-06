import os
import shutil

def recursive_copy(start_path, target_base,relative=""):
	for item in os.listdir(start_path + "\\" + relative):
		if os.path.isdir(start_path + relative + "\\" + item):
			recursive_copy(start_path, target_base,relative+"\\"+item)
		elif item.split(".")[-1] == "pdf" and item != "master.pdf": #and not os.path.exists(target_base + relative + "\\" + item)
			print("Coppied " + item)
			if not os.path.isdir("\\".join((target_base + relative).split("\\")[:-1])):
				os.mkdir("\\".join((target_base + relative).split("\\")[:-1]))
				print("Created dir" + "\\".join((target_base + relative).split("\\")[:-1]))
			shutil.copyfile(start_path + relative + "\\" +item, target_base + relative + ".pdf")

os.chdir("F:\\School\\L6\\Maths\\ALevelFurtherMathsNotes\\src")
recursive_copy(".\\","..\\Output")
