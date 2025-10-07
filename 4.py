class Panda:
	def __init__(self,lengtharms:float,lengthlegs:float,numbereyes:int,tail: bool,furry:bool):
		self.lengtharms = lengtharms
		self.lengthlegs = lengthlegs
		self.numbereyes = numbereyes
		self.tail = tail
		self.furry = furry

	def describe(self):
		print(f"lengtharms is:{self.lengtharms}")
		print(f"lengthlegs is:{self.lengthlegs}")
		print(f"numbereyes is:{self.numbereyes}")
		print(f"lengtharms is:{self.lengtharms}")
		print(f"tail is:{self.tail}")
		print(f"furry is:{self.furry}")




def main():
	Mammal = Panda(lengtharms= 0.5,lengthlegs= 0.6,numbereyes = 2,tail = True, furry = True)
	Mammal.describe()

if __name__ == "__main__":
    main()