from lib.TMA4100.fixed_point_iteration import main as fixed_point_iteration
from lib.TMA4100.newton import main as newton
from lib.TMA4140.chinese_remainder_theorem import main as chinese_remainder_theorem
from lib.TMA4140.truth_table import main as truth_table
from lib.TMA4140.relation_properties import main as relation_properties


COURSES = ("TMA4100 - Calculus 1", "TMA4140 - Discrete Mathematics")
COURSE = None

TOOLS = {
	0: 	(("Fixed point iteration", fixed_point_iteration),
		("Newton", newton)),

	1: 	(("Chinese remainder theorem", chinese_remainder_theorem),
		("Truth table", truth_table),
		("Relation properties", relation_properties))
}
TOOL = None


def ask_for_course():
	global COURSE
	print("\nCourses: ")
	for i, course in enumerate(COURSES):
		print("\t", i, course)
	COURSE = max(0, min(len(COURSES)-1, int(input("\nChoose course: ")))) 


def ask_for_tool():
	global TOOL
	print("\nTOOLS:")
	for i, tool in enumerate(TOOLS[COURSE]):
		print("\t", i, tool[0])
	TOOL = max(0, min(len(COURSES)-1, int(input("\nChoose tool: ")))) 
	

def main():
	print("\nWelcome to CSauto / Computer Science - automated.")
	command = "\n"
	while True:
		if COURSE == None or TOOL == None or command != "r":
			ask_for_course()
			ask_for_tool()
		try:
			TOOLS[COURSE][TOOL][1]()
		except Exception as e:
			print(f"ERROR - {e}")
		command = input("\nTool complete\nq (exit), r (replay tool), enter (main): ")
		if command == "q":
			break

if __name__ == "__main__":
	main()
