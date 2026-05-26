from web_research.online_reader import read_webpage


url = "https://codes.iccsafe.org/"

print("Reading webpage...")

text = read_webpage(url)

print("\nWEBPAGE TEXT PREVIEW:\n")
print(text[:2000])