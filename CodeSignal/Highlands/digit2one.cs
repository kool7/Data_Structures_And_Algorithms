string s = "Hello123";
string result = "";

foreach (char c in s) {
    if (char.IsDigit(c)) {
        int digit = int.Parse(c.ToString());
        result += new string('1', digit);
    } else {
        result += c;
    }
}

Console.WriteLine(result);