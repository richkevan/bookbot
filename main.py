def main():
  def count_words(text):
      return len(text.split())
    
  def count_characters(text):
    char_count = {}
    char_list = []
    for char in text:
      if char in char_count.keys():
        char_count[char] += 1
      else:
        char_count[char] = 1
    for key in char_count.keys():
      char_list.append({"name": key, "count": char_count[key]})
    char_list = sorted(char_list, key=lambda x: x["count"], reverse=True)
    return char_count, char_list

  with open("./frankenstein.txt", 'r') as file:
      text = file.read()
      words = count_words(text)
      char_dict, char_list = count_characters(text)
      print(f"Words: {words}")
      for item in char_list:
          print(f"{item["name"]} : {item["count"]}")





if __name__ == "__main__":
  main() 