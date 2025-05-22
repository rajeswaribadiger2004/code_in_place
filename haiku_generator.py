from ai import call_gpt

def main():
    #using the stanford CIP5 AI module, this code produces custom Haikus in the built in console
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Thinking...")
    haiku = call_gpt("please make a haiku including the following name: " + name + "and the following topic" + topic)
    print(haiku)



#boilerplate code
if __name__ == "__main__":
    main()
