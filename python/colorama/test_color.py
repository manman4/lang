from colorama import Fore, Style

# colorama.pyとするとimportで衝突するため、test_color.pyに記載

print(Fore.RED + "赤文字")
print(Fore.GREEN + "緑文字")
print(Style.RESET_ALL + "通常の文字")