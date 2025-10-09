import numpy as np

def main():
	x_value = np.linspace(0, 2, 1000)

	for x in x_value:
		print(f"x:{x:.3f}, sin(x):{np.sin(x):.3f}")

if __name__ == "__main__":
    main()
